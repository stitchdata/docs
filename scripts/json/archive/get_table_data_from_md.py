import os, frontmatter, pandas, yaml, sys

errors = []
file_count = 0

taps = []
tables = []

folder = '../../../_integration-schemas'

try:
    integration = sys.argv[1]
    folder = folder + '/' + integration
except:
    pass

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
            
            description = data['description']
            replication = data['replication-method']

            parents = []

            try:
                parent = data['dependent-on']
                parent_list = parent.split('|')
                for p in parent_list:
                    parents.append(p)

            except:
                try:
                    parent = data['dependent-table-key']
                    parents.append(parent)
                except:
                    pass
            
            primary_keys = []
            replication_keys = []

            attributes = data['attributes']
            for attribute in attributes:
                attribute_name = attribute['name']
                if 'primary-key' in attribute:
                    primary_keys.append(attribute_name)
                if 'replication-key' in attribute:
                    replication_keys.append(attribute_name)
                    
            
            output_data = {
                'tap': tap,
                'version': version,
                'name': name,
                'description': description,
                'links': {
                },
                'table-details': {
                    'replication-method': replication
                }
            }

            try:
                doc = data['doc-link']
                output_data['links']['doc-link'] = doc
            except:
                pass
            try:
                singer = data['singer-schema']
                output_data['links']['singer-schema'] = singer
            except:
                pass

            try:
                api = data['api-method']
                api_link = api['doc-link']
                output_data['links']['api-method'] = api_link
            except:
                pass

            try:
                loading = data['loading-behavior']
                output_data['table-details']['loading-behavior'] = loading
            except:
                pass

            if (len(primary_keys)) == 1:
                output_data['table-details']['primary-key'] = primary_keys[0]
            elif (len(primary_keys)) > 1:
                output_data['table-details']['primary-keys'] = sorted(primary_keys)
            
            if (len(replication_keys)) == 1:
                output_data['table-details']['replication-key'] = replication_keys[0]
            elif (len(replication_keys)) > 1:
                output_data['table-details']['replication-keys'] = sorted(replication_keys)

            if (len(parents)) == 1:
                output_data['table-details']['parent-table'] = parents[0]
            elif (len(parents)) > 1:
                output_data['table-details']['parent-tables'] = sorted(parents)
            
            tables.append(output_data)



        except:
            pass
    except:
        errors.append(file)
    


    return errors

for root, dirs, files in os.walk(folder):
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
        'tables': tables_dict
    }


    path = '../../../_data/taps/schemas/{0}/v{1}'.format(tap_name, tap_version)
    if os.path.exists(path):
        pass
    else:
        os.makedirs(path)

    with open ('{2}/{0}-v{1}-tables.yml'.format(tap_name, tap_version, path), 'w', encoding='utf-8') as out:

        y = yaml.safe_dump(tap_dict, out, default_flow_style=False, sort_keys=False)
