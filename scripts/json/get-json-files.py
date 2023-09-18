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

def getTapData(setup_file):

    name_pattern = re.compile(r'name=\'([^\']+)\'')
    version_pattern = re.compile(r'version=\'([^\']+)\'')

    tap_name = re.search(name_pattern, setup_file).group(1)
    tap_version = re.search(version_pattern, setup_file).group(1)

    tap_major_version = tap_version[0]

    return [tap_name, tap_major_version]


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

    setup_file = open(tap_folder + '/setup.py').read()
    tap_data = getTapData(setup_file)

    tap_name = tap_data[0]
    tap_version = tap_data[1]

    integration_id = getIntegrationId(tap_name)

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

