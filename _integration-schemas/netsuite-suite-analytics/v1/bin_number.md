---
tap: "netsuite-suite-analytics"
version: "1"
key: "bin-number"

name: "bin_number"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/bin_number.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "bin_id"
    type: "integer"
    description: ""

  - name: "bin_number"
    type: "string"
    description: ""

  - name: "bin_number_extid"
    type: "string"
    description: ""

  - name: "isinactive"
    type: "string"
    description: ""

  - name: "ispreferred"
    type: "string"
    description: ""

  - name: "item_id"
    type: "integer"
    description: ""

  - name: "location_id"
    type: "integer"
    description: ""

  - name: "memo"
    type: "string"
    description: ""

  - name: "on_hand_count"
    type: "integer"
    description: ""
---