---
tap: "netsuite-suite-analytics"
version: "1"
key: "entity-territory-map"

name: "entityterritorymap"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/entityterritorymap.html"
description: ""

replication-method: "Full Table"
loading-behavior: "Append-Only"

attributes:
  - name: "entity_id"
    type: "integer"
    description: ""
    foreign-key-id: "entity-id"

  - name: "territory_id"
    type: "integer"
    description: ""
    foreign-key-id: "territory-id"
---