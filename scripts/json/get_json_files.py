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

def getTapData(setup_file):
    # Get the name of the tap and the current version from the setup file

    name_pattern = re.compile(r'name=(\"|\')([^\'\"]+)(\'|\")')
    version_pattern = re.compile(r'version=(\"|\')([^\'\"]+)(\'|\")')

    tap_name = re.search(name_pattern, setup_file).group(2)
    tap_version = re.search(version_pattern, setup_file).group(2)

    # Extract the major version
    tap_major_version = tap_version[0]
    if tap_major_version == '0':
        tap_major_version = '1'

    return [tap_name, tap_major_version]

def getTapExceptions(tap, version):
    keep = []
    ignore = []
    
    file = 'file_exceptions.json'
    with open(file, 'r') as f:
        data = json.load(f)
        if tap in data:
            if version in data[tap]:
                exceptions = data[tap][version]
                if 'keep' in exceptions:
                    keep = exceptions['keep']
                
                if 'ignore' in exceptions:
                    ignore = exceptions['ignore']
    
    return keep, ignore

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

            # Get list of files with exceptions (if any)
            exceptions = getTapExceptions(tap_name, tap_version)
            keep = exceptions[0]
            ignore = exceptions[1]
            
            # Create JSON folder if it doesn't exist
            if os.path.exists(json_output_folder):
                pass
            else:
                os.makedirs(json_output_folder)

            # Get schema folder and use the function in format_json.py to format the files and get the list of schemas
            for item in os.listdir(tap_folder):
                item_path = tap_folder + '/' + item

                if item.startswith('tap') and os.path.isdir(item_path):
                    if tap_name == 'tap-mambu':
                        schemas = item_path + '/helpers/schemas'
                    else:
                        schemas = item_path + '/schemas'
                        
                    schema_list = formatJSON(schemas, json_output_folder, keep)
                    issue_list = []
                    updated_schema_list = []
                    
                    # Remove files for schemas to ignore
                    for schema in schema_list:
                        schema_file = schema + '.json'
                        if schema_file in ignore:
                            os.remove('{0}/{1}'.format(json_output_folder, schema_file))
                            print('JSON file {} ignored'.format(schema_file))
                        else:
                            updated_schema_list.append(schema)

                    # Use function from 'get_table_data.py' to get and update the yaml file with table details
                    getTableData(integration_id, tap_version, updated_schema_list, 'tap')

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

                    # If no issues found but issues file exists, remove issues file
                    else:
                        if os.path.exists(issues_file):
                            os.remove(issues_file)
                        print('No issues found')

                        
        
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

if branch == '':
    print('Fetching schemas from the main/master branch of the {} repository'.format(repo))
else:
    print('Fetching schemas from the {0} branch of the {1} repository'.format(branch, repo))

getFiles(repo, branch)