import requests, re, base64, json, datetime, os, pandas, sys, zipfile, yaml, shutil
from datetime import datetime as dt
from format_json import formatJSON

# GitHub info
github_token = sys.argv[1]
host = 'https://api.github.com'
github_headers = {'Authorization': github_token}

# Get repository name
repos = sys.argv[2].split(',')

try:
    branch = sys.argv[3]
except:
    branch = ''

def getTags(repo):

    major_versions = []
    version_tags = []

    tags_api = host + '/repos/singer-io/' + repo + '/tags'
    tags = json.loads(requests.get(tags_api, headers=github_headers).content)

    for tag in tags:
        name = tag['name']
        version = name.replace('v', '')
        major_version = version[0]
        
        if major_version not in major_versions:
            if major_version == '0' and len(major_versions) > 0:
                pass
            else:
                major_versions.append(major_version)
                version_tags.append(name)
    
    return version_tags

def getTableData(integration, version, schema_list):

    table_list = []
    not_found = []

    new = []

    
    folder = '../../_data/taps/schemas/{0}/v{1}'.format(integration, version)
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

    name_pattern = re.compile(r'name=(\"|\')([^\'\"]+)(\'|\")')
    version_pattern = re.compile(r'version=(\"|\')([^\'\"]+)(\'|\")')

    tap_name = re.search(name_pattern, setup_file).group(2)
    tap_version = re.search(version_pattern, setup_file).group(2)

    tap_major_version = tap_version[0]

    return [tap_name, tap_major_version]

def getIntegrationData(repo):
    file = '../../_data/taps/integrations.yml'

    with open(file, 'r') as f:
        data = yaml.safe_load(f)
        
        integrations = data['integrations']

        for i in integrations:
            tap = integrations[i]['tap']
            id = integrations[i]['id']
            type = integrations[i]['type']
            
            if tap == repo:
                integration_id = id
                integration_type = type

    return [integration_id, integration_type]

def getFiles(repo, branch):

    # Get all PRs that are closed and had the default branch as base
    contents_api = host + '/repos/singer-io/' + repo + '/zipball'

    if branch != '' and branch != 'all':
        contents_api = contents_api + '/' + branch

    repo_contents = requests.get(contents_api, headers=github_headers)
    output_dir = '../../../'
    output_file = '{0}{1}.zip'.format(output_dir, repo)
    zip_output = output_dir + repo

    with open(output_file, 'wb') as f:
        f.write(repo_contents.content)
    
    with zipfile.ZipFile(output_file, 'r') as zip_file:
        zip_file.extractall(zip_output)
    
    os.remove(output_file)
    
    tap_folder = zip_output + '/' + os.listdir(zip_output)[0]

    setup_file = open(tap_folder + '/setup.py').read()
    tap_data = getTapData(setup_file)

    tap_name = tap_data[0]
    tap_version = tap_data[1]

    integration_data = getIntegrationData(tap_name)
    integration_id = integration_data[0]
    integration_type = integration_data[1]

    if integration_type != 'database':

        json_output_folder = '../../_data/taps/schemas/{0}/v{1}/json'.format(integration_id, tap_version)

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
    
    else:
        print('Ignoring database integration {}'.format(integration_id))
    
    shutil.rmtree(zip_output)


def getIntegrationVersions(integration):

    # To remove before going to prod

    integration_path = '../../_integration-schemas/' + integration
    integration_versions = []

    if os.path.exists(integration_path):

        for item in os.listdir(integration_path):
            item_path = integration_path + '/' + item
            if os.path.isdir(item_path):
                integration_versions.append(item)
    
    else:
        print('{} not found'.format(integration_path))
    return len(integration_versions)

def getAllTaps(branch):
    issues = []

    file = '../../_data/taps/integrations.yml'

    with open(file, 'r') as f:
        data = yaml.safe_load(f)
        
        integrations = data['integrations']
        for i in integrations:
            tap = integrations[i]['tap']
            id = integrations[i]['id']

            version_count = getIntegrationVersions(id)

            if tap != '':
                try:
                    if branch == 'all' and version_count > 1:
                        tags = getTags(tap)
                        for tag in tags:
                            getFiles(tap, tag)
                    elif branch == 'all' and version_count <= 1:
                        getFiles(tap, '')
                    else:
                        getFiles(tap, branch)
                except:
                    issues.append(tap)

    print('Issues were found in the following repositories:')
    print(*issues, sep='\n')

if repos[0] == 'all':
    if branch == '':
        print('Fetching schemas from the main/master branch of all tap repositories listed in _data/taps/integrations.yml')
    elif branch == 'all':
        print('Fetching schemas from each major version of all tap repositories listed in _data/taps/integrations.yml')
    
    getAllTaps(branch)

else:
    for repo in repos:
        if branch == 'all':
            print('Fetching schemas from each major version of the {} repository'.format(repo))
            tags = getTags(repo)
            for tag in tags:
                getFiles(repo, tag)
        else:
            if branch == '':
                print('Fetching schemas from the main/master branch of the {} repository'.format(repo))
            else:
                print('Fetching schemas from the {0} branch of the {1} repository'.format(branch, repo))

            getFiles(repo, branch)