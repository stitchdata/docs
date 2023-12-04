import os, frontmatter, yaml, pandas

issues = []

def convertForeignKeys(file):

    parse = frontmatter.load(file)
    data = parse.metadata

    integration = data['tap-reference']
    version = data['version']

    key_list = data['foreign-keys']

    output_data = {
        'tap': integration,
        'version': version,
        'keys': {}
    }

    for key in key_list:    

        source_key = key['attribute']

        try:
            table = key['table']
            
            id = table + '_' + source_key
        except:
            id = source_key

        output_data['keys'][id] = []

        foreign_keys_list = []
        target_tables = []

        foreign_keys = key['all-foreign-keys']

        for join in foreign_keys:
            target_table = join['table']

            if target_table not in target_tables:
                target_tables.append(target_table)
            try:
                path = join['subattribute']
                try:
                    element = join['join-on']
                except:
                    element = source_key

                foreign_key = path + '.' + element
            except:
                try:
                    path = join['subtable']
                    path = path.replace('__', '.')
                    try:
                        element = join['join-on']  
                    except:
                        element = source_key

                    foreign_key = path + '.' + element
                except:
                    try:
                        foreign_key = join['join-on']
                    except:
                        foreign_key = source_key

            foreign_keys_list.append([target_table, foreign_key])

        df = pandas.DataFrame(foreign_keys_list)

        for target_table in target_tables:
            keys = []
            targets = df.loc[df[0] == target_table]
            for index, row in targets.iterrows():
                target_key = row[1]
                keys.append(target_key)

            target_table_data = {
                'table': target_table,
                'keys': keys
            }

            if target_table_data not in output_data['keys'][id]:

                output_data['keys'][id].append(target_table_data)

    with open ('../../../_data/taps/schemas/{0}/v{1}/{0}-v{1}-foreign-keys.yml'.format(integration, version), 'w', encoding='utf-8') as out:

        y = yaml.safe_dump(output_data, out, default_flow_style=False, sort_keys=False)


for root, dirs, files in os.walk('../../../_integration-schemas'):
    for file in files:
        if file == 'foreign-keys.md':
            file = os.path.join(root, file)
            try:
                convertForeignKeys(file)
            except:
                issues.append(file.replace('../../../_integration-schemas\\', '').replace('\\', '-').replace('-foreign-keys.md', ''))

print(*issues, sep='\n')