---
tap: "netsuite-suite-analytics"
version: "1"
key: "campaign-response-history"

name: "campaignresponse"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/campaignresponsehisstory.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "author"
    type: "integer"
    description: ""
    foreign-key-id: "entity-id"

  - name: "campaign_response_id"
    type: "integer"
    description: ""
    foreign-key-id: "campaign-response-id"

  - name: "date_0"
    type: "date-time"
    description: ""

  - name: "note"
    type: "string"
    description: ""

  - name: "response_id"
    type: "string"
    description: ""

  - name: "status_detail"
    type: "string"
    description: ""

  - name: "transaction_id"
    type: "integer"
    description: ""
    foreign-key-id: "transaction-id"
---