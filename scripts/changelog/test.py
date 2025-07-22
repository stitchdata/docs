import yaml

integration_dict = {}

# Load YAML file
with open('../../_data/taps/integrations.yml', 'r') as file:
    yaml_data = yaml.safe_load(file)
    integration_dict.update(yaml_data['integrations'])

# # Now `data` is a Python dictionary
# print(data)

# print(integration_dict)
# print(integration_dict['zuora'])

if 'zuora' in integration_dict:
    print(integration_dict['zuora'])
else:
    print('Integration not found.')