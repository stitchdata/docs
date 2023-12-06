---
tap: "netsuite-suite-analytics"
version: "1"
key: "location"

name: "locations"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/location.html"
description: ""

replication-method: "Key-based Incremental"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "date_last_modified"
    type: "date-time"
    replication-key: true
    description: |
      The time the {{ table.key | replace: "-"," " }} was last modified.

  - name: "address"
    type: "string"
    description: ""

  - name: "address_one"
    type: "string"
    description: ""

  - name: "address_three"
    type: "string"
    description: ""

  - name: "address_two"
    type: "string"
    description: ""

  - name: "addressee"
    type: "string"
    description: ""

  - name: "attention"
    type: "string"
    description: ""

  - name: "city"
    type: "string"
    description: ""

  - name: "country"
    type: "string"
    description: ""

  - name: "full_name"
    type: "string"
    description: ""

  - name: "inventory_available"
    type: "string"
    description: ""

  - name: "inventory_available_web_store"
    type: "string"
    description: ""

  - name: "is_include_in_supply_planning"
    type: "string"
    description: ""

  - name: "isinactive"
    type: "string"
    description: ""

  - name: "location_extid"
    type: "string"
    description: ""

  - name: "location_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "location-id"

  - name: "name"
    type: "string"
    description: ""

  - name: "parent_id"
    type: "integer"
    description: ""
    foreign-key-id: "location-id"

  - name: "phone"
    type: "string"
    description: ""

  - name: "return_address_one"
    type: "string"
    description: ""

  - name: "return_address_two"
    type: "string"
    description: ""

  - name: "return_city"
    type: "string"
    description: ""

  - name: "return_country"
    type: "string"
    description: ""

  - name: "return_state"
    type: "string"
    description: ""

  - name: "return_zipcode"
    type: "string"
    description: ""

  - name: "returnaddress"
    type: "string"
    description: ""

  - name: "state"
    type: "string"
    description: ""

  - name: "tran_num_prefix"
    type: "string"
    description: ""

  - name: "use_bins"
    type: "string"
    description: ""

  - name: "zipcode"
    type: "string"
    description: ""
---