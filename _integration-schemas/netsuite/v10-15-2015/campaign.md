---
tap: "netsuite"
version: "10-15-2015"

name: "netsuite_campaign"
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/script/record/campaign.html
description: |
  The `{{ table.name }}` table contains info about campaigns.

replication-method: "Key-based Incremental"
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

attributes:
  - name: "internalId"
    type: "integer"
    primary-key: true
    description: "The campaign ID."

  - name: "lastModifiedDate"
    type: "date-time"
    replication-key: true
    description: "The time the campaign was last updated."

  - name: "Additional fields"
    description: |
      For a list of available attributes, refer to [{{ integration.display_name }}'s documentation]({{ table.doc-link }}){:target="new"}. **Note**: You will need to log into your {{ integration.display_name }} account to view the documentation.
---