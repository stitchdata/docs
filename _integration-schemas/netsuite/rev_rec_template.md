---
tap: "netsuite"
# version: "10-15-2015"

name: "netsuite_rev_rec_template"
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/revrectemplate.html
description: |
  The `{{ table.name }}` table contains info about [PLACEHOLDER].

  {% include integrations/saas/netsuite-permission-list.html %}

replication-method: "Full Table"
primary-key: "internalId"
abstract: false

permissions:
  - name: "Revenue Recognition Schedules"
    level: "View"
    location: "Lists"
---