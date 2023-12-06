import yaml

def getIntegrationData(repo):
    # From a tap repo name, get the integration ID and type

    file = '../../_data/taps/integrations.yml'
    with open(file, 'r') as f:
        data = yaml.safe_load(f)
        
        # Get the list of integrations from the file
        integrations = data['integrations']

        # Get and return the ID and type
        for i in integrations:
            tap = integrations[i]['tap']
            id = integrations[i]['id']
            type = integrations[i]['type']
            
            if tap == repo:
                integration_id = id
                integration_type = type

    return [integration_id, integration_type]