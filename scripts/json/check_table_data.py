import yaml, json, os

def checkTableData(integration, version):
    # Check the tables file and the foreign keys file (if it exists) to see if all keys mentioned exist in the JSON files

    issue_list = []
    folder = '../../_data/taps/schemas/{0}/v{1}'.format(integration, version)
    tables_file = '{0}/{1}-v{2}-tables.yml'.format(folder, integration, version)
    foreign_keys_file = '{0}/{1}-v{2}-foreign-keys.yml'.format(folder, integration, version)
    json_folder = '{0}/json'.format(folder)

    issue_list = checkPrimaryReplicationKeys(tables_file, json_folder, issue_list)

    if os.path.exists(foreign_keys_file):
        issue_list = checkForeignKeys(foreign_keys_file, json_folder, issue_list)

    return issue_list

def checkPrimaryReplicationKeys(file, json_folder, issue_list):
    # Check that the primary keys and replication keys exist

    with open(file, 'r') as f:
        data = yaml.safe_load(f)

        # Iterate on each table in the tables file
        tables = data['tables']
        for table in tables:
            table_name = table['name']
            try:
                r = table['report']
                print('Table data for {} not checked'.format(table_name))
            except:

                # Get the corresponding JSON schema
                json_file = '{0}/{1}.json'.format(json_folder, table_name)

                # Get the primary key(s) and replication key(s) if they exist
                details = table['table-details']
                try:
                    primary_keys = [details['primary-key']]
                except:
                    try:
                        primary_keys = details['primary-keys']
                    except:
                        primary_keys = []
                try:
                    replication_keys = [details['replication-key']]
                except:
                    try:
                        replication_keys = details['replication-keys']
                    except:
                        replication_keys = []

                # Find properties in the JSON file
                if os.path.exists(json_file):            
                    with open(json_file, 'r', encoding='utf-8') as j:
                        json_content = json.load(j)
                        properties = json_content['properties']

                        # Look for all primary keys in the JSON file, if some are not found, append the list of issues
                        if len(primary_keys) > 0:
                            for primary_key in primary_keys:
                                try:
                                    element = properties[primary_key]
                                except:
                                    report = 'Primary Key {0} not found in {1}'.format(primary_key, json_file.replace('../../', ''))
                                    issue_list.append(report)

                        # Look for all replication keys in the JSON file, if some are not found, append the list of issues
                        if len(replication_keys) > 0:
                            for replication_key in replication_keys:

                                try:
                                    element = properties[replication_key]
                                except:
                                    report = 'Replication Key {0} not found in {1}'.format(replication_key, json_file.replace('../../', ''))
                                    issue_list.append(report)
                else:
                    report = 'JSON file {} not found'.format(json_file.replace('../../', ''))
                    if report not in issue_list:
                        issue_list.append(report)

    return issue_list

def checkForeignKeys(file, json_folder, issue_list):
    # Check that the foreign keys exist 

    with open(file, 'r') as f:
        data = yaml.safe_load(f)

        # Iterate on each table in the foreign keys file
        tables = data['tables']
        for table in tables:
            table_name = table['table-name']

            # Get the corresponding JSON schema
            json_file = '{0}/{1}.json'.format(json_folder, table_name)

            # Find properties in the JSON file
            if os.path.exists(json_file):
                with open(json_file, 'r', encoding='utf-8') as j:
                    json_content = json.load(j)
                    properties = json_content['properties']

                    # Get each table that can be joined to the current table
                    targets = table['join']
                    for target in targets:

                        # Get each pair of keys that can be used to join the tables
                        keys = target['keys']
                        for key in keys:
                            source_key = key['key']
                            
                            # Get the path to the current table's key
                            steps = source_key.split('.')
                            steps_count = len(steps)

                            # Look for the element with the key's path
                            step = 1
                            try:
                                path = properties[steps[0]]
                                if steps_count == 1:
                                    pass
                                else:

                                    # Iterate on the number of levels in the path
                                    while step < steps_count :
                                        try:
                                            path = path[steps[step]]
                                        except:
                                            try:
                                                
                                                # If the element is not found, try looking in a 'properties' element
                                                path = path['properties'][steps[step]]
                                            
                                            except:
                                                try:

                                                    # If the path element is not found in 'properties', try looking in an 'items' element
                                                    path = path['items']['properties'][steps[step]]
                                                    
                                                except:

                                                    # If the path element is not found in 'properties' or 'items', check for an 'anyOf' element
                                                    path = path['anyOf'][0]['items']['properties'][steps[step]]
                                        step +=1
                            except:
    
                                # If the path is still not found, add the key to the list of errors
                                report = 'Key {0} not found in {1}'.format(source_key, json_file.replace('../../', ''))
                                issue_list.append(report)
            else:
                report = 'JSON file {} not found'.format(json_file.replace('../../', ''))
                if report not in issue_list:
                    issue_list.append(report)

    return issue_list