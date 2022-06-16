import snowflake.connector, requests, re, base64, json, datetime, os, pandas, sys
from datetime import datetime as dt

github_token = sys.argv[1]
snowflake_user = sys.argv[2]
snowflake_password = sys.argv[3]

github_headers = {'Authorization': 'token ' + github_token, 'Accept': 'application/vnd.github.v3+json'}

pr_list = []

con = snowflake.connector.connect(
    user=snowflake_user,
    password=snowflake_password,
    account='TALENDCDW',
    warehouse='STITCH_WH',
    database='STITCHCDW',
    role= "STITCH_READONLY"
)

today = dt.today().date()
last_week = (dt.today() - datetime.timedelta(days=8)).date()

changelog_prs = []
documented = []
all_prs = []
to_document = []

def getDocumentedPRs():
    for root, dirs, files in os.walk('../_changelog-files'):
        for file in files:
            if file.endswith('.md'):
                changelog_file = os.path.join(root, file)
                with open(changelog_file, encoding='utf8') as changelog:
                    changelog_lines = changelog.readlines()
                    for line in changelog_lines:
                        if line.startswith('pull-request:'):
                            link = re.search('^pull-request\:\s\"(.*)\"$', line).group(1)
                            documented.append(link)

def getAllPRs():
    cur = con.cursor()

    cur.execute('select REPOSITORY:name::string, PULL_REQUEST:number, PULL_REQUEST:title::string, PULL_REQUEST:html_url::string, TO_DATE(PULL_REQUEST:merged_at) as DATE FROM "STITCHCDW"."SINGER_GITHUB_EVENTS"."DATA" WHERE PULL_REQUEST:merged = true AND (PULL_REQUEST:base:ref = \'master\' OR PULL_REQUEST:base:ref = \'main\') AND REPOSITORY:name ILIKE \'tap-%\'')

    for (name, number, title, url, date) in cur:
        if [name, number, title, url, date] not in all_prs:
            all_prs.append([name, number, title, url, date])




def getLatestPRs():
    prs = pandas.DataFrame(all_prs, columns=['repository', 'pr_number', 'pr_title', 'pr_url', 'pr_merge_date'])

    latest = prs.loc[(prs['pr_merge_date'] < today) & (prs['pr_merge_date'] > last_week)]

    for index, row in latest.iterrows():
        
        name = row[0]
        number = row[1]
        title = row[2]
        url = row[3]
        date = row[4]

        api = 'https://api.github.com/repos/singer-io/' + name + '/pulls/' + number + '/files'

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
                        if pull in documented:
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
                                    md_filename = '../_changelog-files/drafts/' + pr_date + '-' + tap + '-' + pr_number + '.md'
                                    md_text = '---\ntitle: "' + pr_title + '"\ncontent-type: ""\ndate: ' + pr_date + '\nentry-type: \nentry-category: integration\nconnection-id: \nconnection-version: \npull-request: "' + pr_url + '"\n---'

                                    with open(md_filename, 'w') as out:
                                        out.write(md_text)

getDocumentedPRs()
getAllPRs()
getLatestPRs()