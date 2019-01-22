---
tap: "netsuite"
# version: "10-15-2015"

name: "netsuite_budget"
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/schema/search/budgetsearchbasic.html?mode=package
description: |
  The `{{ table.name }}` table contains info about budgets.

replication-method: "Full Table"
primary-key: "internalId"
abstract: false

permissions:
  - name: "Set Up Budgets"
    level: "View"
    location: "Transactions"
  - name: "Jobs"
    level: "View"
    location: "Lists"

attributes:
  - name: "internalId"
    type: "integer"
    primary-key: true
    description: "The account ID."

  - name: "Additional fields"
    description: |
      For a list of available attributes, refer to [{{ integration.display_name }}'s documentation]({{ table.doc-link }}){:target="new"}. **Note**: You will need to log into your {{ integration.display_name }} account to view the documentation.
---