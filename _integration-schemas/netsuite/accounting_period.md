---
tap: "netsuite"
# version: "10-15-2015"

name: "netsuite_accounting_period"
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/accountingperiod.html
description: |
  The `{{ table.name }}` table contains info about accounting periods in your NetSuite instance.

  {% include integrations/saas/netsuite-permission-list.html %}

replication-method: "Full Table"
primary-key: "internalId"
abstract: false

permissions:
  - name: "Manage Accounts"
    level: "View"
    location: "Setup"
---