---
tap: "netsuite-suite-analytics"
version: "1"
key: "competitor-opp-map"

name: "competitoroppmap"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/competitoroppmap.html"
description: ""

replication-method: "Full Table"
loading-behavior: "Append-Only"

attributes:
  - name: "competitor_id"
    type: "integer"
    description: ""

  - name: "is_winner"
    type: "string"
    description: ""

  - name: "notes"
    type: "string"
    description: ""

  - name: "opportunity_id"
    type: "integer"
    description: ""
---