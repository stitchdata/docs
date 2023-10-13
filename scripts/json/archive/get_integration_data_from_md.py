import yaml, os, frontmatter, re, pandas

folders = [['_database-integrations', 'database'], ['_saas-integrations', 'saas']]
schemas_with_tap = []
schemas_no_tap = []

def getSchemaData(file, type):

    parse = frontmatter.load(file)
    data = parse.metadata


    try:
        name = data['display_name']
        id = data['name']

        try:
            url = data['repo-url']
            tap = re.search('singer-io/([^/]+)', url).group(1)
            schemas_with_tap.append([name, id, type, tap, url])
        except:
            url = ''
            tap = ''
            schemas_no_tap.append([name, id, type, tap, url])  
            
    except:
        pass
        

for folder in folders:
    dir = folder[0]
    type = folder[1]
    for root, dirs, files in os.walk('../../../' + dir):
        for file in files:
            if file.endswith('.md'):
                file = os.path.join(root, file)
                getSchemaData(file, type)


df_tap = pandas.DataFrame(schemas_with_tap)
df_no_tap = pandas.DataFrame(schemas_no_tap)

new = pandas.concat([df_tap,df_no_tap]).drop_duplicates(subset=[0,1,2]).reset_index(drop=True)

integration_data = {
    'integrations': {}
}

for index, row in new.iterrows():
    name = row[0]
    id = row[1]
    type = row[2]
    tap = row[3]
    url = row[4]

    data = {
        'id': id,
        'display_name': name,
        'type': type,
        'tap': tap
    }


    integration_data['integrations'][id] = data

with open ('../../../_data/taps/integrations.yml', 'w', encoding='utf-8') as out:
    yaml.dump(integration_data, out, default_flow_style=False)

