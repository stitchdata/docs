---
tap-reference: "shippo"

version: "1"

foreign-keys: 
  - id: "address-id"
    attribute: ""
    table: "addresses"
    all-foreign-keys:
      - table: "addresses"
        join-on: "object_id"
      - table: "shipments"
        join-on: "object_from"
      - table: "shipments"
        join-on: "object_to"
      - table: "shipments"
        join-on: "object_return"

  - id: "parcel-id"
    attribute: ""
    table: "parcels"
    all-foreign-keys:
      - table: "parcels"
        join-on: "object_id"
      - table: "shipments"
        join-on: "object_parcel"

  - id: "refund-id"
    attribute: ""
    table: "refunds"
    all-foreign-keys:
      - table: "refunds"
        join-on: "object_id"

  - id: "shipment-id"
    attribute: "shipment"
    table: "shipments"
    all-foreign-keys:
      - table: "shipment"
        oin-on: "object_id"

  - id: "transaction-id"
    attribute: "transaction"
    table: "transactions"
    all-foreign-keys:
      - table: "refunds"
      - table: "transactions"
        join-on: "object_id"
---