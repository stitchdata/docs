---
tap: "netsuite-suite-analytics"
version: "1"
key: "mfg-routing"

name: "mfg_routing"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/mfg_routing.html"
description: |
  {{ integration.append-only-loading | flatify }}

replication-method: "Key-based Incremental"

attributes:
  - name: "date_last_modified"
    type: "date-time"
    replication-key: true
    description: |
      The time the {{ table.key | replace: "-"," " }} was last modified.

  - name: "bom_id"
    type: "integer"
    description: ""

  - name: "create_date"
    type: "date-time"
    description: ""

  - name: "externalid"
    type: "string"
    description: ""

  - name: "is_autocalculate_lag"
    type: "string"
    description: ""

  - name: "isdefault"
    type: "string"
    description: ""

  - name: "isinactive"
    type: "string"
    description: ""

  - name: "item_id"
    type: "integer"
    description: ""

  - name: "location_id"
    type: "integer"
    description: ""

  - name: "mfg_routing_id"
    type: "integer"
    description: ""

  - name: "mfg_routing_memo"
    type: "string"
    description: ""

  - name: "mfg_routing_name"
    type: "string"
    description: ""
---