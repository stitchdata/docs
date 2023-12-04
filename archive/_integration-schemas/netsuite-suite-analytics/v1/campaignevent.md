---
tap: "netsuite-suite-analytics"
version: "1"
key: "campaign-event"

name: "campaignevent"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/campaignevent.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "campaign_event_extid"
    type: "string"
    description: ""

  - name: "campaign_event_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "campaign-event-id"

  - name: "campaign_id"
    type: "integer"
    description: ""
    foreign-key-id: "campaign-id"

  - name: "channel_id"
    type: "integer"
    description: ""
    foreign-key-id: "campaign-channel-id"

  - name: "cost_0"
    type: "number"
    description: ""

  - name: "date_scheduled"
    type: "date-time"
    description: ""

  - name: "date_sent"
    type: "date-time"
    description: ""

  - name: "group_id"
    type: "integer"
    description: ""
    foreign-key-id: "crm-group-id"

  - name: "number_clicked_thru"
    type: "integer"
    description: ""

  - name: "number_received"
    type: "integer"
    description: ""

  - name: "number_responded"
    type: "integer"
    description: ""

  - name: "number_sent"
    type: "integer"
    description: ""

  - name: "number_unsubscribed"
    type: "integer"
    description: ""

  - name: "promotion_code_id"
    type: "integer"
    description: ""
    foreign-key-id: "promotion-code-id"

  - name: "status_id"
    type: "string"
    description: ""

  - name: "subscription_id"
    type: "integer"
    description: ""
    foreign-key-id: "campaign-subscription-id"

  - name: "template_id"
    type: "integer"
    description: ""
    foreign-key-id: "crm-template-id"

  - name: "test_cell_id"
    type: "integer"
    description: ""
    foreign-key-id: "test-cell-id"
---