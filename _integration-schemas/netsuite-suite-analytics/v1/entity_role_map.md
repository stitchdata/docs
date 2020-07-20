---
tap: "netsuite-suite-analytics"
version: "1"
key: "entity-role-map"

name: "entity_role_map"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/entity_role_map.html"
description: ""

replication-method: "Full Table"
loading-behavior: "Append-Only"

attributes:
  - name: "contact_id"
    type: "integer"
    description: ""
    foreign-key-id: "contact-id"

  - name: "entity_id"
    type: "integer"
    description: ""
    foreign-key-id: "entity-id"

  - name: "role_id"
    type: "integer"
    description: ""
---