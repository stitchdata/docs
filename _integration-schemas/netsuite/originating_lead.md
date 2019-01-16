---
tap: "netsuite"
# version: "10-15-2015"

name: "netsuite_originating_lead"
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/schema/search/originatingleadsearchbasic.html?mode=package
description: |
  The `{{ table.name }}` table contains info about originating leads.

replication-method: "Key-based Incremental"
abstract: true

permissions:
  - name: "Customers"
    level: "View"
    location: "Lists"

attributes:
  - name: "internalId"
    type: "integer"
    primary-key: true
    description: |
      The {{ table.name | remove: "netsuite_" | replace: "_"," " }} ID.

  - name: "type"
    type: "string"
    description: |
      The {{ table.name | remove: "netsuite_" | replace: "_"," " }} type.

  - name: "lastModifiedDate"
    type: "date-time"
    replication-key: true
    description: |
      The time the {{ table.name | remove: "netsuite_" | replace: "_"," " }} was last updated.

  - name: "Your Selected Fields"
    description: |
      Other fields selected by you. For a list of available attributes, refer to [{{ integration.display_name }}'s documentation]({{ table.doc-link }}){:target="new"}. **Note**: You will need to log into your {{ integration.display_name }} account to view the documentation.
---