---
tap: "netsuite-suite-analytics"
version: "1"
key: "crm-group-map"

name: "crmgroupmap"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/crmgroupmap.html"
description: ""

replication-method: "Full Table"
loading-behavior: "Append-Only"

attributes:
  - name: "entity_id"
    type: "integer"
    description: ""

  - name: "group_id"
    type: "integer"
    description: ""

  - name: "is_primary"
    type: "string"
    description: ""
---