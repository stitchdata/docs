import yaml

def getIntegrationData(repo):
    file = '../../_data/taps/integrations.yml'

    print(repo)

    with open(file, 'r') as f:
        data = yaml.safe_load(f)
        
        integrations = data['integrations']

        for i in integrations:
            tap = integrations[i]['tap']
            id = integrations[i]['id']
            type = integrations[i]['type']
            
            if tap == repo:
                integration_id = id
                print(integration_id)
                integration_type = type

    return [integration_id, integration_type]