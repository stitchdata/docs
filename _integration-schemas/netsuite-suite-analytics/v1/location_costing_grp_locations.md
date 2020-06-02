---
tap: "netsuite-suite-analytics"
version: "1"
key: "location-costing-group-locations"

name: "location_costing_grp_locations"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/location_costing_grp_locations.html"
description: ""
replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "location_costing_group_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "location-costing-group-id"

  - name: "location_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "location-id"
---