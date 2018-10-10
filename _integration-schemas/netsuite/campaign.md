---
tap: "netsuite"
# version: "10-15-2015"

name: "netsuite_campaign"
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/campaign.html
description: |
  The `{{ table.name }}` table contains info about [PLACEHOLDER].

  {% include integrations/saas/netsuite-permission-list.html %}

replication-method: "Incremental"
primary-key: "internalId"
replication-key: "lastModifiedDate"

abstract: false

permissions:
  - name: "Campaign History"
    level: "Lists"
    location: "Setup"
  - name: "Marketing Campaign"
    level: "Lists"
    location: "Setup"
---