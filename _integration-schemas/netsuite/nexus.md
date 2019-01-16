---
tap: "netsuite"
# version: "10-15-2015"

name: "netsuite_nexus"
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/nexus.html
description: |
  The `{{ table.name }}` table contains info about nexus tax items.

replication-method: "Full Table"
abstract: false

permissions:
  - name: "Tax Items"
    level: "View"
    location: "Lists"

attributes:
  - name: "internalId"
    type: "integer"
    primary-key: true
    description: |
      The record ID.

  - name: "Your Selected Fields"
    description: |
      Other fields selected by you. For a list of available attributes, refer to [{{ integration.display_name }}'s documentation]({{ table.doc-link }}){:target="new"}. **Note**: You will need to log into your {{ integration.display_name }} account to view the documentation.
---