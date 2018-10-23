---
tap: "netsuite"
# version: "10-15-2015"

name: "netsuite_employee"
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/schema/search/employeesearchbasic.html?mode=package
description: |
  The `{{ table.name }}` table contains info about [PLACEHOLDER].

  {% include integrations/saas/netsuite-permission-list.html %}

replication-method: "Incremental"
primary-key: "internalId"
replication-key: "lastModifiedDate"

abstract: false

permissions:
  - name: "Employee Search"
    level: "View"
    location: "Lists"
  - name: "Employees"
    level: "View"
    location: "Lists"
---