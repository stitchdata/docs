---
tap-reference: "bigcommerce"

version: "1"

foreign-keys:
  - id: "coupons-id"
    attribute: ""
    table: "coupons"
    all-foreign-keys:
      - table: "coupons"
        join-on: "id"
      - table: "orders"
        subtable: "coupons"
      - table: "orders"
        subtable: "products__applied_discounts"
        join-on: "id"

  - id: "customer-id"
    attribute: "customer_id"
    table: "customers"
    all-foreign-keys:
      - table: "customers"
        join-on: "id"
      - table: "orders"

  # - id: "order-id"
  #   attribute: "order_id"
  #   table: "orders"
  #   all-foreign-keys:
  #     - table: "orders"
  #       join-on: "id"
  #     - table: "orders"
  #       subtable: "coupons"
        # - table: "orders"
        #   subtable: "products"
  #     - table: "orders"
  #       subtable: "shipping_addresses"

  - id: "product-id"
    attribute: "product_id"
    table: "products"
    all-foreign-keys:
      - table: "products"
        join-on: "id"
      - table: "products"
        subtable: "images"
      - table: "products"
        subtable: "related_products"
        join-on: "value"
      - table: "products"
        subtable: "variants"
      - table: "orders"
        subtable: "products"
      - table: "orders"
        subtable: "products"
        join-on: "parent_order_product_id"

---