---
tap: "netsuite"
# version: "10-15-2015"

name: "netsuite_customer_category"
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/customercategory.html
description: |
  The `{{ table.name }}` table contains info about [PLACEHOLDER].

  {% include integrations/saas/netsuite-permission-list.html %}

replication-method: "Incremental"
primary-key: "internalId"
abstract: false

permissions:
  - name: "Accounting Lists"
    level: "View"
    location: "Setup"
---