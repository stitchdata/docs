---
tap: "netsuite-suite-analytics"
version: "1"
key: "campaign-response"

name: "campaignresponse"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/campaignresponse.html"
description: ""

replication-method: "Full Table"
loading-behavior: "Append-Only"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "campaign_event_id"
    type: "integer"
    description: ""
    foreign-key-id: "campaign-event-id"

  - name: "campaign_response_extid"
    type: "string"
    description: ""

  - name: "campaign_response_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "campaign-response-id"

  - name: "contact_id"
    type: "integer"
    description: ""
    foreign-key-id: "contact-id"

  - name: "date_sent"
    type: "date-time"
    description: ""

  - name: "entity_id"
    type: "integer"
    description: ""
    foreign-key-id: "entity-id"

  - name: "response_id"
    type: "string"
    description: ""
---