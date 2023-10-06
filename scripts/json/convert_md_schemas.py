import os, frontmatter, json, yaml

taps_no_schema = [
    "tap-amplitude",
    "tap-bing-ads",
    "tap-bronto",
    "tap-calendly",
    "tap-darkskyapi",
    "tap-db2",
    "tap-deputy",
    "tap-doubleclick-campaign-manager",
    "tap-dynamics-365",
    "tap-dynamodb",
    "tap-exchangeratesapi",
    "tap-fixerio",
    "tap-ga4",
    "tap-google-analytics",
    "tap-heap",
    "tap-intacct",
    "tap-kafka",
    "tap-mambu",
    "tap-mongodb",
    "tap-ms-dynamics",
    "tap-ms-teams",
    "tap-mysql",
    "tap-nikabot",
    "tap-oracle",
    "tap-outbrain",
    "tap-pinterest-ads",
    "tap-postgres",
    "tap-quickbase",
    "tap-redshift",
    "tap-responsys",
    "tap-revinate",
    "tap-s3-csv",
    "tap-saasoptics",
    "tap-sailthru",
    "tap-salesforce",
    "tap-selligent",
    "tap-sendgrid",
    "tap-sftp",
    "tap-taboola",
    "tap-typo",
    "tap-uservoice",
    "tap-workday-raas",
    "tap-zuora"
    ]

integrations_file = '../../_data/taps/integrations.yml'
schema_folder = '../../_integration-schemas/'

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
        tap = integrations[i]['tap']
        integration_id = integrations[i]['id']

        if tap in taps_no_schema:
            for root, dirs, files in os.walk(schema_folder + integration_id):
                for file in files:
                    if file.endswith('.md') and file != 'foreign-keys.md':
                        filepath = os.path.join(root, file)
                        parse = frontmatter.load(filepath)
                        data = parse.metadata
                        if 'version' in data:
                            print(filepath)
                            tap_version = data['version']
                            table_name = data['name']

                            filename = file.replace('.md', '.json')

                            output_file_path = '../../_data/taps/schemas/{0}/v{1}/{2}'.format(integration_id, tap_version, filename)

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