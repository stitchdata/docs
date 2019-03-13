---
tap-reference: "shiphero"

# version: "1.0"

foreign-keys:
  - id: "order-id"
    attribute: "order_id"
    table: "orders"
    all-foreign-keys:
      - table: "orders"
        join-on: "id"
      - table: "shipments"
      - table: "shipments"
        subattribute: "order"
        join-on: "id"


  - id: "product-id"
    attribute: "product_id"
    table: "products"
    all-foreign-keys:
      - table: "orders"
        subtable: "line_items"
      - table: "products"
        join-on: "id"
      - table: "shipments"
        subtable: "orders__line_items"

  # - id: "shipment-id"
  #   attribute: "shipment_id"
  #   table: "shipments"
  #   all-foreign-keys:
  #     - table: "shipments"
  #       join-on: "id"
      

  # - id: "vendor-id"
  #   attribute: "vendor_id"
  #   table: "vendors"
  #   all-foreign-keys:
  #     - table: "vendors"
  #     - table: ""

  - id: "warehouse-id"
    attribute: "warehouse_id"
    table: ""
    all-foreign-keys:
      - table: "orders"
        subtable: "line_items"
      - table: "products"
        subtable: "warehouses"
      - table: "shipments"
        subtable: "orders__line_items"
---