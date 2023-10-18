import yaml, pandas, os

issues = []

def getFKByTable(file):
    # Takes all foreign keys listed and generates a list of join options by table

    tables = []
    table_names = []
    key_data = []

    # Get the key IDs in the foreign keys file
    with open(file, 'r') as f:
        content = yaml.safe_load(f)
        keys = content['keys']

        # For each key ID, get the tables that use it
        for key in keys:
            key_tables = keys[key]

            # For each table, get the actual name of the keys in the table, and add the table name, key ID and key in a list
            for table in key_tables:
                name = table['table']
                k = table['keys']
                for i in k:
                    data = [name, key, i]
                    if data not in key_data:
                        key_data.append(data)
                
                # Append the list of all tables mentioned in the file
                if name not in table_names:
                    table_names.append(name)

        # Create a DataFrame with all the keys mentioned
        key_df = pandas.DataFrame(key_data, columns=['table_name', 'key_id', 'table_key'])

        # Create a DataFrame with all keys in each table
        for table in table_names:
            table_keys = key_df.loc[key_df['table_name'] == table]

            # Get the list of key IDs in the table            
            table_ids = []
            for index, row in table_keys.iterrows():
                id = row['key_id']
                table_ids.append(id)
            
            # Get the list of tables that can be joined with the current table
            targets = key_df.loc[(key_df['table_name'] != table) & (key_df['key_id'].isin(table_ids))]
            target_tables = []
            for index, row in targets.iterrows():
                target_table = row['table_name']
                target_tables.append(target_table)
            
            # Create a dict with all the foreign key data for the current table
            table_data = {
                'table-name': table,
                'join': []
            }

            # For each table to join with the current table, get the keys to join them with
            for target_table in target_tables:

                target_table_data = {
                    'table-name': target_table,
                    'keys': []
                }

                # Get all key IDs in the table_ids for the current target table
                target_keys = key_df.loc[(key_df['table_name'] == target_table) & (key_df['key_id'].isin(table_ids))]
                
                # For each key ID, get the list of keys
                for index, row in target_keys.iterrows():
                    key_id = row['key_id']
                    target_key = row['table_key']

                    # Get the keys that match the current key ID
                    matching_keys = table_keys.loc[key_df['key_id'] == key_id]                 
                    for i, r in matching_keys.iterrows():
                        source_key = r['table_key']

                        key_data = {
                            'key': source_key,
                            'foreign-key': target_key
                        }

                        # Add the keys to the target table
                        if key_data not in target_table_data['keys']:
                            target_table_data['keys'].append(key_data)

                # Add the target table data to the list of tables to join               
                if target_table_data not in table_data['join']:
                    table_data['join'].append(target_table_data)
                    
            # Add the list of tables to join to the table data
            if len(table_data['join']) > 0:
                tables.append(table_data)

        # Create the 'tables' element in the YAML content        
        content['tables'] = tables

    # Write the output to the foreign-keys file
    with open(file, 'w', encoding='utf-8') as f:
        yaml.safe_dump(content, f, default_flow_style=False, sort_keys=False)

# Get and update all foreign key files, and return a list of issues
for root, dirs, files in os.walk('../../_data/taps/schemas'):
    for file in files:
        if file.endswith('-foreign-keys.yml'):
            file = os.path.join(root, file)
            try:
                getFKByTable(file)
            except:
                issues.append(file)

if len(issues) > 0:
    print(*issues, sep='\n')