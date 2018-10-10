---
tap: "netsuite"
# version: "10-15-2015"

name: "netsuite_account"
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/account.html

description: |
  The `{{ table.name }}` table contains info about the accounts in your NetSuite instance.

  {% include integrations/saas/netsuite-permission-list.html %}

replication-method: "Full Table"
primary-key: "internalId"
abstract: false

permissions:
  - name: "Accounts"
    level: "View"
    location: "Lists"
---