---
tap: "netsuite-suite-analytics"
version: "1"
key: "commission-rate"

name: "commissionrate"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/commissionrate.html"
description: ""

replication-method: "Full Table"
loading-behavior: "Append-Only"

attributes:
  - name: "commisssion_schedule_id"
    type: "integer"
    description: ""

  - name: "rate"
    type: "integer"
    description: ""
---