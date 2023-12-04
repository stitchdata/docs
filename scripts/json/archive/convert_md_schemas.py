import os, frontmatter, json, yaml, sys

integrations_file = '../../../_data/taps/integrations.yml'
schema_folder = '../../../_integration-schemas/'

try:
    integration = sys.argv[1]
except:
    integration = ''


def formatProperties(properties):
    json_out = {}
    for prop in properties:
        name = prop['name']
        if 'type' in prop:
            type = prop['type']
            if type != None:
                if ',' in type:
                    type = type.split(',')
                else:
                    type = [type]
                
                json_out[name] = {
                    'type': type
                }
                if 'subattributes' in prop:
                    attributes = prop['subattributes']
                    json_out[name]['properties'] = formatProperties(attributes)
    return json_out

with open(integrations_file, 'r') as f:
    data = yaml.safe_load(f)
    
    integrations = data['integrations']
    for i in integrations:
        if integration != '':
            if i == integration:
                tap = integrations[i]['tap']
                integration_id = integrations[i]['id']
                for root, dirs, files in os.walk(schema_folder + integration_id):
                    for file in files:
                        if file.endswith('.md') and file != 'foreign-keys.md':
                            filepath = os.path.join(root, file)
                            print(filepath)
                            # try:
                            parse = frontmatter.load(filepath)
                            data = parse.metadata
                            if 'version' in data:
                                tap_version = data['version']
                                table_name = data['name']

                                filename = file.replace('.md', '.json')

                                output_dir = '../../../_data/taps/schemas/{0}/v{1}/json'.format(integration_id, tap_version)

                                if os.path.exists(output_dir):
                                    pass
                                else:
                                    os.makedirs(output_dir)

                                output_file_path = '{0}/{1}'.format(output_dir, filename)

                                properties = data['attributes']

                                json_out = {
                                    'properties': {}
                                }

                                for prop in properties:
                                    name = prop['name']
                                    
                                    if 'type' in prop:
                                        type = prop['type']
                                        if type != None and type != '':
                                            

                                            if ',' in type:
                                                type = type.split(',')
                                            else:
                                                type = [type]
                                            
                                            json_out['properties'][name] = {
                                                'type': type
                                            }

                                            if 'subattributes' in prop:
                                                attributes = prop['subattributes']
                                                json_out['properties'][name]['properties'] = formatProperties(attributes)
                            
                                with open(output_file_path, 'w') as out:
                                    json.dump(json_out, out, indent=2, sort_keys=True)
                            # except:
                            #     print(filepath)