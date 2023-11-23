---
tap: "netsuite-suite-analytics"
version: "1"
key: "inbound-shipment"

name: "inbound_shipments"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/inboundshipment.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "bill_of_landing"
    type: "string"
    description: ""

  - name: "bill_status"
    type: "string"
    description: ""

  - name: "currency_id"
    type: "integer"
    description: ""
    foreign-key-id: "currency-id"

  - name: "date_actual_delivery"
    type: "date-time"
    description: ""

  - name: "date_actual_shipping"
    type: "date-time"
    description: ""

  - name: "date_create"
    type: "date-time"
    description: ""

  - name: "date_expected_delivery"
    type: "date-time"
    description: ""

  - name: "date_expected_shipping"
    type: "date-time"
    description: ""

  - name: "inboundshipment_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""

  - name: "memo"
    type: "string"
    description: ""

  - name: "shipment_number"
    type: "integer"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "vessel_number"
    type: "string"
    description: ""
---