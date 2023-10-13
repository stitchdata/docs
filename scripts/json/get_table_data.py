import os, yaml

def compareTableData(existing, new):
    existing_details = existing['table-details']
    new_details = new['table-details']

    updated = existing
    updated_details = updated['table-details']

    if existing_details == new_details:
        pass
    else:
        for element in new_details:
            if element in existing_details:
                existing_element = existing_details[element]
                new_element = new_details[element]

                if type(existing_element) == list:
                    existing_element = sorted(existing_element)

                if existing_element == new_element:
                    pass
                else: 
                    updated_details[element] = new_element
            else:
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

    new = []
    
    folder = '../../_data/taps/schemas/{0}/v{1}'.format(integration, version)
    file = '{2}/{0}-v{1}-tables.yml'.format(integration, version, folder)

    existing_tables = []

    if os.path.exists(file):
        with open(file, 'r') as f:
            existing_data = yaml.safe_load(f)

            tables = existing_data['tables']

            for table in tables:
                table_name = table['name']
                existing_tables.append(table_name)

                if table_name == name:
                    print(table_name)
                    table = compareTableData(table, data)
            
            if name not in existing_tables:
                new.append(name)

                table = {
                    'name': name,
                    'table-details': {}
                }
                table = compareTableData(table, data)
                tables.append(table)

    with open (file, 'w', encoding='utf-8') as out:
        yaml.dump(existing_data, out, default_flow_style=False, sort_keys=False)    

                
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
                    'doc-link': '',
                    'api-method': ''
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
        else:
            for t in data['tables']:
                if t['name'] == table: 
                    try:
                        t.pop('status')
                    except:
                        pass

    with open (file, 'w', encoding='utf-8') as out:
        yaml.dump(data, out, default_flow_style=False, sort_keys=False)

    if len(new) > 0:
        print('The following tables have been added to {}:'.format(file.replace('../../', '')))
        print(*new, sep='\n')

    if len(not_found) > 0:
        print('The following tables exist in {} but were not found in the repository:'.format(file.replace('../../', '')))
        print(*not_found, sep='\n')