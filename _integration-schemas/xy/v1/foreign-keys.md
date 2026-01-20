---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-foreign-keys/
## FOR INSTRUCTIONS & REFERENCE INFO

tap-reference: "x-y"

version: "1"

foreign-keys:
  - id: "item-id"
    table: "item"
    attribute: "id"
    all-foreign-keys:
      - table: "item"
        join-on: "id"
      - table: "inventory" 
        join-on: "item_uri"
      - table: "inventory_movement" 
        join-on: "item_uri"
      - table: "sales_order_line" 
        join-on: "item_uri"
      - table: "stock_transfer" 
        join-on: "item_uri"     

  - id: "order-id"
    table: "sales_order_line"
    attribute: "id"
    all-foreign-keys:
      - table: "sales_order_line"
        join-on: "id"
      - table: "inventory_movement"
        join-on: "order"
      - table: "sales_order_line"
        join-on: "order_uri"                                   
---