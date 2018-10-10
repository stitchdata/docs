---
tap: "netsuite"
# version: "10-15-2015"

name: "netsuite_deleted"
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/schema/search/customerstatussearchbasic.html?mode=package
description: |
  The `{{ table.name }}` table contains info about [PLACEHOLDER].

  {% include integrations/saas/netsuite-permission-list.html %}

replication-method: "Incremental"
primary-key: "internalId:_type"
abstract: true

permissions:
  - name: ""
    level: "View"
    location: ""
---