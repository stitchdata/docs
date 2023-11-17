import os, yaml

def compareTableData(existing, new):
    # Compare and merge existing table details with table details from the catalog file

    updated = existing
    existing_details = existing['table-details']
    new_details = new['table-details']
    updated_details = updated['table-details']

    if existing_details == new_details:
        pass
    else:

        # If the existing and new details are different check each element
        for element in new_details:
            if element in existing_details:

                # Check if the element in the new details is already in the existing details
                existing_element = existing_details[element]
                new_element = new_details[element]

                # If the value of the element is different, keep the newest value
                if existing_element == new_element:
                    pass
                else: 
                    updated_details[element] = new_element
            else:

                # If the element isn't in the existing details: 
                # - deduplicate replication-key(s) and primary-key(s) elements
                # - add the element to the table details
                if element == 'replication-key' and 'replication-keys' in existing_details:
                    updated_details['replication-key'] = new_details['replication-key']
                    updated_details.pop('replication-keys')
                elif element == 'replication-keys' and 'replication-key' in existing_details:
                    updated_details['replication-keys'] = new_details['replication-keys']
                    updated_details.pop('replication-key')
                elif element == 'primary-key' and 'primary-keys' in existing_details:
                    updated_details['primary-key'] = new_details['primary-key']
                    updated_details.pop('primary-keys')
                elif element == 'primary-keys' and 'primary-key' in existing_details:
                    updated_details['primary-keys'] = new_details['primary-keys']
                    updated_details.pop('primary-key')
                else:
                    updated_details[element] = new_details[element]

    return updated

def updateTableData(integration, version, name, data):
    # Update table details from catalog file

    # Get current table data
    folder = '../../_data/taps/schemas/{0}/v{1}'.format(integration, version)
    file = '{2}/{0}-v{1}-tables.yml'.format(integration, version, folder)
    existing_tables = []

    if os.path.exists(file):
        with open(file, 'r') as f:

            # Get list of existing tables
            existing_data = yaml.safe_load(f)
            tables = existing_data['tables']

            # Look for the current table in the existing tables and compare the existing and new table details
            for table in tables:
                table_name = table['name']
                existing_tables.append(table_name)
                if table_name == name:
                    table = compareTableData(table, data)
            
            # Add data for new tables
            if name not in existing_tables:
                table = {
                    'name': name,
                    'table-details': {}
                }
                table = compareTableData(table, data)
                tables.append(table)

    # Write the updated table data to the YAML file
    with open (file, 'w', encoding='utf-8') as out:
        yaml.dump(existing_data, out, default_flow_style=False, sort_keys=False)    

                
def getTableData(integration, version, schema_list, import_type):
    # Get table data for JSON schemas

    table_list = []
    not_found = []
    new = []
    
    folder = '../../_data/taps/schemas/{0}/v{1}'.format(integration, version)
    file = '{2}/{0}-v{1}-tables.yml'.format(integration, version, folder)

    # Get the list of existing tables
    if os.path.exists(file):
        with open(file, 'r') as f:
            data = yaml.safe_load(f)

            # Check if the integration has a tap-repo-schema value, otherwise set it to true by default
            if 'tap-repo-schemas' in data:
                pass
            else:
                data['tap-repo-schemas'] = True
            
            tap_schemas = data['tap-repo-schemas']

            tables = data['tables']

            for table in tables:
                table_name = table['name']
                table_list.append(table_name)

    # If the tables YAML file doesn't exist, create it
    else:
        if os.path.exists(folder):
            pass
        else:
            os.makedirs(folder)

        data = {
            'tap': integration,
            'version': version,
            'tap-repo-schemas': True,
            'tables': []
        }

    # For JSON schema found, check if the table is in the list of existing tables
    for table in schema_list:

        # Add the table if it doesn't exist
        if table not in table_list:
            new.append(table)
            table_data = {
                'name': table,
                'description': '',
                'links': {
                    'doc-link': '',
                    'singer-schema': '',
                    'api-method': ''
                },
                'table-details': {
                    'replication-method': '',
                    'primary-key': '',
                    'replication-key': ''
                }
            }
            data['tables'].append(table_data)

    # For each table in the list of existing tables, check if the JSON schema exists
    for table in table_list:

        # If the schema doesn't exist, mark the table as 'not found', it will hide it from the docs but the table data will still exist in the YAML file
        if table not in schema_list and tap_schemas != False and import_type == 'tap':
            status = 'not_found'
            for t in data['tables']:
                if t['name'] == table:
                    try:
                        r = t['report']
                    except:
                        try:
                            s = t['tap-repo-schema']
                        except:
                            t['status'] = status
                            not_found.append(table)
        else:

            # If the schema exists and the table has the 'not found' status, remove it the status 
            for t in data['tables']:
                if t['name'] == table: 
                    try:
                        t.pop('status')
                    except:
                        pass

    # Write the updated data to the YAML file
    with open (file, 'w', encoding='utf-8') as out:
        yaml.dump(data, out, default_flow_style=False, sort_keys=False)

    # Report new tables and schemas not found
    if len(new) > 0:
        print('The following tables have been added to {}:'.format(file.replace('../../', '')))
        print(*new, sep='\n')

    if len(not_found) > 0:
        print('The following tables exist in {} but were not found in the repository:'.format(file.replace('../../', '')))
        print(*not_found, sep='\n')