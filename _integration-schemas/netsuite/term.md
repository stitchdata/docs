---
tap: "netsuite"
# version: "10-15-2015"

name: "netsuite_term"
doc-link: https://system.netsuite.com/help/helpcenter/en_US/
description: |
  The `{{ table.name }}` table contains info about [PLACEHOLDER].

  {% include integrations/saas/netsuite-permission-list.html %}

replication-method: "Full Table"
primary-key: "internalId"
abstract: false

permissions:
  - name: "Accounting Lists"
    level: "View"
    location: "Setup"
---