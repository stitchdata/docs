import requests, re, base64, json, datetime, os, pandas, sys, yaml
from datetime import datetime as dt

# GitHub info
github_token = sys.argv[1]
host = 'https://api.github.com'
github_headers = {'Authorization': 'token ' + github_token, 'Accept': 'application/vnd.github.v3+json'}

# Date range parameter
nb_days = int(sys.argv[2])


# Folder for new files
year = dt.today().strftime('%Y')
path = f'../../_changelog-files/{year}'

start_date = (dt.today() - datetime.timedelta(days=nb_days)).date()

repo_list = []
pr_list = []
documented = []
to_document = []
to_ignore = []
integration_dict = {}

# Lists of words to guess the entry type
bug_fix = ['fix', 'fixed', 'fixing']
deprecation = ['deprecate', 'deprecated','deprecating', 'deprecation']
improvement = ['improve', 'improved', 'improving', 'improvement', 'enhance', 'enhanced', 'enhancing', 'enhancement', 'update', 'updated', 'updating', 'upgrade', 'upgraded', 'upgrading']
issue_identified = ['identify', 'identified', 'identifying']
new_feature = ['new version']
removed = ['remove', 'removed', 'removing', 'removal']

def createDir(): # Check if the target folder exists and create it if it doesn't
    if os.path.exists(path) == False:
        os.makedirs(path)
    else:
        pass

def createIntegrationDict(): # Create a dictionary of all integrations from the integrations.yml file
    with open('../../_data/taps/integrations.yml', 'r') as file:
        yaml_data = yaml.safe_load(file)
        integration_dict.update(yaml_data['integrations'])

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
                            link = re.search(r'^pull-request\:\s\"(.*)\"$', line).group(1)

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
        name = row.iloc[0]
        number = row.iloc[1]

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
                                    tap_raw = pr[0]
                                    tap = tap_raw.replace('tap-', '')
                                    pr_number = str(pr[1])
                                    pr_title = pr[2]
                                    pr_url = pr[3]
                                    pr_date = pr[4].strftime('%Y-%m-%d')

                                    # Add the PR to the list of PRs to document
                                    to_document.append(pr)

                                    # Get connection information from integrations.yaml
                                    connection_id_found = False
                                    connection_name_found = False
                                    for key, value in integration_dict.items():
                                        if value['tap'] == tap_raw:
                                            connection_id = value['id']
                                            connection_id_found = True
                                            connection_name = value['display_name']
                                            connection_name_found = True
                                            break
                                    if not connection_id_found:
                                        connection_id = 'NOT FOUND'
                                    if not connection_name_found:
                                        connection_name = 'NOT FOUND'

                                    # Get latest connection version
                                    with open(f'../../_data/taps/versions/{connection_id}.yml', 'r') as file:
                                        yaml_data = yaml.safe_load(file)
                                        connection_version = yaml_data['latest-version']

                                    # Process PR title
                                    pr_title = re.sub(r'\w*-\d*\s?:\s?', '', pr_title)
                                    pr_title_for_md_description = pr_title[0].lower() + pr_title[1:]
                                    pr_title_for_md_filename = pr_title.lower().replace(' ', '-').replace(':', '-').replace(',', '-').replace('.', '-').replace('--', '-')

                                    # Guess the entry type from the PR title
                                    entry_type = 'NOT FOUND'
                                    pr_title_lower = pr_title.lower()
                                    entry_types = [
                                        ('bug-fix', bug_fix),
                                        ('deprecation', deprecation),
                                        ('improvement', improvement),
                                        ('issue-identified', issue_identified),
                                        ('new-feature', new_feature),
                                        ('removed', removed)
                                    ]
                                    for type, keywords in entry_types:
                                        if any(word in pr_title_lower for word in keywords):
                                            entry_type = type
                                            break

                                    # Create the filename and content of the changelog file and create it
                                    md_filename = f'{path}/{pr_date}-{tap}-v{connection_version}-{pr_title_for_md_filename}.md'
                                    md_text = f'---\ntitle: "{connection_name} (v{connection_version}): {pr_title}"\ncontent-type: "changelog-entry"\ndate: {pr_date}\nentry-type: {entry_type}\nentry-category: integration\nconnection-id: {connection_id}\nconnection-version: {connection_version}\npull-request: "{pr_url}"\n---\n{{ site.data.changelog.metadata.single-integration | flatify }}\n\nWe\'ve improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to {pr_title_for_md_description}.'
                                    with open(md_filename, 'w') as out:
                                        out.write(md_text)

    # Print results
    count = len(to_document)
    if count > 1:
        print(f'{str(count)} pull requests to document')
    elif count == 1:
        print('1 pull request to document')
    else: 
        print('No pull requests to document')


createDir()
createIntegrationDict()
getDocumentedPRs()
getPRsToIgnore()
getRepoList()
getPRList()
getPRsToDocument()