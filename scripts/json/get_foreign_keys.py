import yaml, pandas, os

issues = []

def getFKByTable(file):

    tables = []

    table_names = []

    key_data = []

    with open(file, 'r') as f:
        content = yaml.safe_load(f)

        keys = content['keys']

        for key in keys:
            key_tables = keys[key]
            for table in key_tables:
                name = table['table']
                k = table['keys']
                for i in k:
                    data = [name, key, i]
                    if data not in key_data:
                        key_data.append(data)
                if name not in table_names:
                    table_names.append(name)

        key_df = pandas.DataFrame(key_data, columns=['table_name', 'key_id', 'table_key'])

        for table in table_names:

            target_tables = []
            table_ids = []

            table_data = {
                'table-name': table,
                'join': []
            }

            table_keys = key_df.loc[key_df['table_name'] == table]

            for index, row in table_keys.iterrows():
                id = row[1]
                table_ids.append(id)
            
            targets = key_df.loc[(key_df['table_name'] != table) & (key_df['key_id'].isin(table_ids))]
            
            for index, row in targets.iterrows():
                target_table = row[0]
                target_tables.append(target_table)

            for target_table in target_tables:

                target_table_data = {
                    'table-name': target_table,
                    'keys': []
                }

                target_keys = key_df.loc[(key_df['table_name'] == target_table) & (key_df['key_id'].isin(table_ids))]
                
                for index, row in target_keys.iterrows():
                    key_id = row[1]
                    target_key = row[2]

                    matching_keys = table_keys.loc[key_df['key_id'] == key_id]
                    
                    for i, r in matching_keys.iterrows():
                        source_key = r[2]

                        key_data = {
                            'key': source_key,
                            'foreign-key': target_key
                        }

                        if key_data not in target_table_data['keys']:

                            target_table_data['keys'].append(key_data)
                
                if target_table_data not in table_data['join']:
                
                    table_data['join'].append(target_table_data)

            tables.append(table_data)

        
        content['tables'] = tables

    with open(file, 'w', encoding='utf-8') as f:
        yaml.safe_dump(content, f, default_flow_style=False, sort_keys=False)


for root, dirs, files in os.walk('../../_data/taps/schemas'):
    for file in files:
        if file.endswith('-foreign-keys.yml'):
            file = os.path.join(root, file)
            try:
                getFKByTable(file)
            except:
                issues.append(file)

print(*issues, sep='\n')