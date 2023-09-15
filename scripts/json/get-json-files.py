import requests, re, base64, json, datetime, os, pandas, sys, zipfile, yaml
from datetime import datetime as dt
from format_json import formatJSON

# GitHub info
github_token = sys.argv[1]
host = 'https://api.github.com'
github_headers = {'Authorization': github_token}

# Get repository name
repo = sys.argv[2]
branch = sys.argv[3]

def getIntegrationId(repo):
    file = '../../_data/taps/integrations.yml'

    with open(file, 'r') as f:
        data = yaml.safe_load(f)
        
        integrations = data['integrations']

        for i in integrations:
            tap = i['tap']
            id = i['id']

            if tap == repo:
                integration_id = id
    
    return integration_id


def getTapVersion(changelog):

    changelog = str(changelog)

    version_line = re.search('##\s(v\d|\d|v\s\d)', changelog, re.MULTILINE).group(1)
    version = version_line[-1]

    return version

def getFiles(repo, branch): 

    # Get all PRs that are closed and had the default branch as base
    contents_api = host + '/repos/singer-io/' + repo + '/zipball/' + branch
    repo_contents = requests.get(contents_api, headers=github_headers)
    output_dir = '../../../'
    output_file = '{0}{1}.zip'.format(output_dir, repo)
    zip_output = output_dir + repo

    with open(output_file, 'wb') as f:
        f.write(repo_contents.content)
    
    with zipfile.ZipFile(output_file, 'r') as zip_file:
        zip_file.extractall(zip_output)
    
    tap_folder = zip_output + '/' + os.listdir(zip_output)[0]

    integration_id = getIntegrationId(repo)

    changelog = open( tap_folder + '/CHANGELOG.md').read()
    tap_version = getTapVersion(changelog)
    print(tap_version)

    json_output_folder = '../../_data/schemas/{0}/v{1}/json'.format(integration_id, tap_version)

    if os.path.exists(json_output_folder):
        pass
    else:
        os.makedirs(json_output_folder)

    for item in os.listdir(tap_folder):
        item_path = tap_folder + '/' + item

        if item.startswith('tap'):
            schemas = item_path + '/schemas'
            formatJSON(schemas, json_output_folder)
        
getFiles(repo, branch)

