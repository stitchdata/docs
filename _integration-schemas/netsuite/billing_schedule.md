---
tap: "netsuite"
# version: "10-15-2015"

name: "netsuite_billing_schedule"
doc-link: 
description: |
  The `{{ table.name }}` table contains info about the accounts in your NetSuite instance.

  {% include integrations/saas/netsuite-permission-list.html %}

replication-method: "Full Table"
primary-key: "internalId"
abstract: false

permissions:
  - name: "Billing Schedules"
    level: "View"
    location: "Lists"
---