---
tap: "netsuite"
# version: "10-15-2015"

name: "netsuite_time_sheet"
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/timesheet.html
description: |
  The `{{ table.name }}` table contains info about [PLACEHOLDER].

  {% include integrations/saas/netsuite-permission-list.html %}

replication-method: "Full Table"
primary-key: "internalId"
abstract: false

permissions:
  - name: "Track Time"
    level: "View"
    location: "Transactions"
---