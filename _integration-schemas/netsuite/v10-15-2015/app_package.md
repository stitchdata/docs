---
tap: "netsuite"
version: "10-15-2015"

name: "netsuite_app_package"
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2015_1/schema/record/apppackage.html
description: |
  The `{{ table.name }}` table contains info about the app packages in your NetSuite instance.

replication-method: "Full Table"
primary-key: "internalId"
abstract: false

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "app-package"

attributes:
  - name: "internalId"
    type: "integer"
    primary-key: true
    description: "The app package ID."

  - name: "Additional fields"
    description: |
      For a list of available attributes, refer to [{{ integration.display_name }}'s documentation]({{ table.doc-link }}){:target="new"}. **Note**: You will need to log into your {{ integration.display_name }} account to view the documentation.
---