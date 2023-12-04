---
tap: "netsuite-suite-analytics"
version: "1"
key: "campaign-channel"

name: "campaignchannel"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/campaignchannel.html"
description: |
  {{ integration.append-only-loading | flatify }}

replication-method: "Key-based Incremental"
loading-behavior: "Append-Only"

attributes:
  - name: "date_last_modified"
    type: "date-time"
    replication-key: true
    description: |
      The time the {{ table.key | replace: "-"," " }} was last modified.

  - name: "campaign_channel_extid"
    type: "string"
    description: ""

  - name: "campaign_channel_id"
    type: "integer"
    description: ""
    foreign-key-id: "campaign-channel-id"

  - name: "description"
    type: "string"
    description: ""

  - name: "event_type_id"
    type: "string"
    description: ""

  - name: "is_inactive"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""
---