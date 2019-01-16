---
tap: "netsuite"
# version: "10-15-2015"

name: "netsuite_classification"
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/schema/search/classificationsearchbasic.html?mode=package
description: |
  The `{{ table.name }}` table contains info about classifications.

replication-method: "Full Table"
primary-key: "internalId"
abstract: false

permissions:
  - name: ""
    level: "View"
    location: "Setup"

attributes:
  - name: "internalId"
    type: "integer"
    primary-key: true
    description: "The classification ID."

  - name: "Your Selected Fields"
    description: |
      Other fields selected by you. For a list of available attributes, refer to [{{ integration.display_name }}'s documentation]({{ table.doc-link }}){:target="new"}. **Note**: You will need to log into your {{ integration.display_name }} account to view the documentation.
---