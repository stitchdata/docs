import os, frontmatter, pandas, yaml

errors = []
file_count = 0

taps = []
tables = []

def getSchemaData(file):
    try:
        parse = frontmatter.load(file)
        data = parse.metadata

        try:
            tap = data['tap']
            version = data['version']

            tap_version = [tap, version]

            if tap_version not in taps:
                taps.append(tap_version)

            name = data['name']
            doc = data['doc-link']
            try:
                singer = data['singer-schema']
            except:
                singer = ''
            
            description = data['description']
            replication = data['replication-method']

            primary_keys = []
            replication_keys = []

            attributes = data['attributes']
            for attribute in attributes:
                attribute_name = attribute['name']
                if 'primary-key' in attribute:
                    primary_keys.append(attribute_name)
                if 'replication-key' in attribute:
                    replication_keys.append(attribute_name)
            
            data = {
                'tap': tap,
                'version': version,
                'name': name,
                'description': description,
                'links': {
                    'doc-link': doc,
                    'singer-schema': singer
                },
                'table-details': {
                    'replication-method': replication,
                    'primary-keys': primary_keys,
                    'replication-keys': replication_keys
                }
            }
            
            tables.append(data)



        except:
            pass
    except:
        errors.append(file)
    


    return errors

for root, dirs, files in os.walk('../../_integration-schemas'):
    for file in files:
        if file.endswith('.md') and file != 'foreign-keys.md':
            file_count += 1
            file = os.path.join(root, file)
            getSchemaData(file)

tables_df = pandas.DataFrame(tables)

for tap in taps:
    tap_name = tap[0]
    tap_version = tap[1]
    tap_tables = tables_df.loc[(tables_df['tap'] == tap_name) & (tables_df['version'] == tap_version)]

    tap_tables = tap_tables.drop(columns=['tap', 'version'])

    tables_dict = tap_tables.to_dict(orient='records')

    tap_dict = {
        'tap': tap_name,
        'version': tap_version,
        'schemas': tables_dict
    }


    path = 'yaml/{0}/v{1}'.format(tap_name, tap_version)
    if os.path.exists(path):
        pass
    else:
        os.makedirs(path)

    with open ('{2}/{0}-v{1}-tables.yaml'.format(tap_name, tap_version, path), 'w', encoding='utf-8') as out:

        y = yaml.dump(tap_dict, out, default_flow_style=None, sort_keys=False)
