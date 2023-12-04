---
tap: "netsuite-suite-analytics"
version: "1"
key: "inbound-shipment-items"

name: "inbound_shipment_items"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/inboundshipment.html"
description: |
  From NetSuite's documentation:

  > This table is available only for NetSuite accounts with the Inbound Shipment Management feature enabled.

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "amount"
    type: "number"
    description: ""

  - name: "currency_id"
    type: "integer"
    description: ""
    foreign-key-id: "currency-id"

  - name: "date_effective"
    type: "date-time"
    description: ""

  - name: "exchange_rate"
    type: "number"
    description: ""

  - name: "fx_rate"
    type: "number"
    description: ""

  - name: "inboundshipment_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""

  - name: "inboundshipmentitem_id"
    type: "integer"
    description: ""

  - name: "incoterm_id"
    type: "integer"
    description: ""

  - name: "item_id"
    type: "integer"
    description: ""

  - name: "item_type"
    type: "string"
    description: ""

  - name: "quantity_billed"
    type: "integer"
    description: ""

  - name: "quantity_expected"
    type: "number"
    description: ""

  - name: "quantity_received"
    type: "integer"
    description: ""

  - name: "quantity_remaining"
    type: "integer"
    description: ""

  - name: "receiving_location_id"
    type: "integer"
    description: ""

  - name: "unit_id"
    type: "integer"
    description: ""

  - name: "unit_rate"
    type: "number"
    description: ""

  - name: "vendor_id"
    type: "integer"
    description: ""

  - name: "vendor_name"
    type: "string"
    description: ""
---