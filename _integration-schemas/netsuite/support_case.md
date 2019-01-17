---
tap: "netsuite"
# version: "10-15-2015"

name: "netsuite_support_case"
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/schema/search/supportcasesearchbasic.html?mode=package
description: |
  The `{{ table.name }}` table contains info about support cases.

replication-method: "Key-based Incremental"
abstract: false

permissions:
  - name: "Support Case Issue"
    level: "View"
    location: "Setup"

  - name: "Support Case Origin"
    level: "View"
    location: "Setup"

  - name: "Support Case Priority"
    level: "View"
    location: "Setup"

  - name: "Support Case Status"
    level: "View"
    location: "Setup"

  - name: "Support Case Territory"
    level: "View"
    location: "Setup"

  - name: "Support Case Territory Rule"
    level: "View"
    location: "Setup"

  - name: "Support Case Type"
    level: "View"
    location: "Setup"

attributes:
  - name: "internalId"
    type: "integer"
    primary-key: true
    description: |
      The {{ table.name | remove: "netsuite_" | replace: "_"," " }} ID.

  - name: "lastModifiedDate"
    type: "date-time"
    replication-key: true
    description: |
      The time the {{ table.name | remove: "netsuite_" | replace: "_"," " }} was last updated.

  - name: "Additional fields"
    description: |
      For a list of available attributes, refer to [{{ integration.display_name }}'s documentation]({{ table.doc-link }}){:target="new"}. **Note**: You will need to log into your {{ integration.display_name }} account to view the documentation.
---