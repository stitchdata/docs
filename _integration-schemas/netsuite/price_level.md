---
tap: "netsuite"
# version: "10-15-2015"

name: "netsuite_price_level"
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/pricelevel.html
description: |
  The `{{ table.name }}` table contains info about [price levels.

replication-method: "Full Table"
abstract: false

permissions:
  - name: "Accounting Lists"
    level: "View"
    location: "Setup"

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