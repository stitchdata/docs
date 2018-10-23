---
tap: "netsuite"
# version: "10-15-2015"

name: "netsuite_support_case"
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/schema/search/supportcasesearchbasic.html?mode=package
description: |
  The `{{ table.name }}` table contains info about [PLACEHOLDER].

  {% include integrations/saas/netsuite-permission-list.html %}

replication-method: "Incremental"
primary-key: "internalId"
replication-key: "lastModifiedDate"

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
---