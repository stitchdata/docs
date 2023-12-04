import os

integrations_folder = '../../../_data/taps/schemas'
integrations = os.listdir(integrations_folder)

empty = []

for integration in integrations:
    integration_folder = integrations_folder + '/' + integration

    versions = os.listdir(integration_folder)
    for version in versions:
        version_json_folder = integration_folder + '/' + version + '/json'
        try:
            json_files = os.listdir(version_json_folder)
        except:
            json_files = []

        if len(json_files) == 0:
            empty.append(integration + ' - ' + version)

print(*empty, sep='\n')

