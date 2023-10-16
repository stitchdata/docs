import requests, re, json, os, sys, zipfile, yaml, shutil
from format_json import formatJSON
from check_table_data import checkTableData
from get_integration_data import getIntegrationData
from get_table_data import getTableData

# GitHub info
github_token = sys.argv[1]
host = 'https://api.github.com'
github_headers = {'Authorization': github_token}

# Get repository name
repo = sys.argv[2]

# Get branch if specified
try:
    branch = sys.argv[3]
except:
    branch = ''

def getTags(repo):
    # To be removed

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

def getTapData(setup_file):
    # Get the name of the tap and the current version from the setup file

    name_pattern = re.compile(r'name=(\"|\')([^\'\"]+)(\'|\")')
    version_pattern = re.compile(r'version=(\"|\')([^\'\"]+)(\'|\")')

    tap_name = re.search(name_pattern, setup_file).group(2)
    tap_version = re.search(version_pattern, setup_file).group(2)

    # Extract the major version
    tap_major_version = tap_version[0]

    return [tap_name, tap_major_version]

def getFiles(repo, branch):
    # Get all files from the selected tap

    # Download zip file with contents of the repo (from specific branch if specified)
    contents_api = host + '/repos/singer-io/' + repo + '/zipball'
    if branch != '' and branch != 'all':
        contents_api = contents_api + '/' + branch
    repo_contents = requests.get(contents_api, headers=github_headers)

    # Stop process in case of API issue
    status_code = repo_contents.status_code
    if status_code != 200:
        sys.exit('API issue\n Status: {}\nMessage:'.format(status_code, repo_contents.content))
    else:
        # Save, unzip, and delete file
        output_dir = '../../../'
        output_file = '{0}{1}.zip'.format(output_dir, repo)
        zip_output = output_dir + repo
        with open(output_file, 'wb') as f:
            f.write(repo_contents.content)
        with zipfile.ZipFile(output_file, 'r') as zip_file:
            zip_file.extractall(zip_output)
        os.remove(output_file)

        # Open tap folder, find setup file and extract tap name and version        
        tap_folder = zip_output + '/' + os.listdir(zip_output)[0]
        setup_file = open(tap_folder + '/setup.py').read()
        tap_data = getTapData(setup_file)
        tap_name = tap_data[0]
        tap_version = tap_data[1]

        # Get integration ID and type from '_data/taps/integrations.yml'
        integration_data = getIntegrationData(tap_name)
        integration_id = integration_data[0]
        integration_type = integration_data[1]

        # Get integration version folder
        folder = '../../_data/taps/schemas/{0}/v{1}'.format(integration_id, tap_version)
        json_output_folder = '{}/json'.format(folder)

        # Ignore integrations with type 'database' since they don't have pre-defined schemas
        if integration_type != 'database':

            # Get list of files to ignore (if any)
            ignore= []
            ignore_file = '{0}/{1}-v{2}-to-ignore.yml'.format(folder, integration_id, tap_version)
            if os.path.exists(ignore_file):
                with open(ignore_file, 'r', encoding='utf-8') as i:
                    to_ignore = yaml.safe_load(i)
                    ignore = to_ignore['schemas']
            
            # Create JSON folder if it doesn't exist
            if os.path.exists(json_output_folder):
                pass
            else:
                os.makedirs(json_output_folder)

            # Get schema folder and use the function in format_json.py to format the files and get the list of schemas
            for item in os.listdir(tap_folder):
                item_path = tap_folder + '/' + item

                if item.startswith('tap'):
                    schemas = item_path + '/schemas'
                    format_results = formatJSON(schemas, json_output_folder)

                    schema_list = format_results[0]
                    issue_list = format_results[1]
                    
                    # Remove files for schemas to ignore
                    for schema in schema_list:
                        if schema in ignore:
                            schema_list.remove(schema)
                            os.remove('{0}/{1}.json'.format(json_output_folder, schema))
                            issue_list.append('JSON file {}.json ignored'.format(schema))

                    # Use function from 'get_table_data.py' to get and update the yaml file with table details
                    getTableData(integration_id, tap_version, schema_list)

                    # Use function from 'check_table_data.py' to check that the primary keys, replication keys and foreign keys listed are found in the schemas
                    table_issues = checkTableData(integration_id, tap_version)
                    if len(table_issues) > 0:
                        for issue in table_issues:
                            if issue not in issue_list:
                                issue_list.append(issue)

                    # Write all issues found to a text file
                    issues_file = '{0}/{1}-v{2}-issues.txt'.format(folder, integration_id, tap_version)
                    issues_count = len(issue_list)

                    if issues_count > 0:
                        with open(issues_file, 'w', encoding='utf-8') as f:
                            f.writelines([string + '\n' for string in issue_list])

                        print('{0} issues found, check {1} for details.'.format(issues_count, issues_file.replace('../../', '')))
        
        else:
            print('Ignoring database integration {}'.format(integration_id))

        # Delete tap folder        
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
    # To remove
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

if repo == 'all':
    if branch == '':
        print('Fetching schemas from the main/master branch of all tap repositories listed in _data/taps/integrations.yml')
    elif branch == 'all':
        print('Fetching schemas from each major version of all tap repositories listed in _data/taps/integrations.yml')
    
    getAllTaps(branch)

else:
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