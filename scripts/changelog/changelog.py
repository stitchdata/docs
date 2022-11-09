import requests, re, base64, json, datetime, os, pandas, sys
from datetime import datetime as dt

# GitHub info
github_token = sys.argv[1]
host = 'https://api.github.com'
github_headers = {'Authorization': 'token ' + github_token, 'Accept': 'application/vnd.github.v3+json'}

# Date range parameter
nb_days = int(sys.argv[2])


# Folder for new files
path = '../../_changelog-files/drafts'

start_date = (dt.today() - datetime.timedelta(days=nb_days)).date()

repo_list = []
pr_list = []
documented = []
to_document = []
to_ignore = []

def createDir(): # Check if the drafts folder exists and create it if it doesn't
    if os.path.exists(path) == False:
        os.makedirs(path)
    else: 
        pass

def getPRsToIgnore(): # Check the ignore.txt file for PRs that shouldn't be documented
    with open('ignore.txt', 'r', encoding='utf8') as f:
        ignore = f.readlines()
        for item in ignore:
            item = item.strip()
            to_ignore.append(item)

def getDocumentedPRs(): # Get PRs that already have a changelog file

    # Get all markdown files in changelog-files
    for root, dirs, files in os.walk('../../_changelog-files'):
        for file in files:
            if file.endswith('.md'):
                changelog_file = os.path.join(root, file)
                with open(changelog_file, encoding='utf8') as changelog:
                    changelog_lines = changelog.readlines()
                    
                    # Find the line that contains the PR URL
                    for line in changelog_lines:
                        if line.startswith('pull-request:'):
                            link = re.search('^pull-request\:\s\"(.*)\"$', line).group(1)

                            # Add the URL to the list of PRs already added in the changelog
                            documented.append(link)

def getRepoList(): # Get the list of all tap repositories in the singer-io organization

    # Create loop until the last page of the repository list is reached
    page = 0
    length = 100
    while length == 100:
        page += 1
        api = host + '/orgs/singer-io/repos'
        params = '?per_page=100&page=' + str(page) + '&type=public'
        r = json.loads(requests.get(api + params, headers=github_headers).content)
        length = len(r)
        for repo in r:

            # For each repository, get the repo name, the base branch and the date of the last commit pushed
            name = repo['name']
            base = repo['default_branch']
            pushed = repo['pushed_at']
            push_date = dt.strptime(pushed, "%Y-%m-%dT%H:%M:%SZ").date()

            # If the repository is a tap repo and if the last commit was done in the past week, add the repo to the list or repos to check for new PRs
            if name.startswith('tap-') and push_date > start_date:
                repo_list.append([name, base])
            else:
                pass

def getPRList(): # Get a list of PRs merged in the past week on all repos

    # For each repo in the list, get the repo name and the name of the default branch
    for repo in repo_list:
        name = repo[0]
        base = repo[1]

        # Create loop until the last page of the PR list is reached
        page = 0
        length = 100
        while length == 100:
            page += 1
            # Get all PRs that are closed and had the default branch as base
            api = host + '/repos/singer-io/' + name + '/pulls'
            params = '?state=closed&base=' + base + '&page=' + str(page)
            r = json.loads(requests.get(api + params, headers=github_headers).content)
            length = len(r)

            # For each PR in the response, get the PR number, title, url and merge date
            for pull in r:
                number = pull['number']
                title = pull['title']
                url = pull['html_url']
                merged = pull['merged_at']

                # Filter out PRs that were closed without being merged
                if merged != None:
                    date = dt.strptime(merged, "%Y-%m-%dT%H:%M:%SZ").date()

                    # If a PR was merged in the past week, add it to the list of PRs to check
                    if date > start_date:
                        pr_list.append([name, number, title, url, date])

def getPRsToDocument(): # Find PRs that need to be documented and create draft changelog files

    # Make the PR list into a DataFrame
    prs = pandas.DataFrame(pr_list, columns=['repository', 'pr_number', 'pr_title', 'pr_url', 'pr_merge_date'])

    for index, row in prs.iterrows():
        name = row[0]
        number = row[1]

        # For each PR, check the files updated
        api = 'https://api.github.com/repos/singer-io/' + name + '/pulls/' + str(number) + '/files'
        r = requests.get(api, headers=github_headers)
        if r.status_code == 200:
            response = json.loads(r.content)
            for file in response:

                # Filter on PRs where the changelog file was modified
                if file['filename'] == 'CHANGELOG.md':

                    # Get and decode the contents of the changelog file
                    content_url = file['contents_url']
                    f = requests.get(content_url, headers=github_headers)
                    file_content = json.loads(f.content)
                    content = file_content['content']
                    text = str(base64.b64decode(content))

                    # Find all PRs mentioned in the changelog file
                    pattern = re.compile(r'https\://github.com/singer-io/[^/]+/pull/\d+')
                    pulls = re.findall(pattern, text)
                    for pull in pulls:

                        # For each PR mentioned, check if it is already documented or should be ignored
                        if pull in documented or pull in to_ignore:
                            pass
                        else:

                            # If the PR should be documented, find the URL in the PRs DataFrame
                            target = prs.loc[prs['pr_url'] == pull]
                            list = target.values.tolist()
                            if len(list) > 0:
                                pr = list[0]
                                if pr not in to_document:
                                    print(pr)

                                    # If the PR is not already in the list of PRs to document, get the name of the tap, and the PR number, title, URL and merge date from the DataFrame
                                    tap = pr[0].replace('tap-', '')
                                    pr_number = str(pr[1])
                                    pr_title = pr[2]
                                    pr_url = pr[3]
                                    pr_date = pr[4].strftime('%Y-%m-%d')

                                    # Add the PR to the list of PRs to document
                                    to_document.append(pr)

                                    # Create the filename and content of the changelog file and create it
                                    md_filename = path + '/' + pr_date + '-' + tap + '-' + pr_number + '.md'
                                    md_text = '---\ntitle: "' + pr_title + '"\ncontent-type: "changelog-entry"\ndate: ' + pr_date + '\nentry-type: \nentry-category: integration\nconnection-id: \nconnection-version: \npull-request: "' + pr_url + '"\n---\n{{ site.data.changelog.metadata.single-integration | flatify }}'
                                    with open(md_filename, 'w') as out:
                                        out.write(md_text)

    # Print results
    count = len(to_document)
    if count > 0:
        print(str(count) + ' pull requests to document')
    else: 
        print('No pull requests to document')


createDir()
getDocumentedPRs()
getPRsToIgnore()
getRepoList()
getPRList()
getPRsToDocument()