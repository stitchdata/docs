import sys, json, re, os
from format_json import replaceFormat
from get_integration_data import getIntegrationData
from get_table_data import getTableData, updateTableData
from check_table_data import checkTableData

# Get tap name, tap version, and discovery file path
tap = sys.argv[1]
tap_version = str(sys.argv[2])
if tap_version == '0':
    tap_version = '1'
discovery_file = sys.argv[3]

# Get integration ID and type from '_data/taps/integrations.yml'
integration_id = getIntegrationData(tap)[0]

# Get integration version folder
folder = '../../_data/taps/schemas/{0}/v{1}'.format(integration_id, tap_version)
json_output_folder = '{}/json'.format(folder)

schema_list = []
issue_list = []

# Open discovery file and get schemas
with open(discovery_file, 'r', encoding='utf-8') as f:
    content = json.load(f)
    streams = content['streams']
    for stream in streams:

        # Get schema name, replication method, replication keys and primary keys
        name = stream['tap_stream_id']
        schema_list.append(name)
        schema = stream['discovered_schema']
        metadata = stream['metadata'][0]['metadata']
        replication_method = metadata['forced-replication-method']

        # Format name of replication method
        if replication_method == 'INCREMENTAL':
            replication_method = 'Key-based Incremental'
        elif replication_method == 'FULL_TABLE':
            replication_method = 'Full Table'

        # Find replication keys and primary keys if there are any
        try:
            replication_keys = metadata['valid-replication-keys']
        except:
            replication_keys = []
        try:
            primary_keys = metadata['table-key-properties']
        except:
            primary_keys = []
        
        # Create dict with schema data
        data = {
                'name': name,
                'table-details': {
                    'replication-method': replication_method
                }
            }
        
        # Add primary-key(s) and replication-key(s) elements if needed
        if len(primary_keys) == 1:
            data['table-details']['primary-key'] = primary_keys[0]
        elif len(primary_keys) > 1:
            data['table-details']['primary-keys'] = sorted(primary_keys)
        if len(replication_keys) == 1:
            data['table-details']['replication-key'] = replication_keys[0]
        elif len(replication_keys) > 1:
            data['table-details']['replication-keys'] = sorted(replication_keys)

        # Use function in 'get_table_data.py' to find and update table data        
        updateTableData(integration_id, tap_version, name, data)
        
        # Use function un 'format_json.py' to replace format elements
        json_content = json.dumps(schema)
        format_pattern = re.compile('"format":\s*"[^\"]+"')
        while re.search(format_pattern, json_content):
            json_content = replaceFormat(json_content)
        
        # Write the JSON output to the schema file
        json_output = json.loads(json_content)
        filepath = '{0}/{1}.json'.format(json_output_folder, name)
        with open(filepath, 'w') as j:
            json.dump(json_output, j, indent=2, sort_keys=True)

# Use function in 'get_table_data.py' to add entry for new tables
getTableData(integration_id, tap_version, schema_list, 'catalog')

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

# Delete discovery file
os.remove(discovery_file)

