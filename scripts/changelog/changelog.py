import requests, re, base64, json, datetime, os, pandas, sys
from datetime import datetime as dt

github_token = sys.argv[1]

host = 'https://api.github.com'

github_headers = {'Authorization': 'token ' + github_token, 'Accept': 'application/vnd.github.v3+json'}

repo_list = []
pr_list = []

last_week = (dt.today() - datetime.timedelta(days=8)).date()

changelog_prs = []
documented = []
to_document = []
to_ignore = []

path = '../../_changelog-files/drafts'

def createDir():
    if os.path.exists(path) == False:
        os.makedirs(path)
    else: 
        pass

def getPRsToIgnore():
    with open('ignore.txt', 'r', encoding='utf8') as f:
        ignore = f.readlines()
        for item in ignore:
            item = item.strip()
            to_ignore.append(item)

def getDocumentedPRs():
    for root, dirs, files in os.walk('../../_changelog-files'):
        for file in files:
            if file.endswith('.md'):
                changelog_file = os.path.join(root, file)
                with open(changelog_file, encoding='utf8') as changelog:
                    changelog_lines = changelog.readlines()
                    for line in changelog_lines:
                        if line.startswith('pull-request:'):
                            link = re.search('^pull-request\:\s\"(.*)\"$', line).group(1)
                            documented.append(link)

def getRepoList():

    page = 0
    length = 100

    while length == 100:
        page += 1
        api = host + '/orgs/singer-io/repos'
        params = '?per_page=100&page=' + str(page) + '&type=public'
        r = json.loads(requests.get(api + params, headers=github_headers).content)
        length = len(r)
        for repo in r:
            name = repo['name']
            pushed = repo['pushed_at']
            base = repo['default_branch']
            push_date = dt.strptime(pushed, "%Y-%m-%dT%H:%M:%SZ").date()
            if name.startswith('tap-') and push_date > last_week:
                repo_list.append([name, base])
            else:
                pass

def getPRList():

    for repo in repo_list:

        name = repo[0]
        base = repo[1]

        page = 0
        length = 100

        while length == 100:
            page += 1

            api = host + '/repos/singer-io/' + name + '/pulls'

            params = '?state=closed&base=' + base + '&page=' + str(page)

            r = json.loads(requests.get(api + params, headers=github_headers).content)

            length = len(r)

            for pull in r:
                number = pull['number']
                title = pull['title']
                url = pull['html_url']
                merged = pull['merged_at']

                if merged != None:
                    date = dt.strptime(merged, "%Y-%m-%dT%H:%M:%SZ").date()
                    if date > last_week:
                        pr_list.append([name, number, title, url, date])

def getPRsToDocument():

    prs = pandas.DataFrame(pr_list, columns=['repository', 'pr_number', 'pr_title', 'pr_url', 'pr_merge_date'])

    for index, row in prs.iterrows():
        
        name = row[0]
        number = row[1]
        title = row[2]
        url = row[3]
        date = row[4]

        api = 'https://api.github.com/repos/singer-io/' + name + '/pulls/' + str(number) + '/files'

        r = requests.get(api, headers=github_headers)
        if r.status_code == 200:
            response = json.loads(r.content)
            for file in response:
                if file['filename'] == 'CHANGELOG.md':
                    changelog_prs.append([url, date])
                    content_url = file['contents_url']
                    f = requests.get(content_url, headers=github_headers)
                    file_content = json.loads(f.content)
                    content = file_content['content']
                    text = str(base64.b64decode(content))
                    pattern = re.compile(r'https\://github.com/singer-io/[^/]+/pull/\d+')
                    pulls = re.findall(pattern, text)
                    for pull in pulls:
                        if pull in documented or pull in to_ignore:
                            pass
                        else:
                            target = prs.loc[prs['pr_url'] == pull]
                            list = target.values.tolist()
                            if len(list) > 0:
                                pr = list[0]
                                if pr not in to_document:
                                    print(pr)
                                    tap = pr[0].replace('tap-', '')
                                    pr_number = str(pr[1])
                                    pr_title = pr[2]
                                    pr_url = pr[3]
                                    pr_date = pr[4].strftime('%Y-%m-%d')
                                    to_document.append(pr)
                                    md_filename = path + '/' + pr_date + '-' + tap + '-' + pr_number + '.md'
                                    md_text = '---\ntitle: "' + pr_title + '"\ncontent-type: ""\ndate: ' + pr_date + '\nentry-type: \nentry-category: integration\nconnection-id: \nconnection-version: \npull-request: "' + pr_url + '"\n---'

                                    with open(md_filename, 'w') as out:
                                        out.write(md_text)


createDir()
getDocumentedPRs()
getPRsToIgnore()
getRepoList()
getPRList()
getPRsToDocument()