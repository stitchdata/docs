---
tap: "netsuite-suite-analytics"
version: "1"
key: "campaign-item"

name: "campaignitem"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/campaignitem.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "campaign_id"
    type: "integer"
    description: ""
    foreign-key-id: "campaign-id"

  - name: "item_id"
    type: "integer"
    description: ""
    foreign-key-id: "item-id"
---