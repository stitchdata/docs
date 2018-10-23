---
tap: "netsuite"
# version: "10-15-2015"

name: "netsuite_app_definition"
doc-link: 
description: |
  The `{{ table.name }}` table contains info about the accounts in your NetSuite instance.

  {% include integrations/saas/netsuite-permission-list.html %}

replication-method: "Full Table"
primary-key: "internalId"
abstract: false

permissions:
  - name: "Integration Application"
    level: "View"
    location: "Setup"
---