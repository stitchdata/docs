import requests, re, base64, json, datetime, os, pandas, sys, zipfile, yaml
from datetime import datetime as dt
from format_json import formatJSON

# GitHub info
github_token = sys.argv[1]
host = 'https://api.github.com'
github_headers = {'Authorization': github_token}

# Get repository name
repo = sys.argv[2]

try:
    branch = sys.argv[3]
except:
    branch = ''

def getTableData(integration, version, schema_list):

    table_list = []
    not_found = []

    new = []

    
    folder = '../../_data/schemas/{0}/v{1}'.format(integration, version)
    file = '{2}/{0}-v{1}-tables.yml'.format(integration, version, folder)

    if os.path.exists(file):
        with open(file, 'r') as f:
            data = yaml.safe_load(f)

            tables = data['tables']

            for table in tables:
                table_name = table['name']
                table_list.append(table_name)
    else:
        if os.path.exists(folder):
            pass
        else:
            os.makedirs(folder)

        data = {
            'tap': integration,
            'version': version,
            'tables': []
        }

    for table in schema_list:
        if table not in table_list:

            new.append(table)

            table_data = {
                'name': table,
                'description': '',
                'links': {
                    'singer-schema': '',
                    'doc-link': ''
                },
                'table-details': {
                    'replication-method': '',
                    'primary-key': '',
                    'replication-key': ''
                }
            }

            data['tables'].append(table_data)

    
    for table in table_list:
        if table not in schema_list:
            status = 'not_found'
            for t in data['tables']:
                if t['name'] == table:
                    t['status'] = status
                    not_found.append(table)

    with open (file, 'w', encoding='utf-8') as out:
        yaml.dump(data, out, default_flow_style=False, sort_keys=False)


    if len(new) > 0:
        print('The following tables have been added to {}:'.format(file.replace('../../', '')))
        print(*new, sep='\n')

    if len(not_found) > 0:
        print('The following tables exist in {} but were not found in the repository:'.format(file.replace('../../', '')))
        print(*not_found, sep='\n')

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
            tap = integrations[i]['tap']
            id = integrations[i]['id']

            if tap == repo:
                integration_id = id

    return integration_id

def getFiles(repo, branch):

    # Get all PRs that are closed and had the default branch as base
    contents_api = host + '/repos/singer-io/' + repo + '/zipball'

    if branch != '':
        contents_api = contents_api + '/' + branch

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
            schema_list = formatJSON(schemas, json_output_folder)

            getTableData(integration_id, tap_version, schema_list)

def getAllTaps():
    issues = []

    file = '../../_data/taps/integrations.yml'

    with open(file, 'r') as f:
        data = yaml.safe_load(f)
        
        integrations = data['integrations']
        for i in integrations:
            tap = integrations[i]['tap']

            if tap != '':
                try:
                    print(tap)
                    getFiles(tap, branch)
                except:
                    issues.append(tap)

    print('Issues were found in the following repositories:')
    print(*issues, spe='\n')

if repo == 'all':
    print('Fetching schemas from all tap repositories listed in _data/taps/integrations.yml')
    getAllTaps()
else:
    if branch == '':
        print('Fetching schemas from the main/master branch of the {} repository'.format(repo))
    else:
        print('Fetching schemas from the {0} branch of the {1} repository'.format(branch, repo))

    getFiles(repo, branch)