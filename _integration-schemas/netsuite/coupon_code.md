---
tap: "netsuite"
# version: "10-15-2015"

name: "netsuite_coupon_code"
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/couponcode.html
description: |
  The `{{ table.name }}` table contains info about [PLACEHOLDER].

  {% include integrations/saas/netsuite-permission-list.html %}

replication-method: "Full Table"
primary-key: "internalId"
abstract: false

permissions:
  - name: "Promotion"
    level: "View"
    location: "Lists"
---