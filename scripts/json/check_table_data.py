import yaml, json, os

def checkTableData(integration, version):
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

    with open(file, 'r') as f:
        data = yaml.safe_load(f)

        tables = data['tables']

        for table in tables:

            table_name = table['name']

            json_file = '{0}/{1}.json'.format(json_folder, table_name)

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

            if os.path.exists(json_file):            
                with open(json_file, 'r', encoding='utf-8') as j:
                    json_content = json.load(j)
                    properties = json_content['properties']

                    if len(primary_keys) > 0:
                        for primary_key in primary_keys:

                            try:
                                element = properties[primary_key]
                            except:
                                report = 'Primary Key {0} not found in {1}'.format(primary_key, json_file.replace('../../', ''))
                                issue_list.append(report)

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

    with open(file, 'r') as f:
        data = yaml.safe_load(f)

        tables = data['tables']

        for table in tables:

            table_name = table['table-name']

            json_file = '{0}/{1}.json'.format(json_folder, table_name)

            if os.path.exists(json_file):
                with open(json_file, 'r', encoding='utf-8') as j:
                    json_content = json.load(j)
                    properties = json_content['properties']

                    targets = table['join']
                    for target in targets:
                        keys = target['keys']
                        for key in keys:
                            source_key = key['key']
                            
                            steps = source_key.split('.')
                            steps_count = len(steps)

                            step = 1
                            try:
                                path = properties[steps[0]]
                                if steps_count == 1:
                                    pass
                                else:
                                    while step < steps_count :
                                        try:
                                            path = path[steps[step]]
                                        except:
                                            try:
                                                path = path['properties'][steps[step]]
                                            
                                            except:
                                                path = path['items']['properties'][steps[step]]
                                        step +=1
                            except:
                                report = 'Key {0} not found in {1}'.format(source_key, json_file.replace('../../', ''))
                                issue_list.append(report)
            else:
                report = 'JSON file {} not found'.format(json_file.replace('../../', ''))
                if report not in issue_list:
                    issue_list.append(report)

    return issue_list