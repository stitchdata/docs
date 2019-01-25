---
tap: "netsuite"
# version: "10-15-2015"

name: "netsuite_custom_records"
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/schema/search/customerstatussearchbasic.html?mode=package
description: |
  The `{{ table.name }}` table contains info about custom records.

replication-method: "Full Table"
abstract: false

permissions:
  - name: ""
    level: "View"
    location: ""

attributes:
  - name: "internalId"
    type: "integer"
    primary-key: true
    description: |
      The {{ table.name | remove: "netsuite_" | replace: "_"," " }} ID.

  - name: "Additional fields"
    description: |
      For a list of available attributes, refer to [{{ integration.display_name }}'s documentation]({{ table.doc-link }}){:target="new"}. **Note**: You will need to log into your {{ integration.display_name }} account to view the documentation.
---