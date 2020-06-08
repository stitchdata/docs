---
tap: "netsuite-suite-analytics"
version: "1"
key: "bin-number-count"

name: "bin_number_counts"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/bin_number_counts.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "available_count"
    type: "integer"
    description: ""

  - name: "bin_id"
    type: "integer"
    description: ""

  - name: "bin_number"
    type: "string"
    description: ""

  - name: "item_id"
    type: "integer"
    description: ""

  - name: "location_id"
    type: "integer"
    description: ""

  - name: "on_hand_count"
    type: "integer"
    description: ""
---