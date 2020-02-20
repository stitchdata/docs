---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-foreign-keys/
## FOR INSTRUCTIONS & REFERENCE INFO

tap-reference: "3plcentral"

version: "1"

foreign-keys:
  - id: "customer-id"
    table: "customers"
    attribute: "customer_id"
    all-foreign-keys:
      - table: "customers"
        join-on: "customer_id"

      - table: "sku_items"
        join-on: "customer_id"

      - table: "stock_details"
        join-on: "customer_id" 

      - table: "inventory"
        subattribute: "customer_identifier"
        join-on: "id"

      - table: "locations"
        subattribute: "customer_identifier"
        join-on: "id"

      - table: "orders"
        subattribute: "customer_identifier"
        join-on: "id"
      
      - table: "orders"
        subattribute: "batch_identifier.name_key.customer_identifier"
        join-on: "id"

      - table: "orders"
        subattribute: "retailer_info.name_key.customer_identifier"
        join-on: "id" 

      - table: "sku_items"
        subattribute: "customer_identifier"
        join-on: "id"          

  - id: "facility-id"
    table: "facilities"
    attribute: "facility_id"
    all-foreign-keys:
      - table: "customers"
        subattribute: "facilities"
        join-on: "id"

      - table: "customers"
        subattribute: "primary_facility_identifier" 
        join-on: "id"

      - table: "inventory"
        subattribute: "facility_identifier"
        join-on: "id"

      - table: "inventory"
        subattribute: "location_identifier.name_key.facility_identifier"
        join-on: "id"

      - table: "inventory"
        subattribute: "pallet_identifier.name_key.facility_identifier"
        join-on: "id"

      - table: "locations"
        join-on: "facility_id"
      
      - table: "locations"
        subattribute: "item_traits.pallet_identifier.name_key.facility_identifier"
        join-on: "id"    

      - table: "locations"
        subattribute: "location_identifier.name_key.facility_identifier"
        join-on: "id"

      - table: "orders"
        join-on: "facility_identifier.id"   

      - table: "sku_items"
        subattribute: "options.directed_put_away.preferred_location_identifier.name_key.facility_identifier"
        join-on: "id" 

      - table: "stock_details"
        subattribute: "location_identifier.name_key.facility_identifier"
        join-on: "id"

      - table: "stock_details"
        subattribute: "pallet_identifier.name_key.facility_identifier"
        join-on: "id"

      - table: "stock_summaries"
        join-on: "facility_id" 

  - id: "item-identifier"
    table: "sku_items"
    attribute: "item_identifier"
    subattributes: "id"
    all-foreign-keys:
      - table: "inventory"
        subattribute: "item_identifier"
        join-on: "id"

      - table: "sku_items"
        subattribute: "item_identifier"
        join-on: "id"

      - table: "sku_items"
        subattribute: "kit.components.item_identifier"
        join-on: "id"

      - table: "stock_details"
        subattribute: "item_identifier"
        join-on: "id"

  - id: "item-id"
    table: "sku_items"
    attribute: "item_id"
    all-foreign-keys:
      - table: "locations"
        subattribute: "item_traits.item_identifier"
        join-on: "id"  

      - table: "sku_items"
        join-on: "item_id"

      - table: "stock_summaries"
        join-on: "item_id"  

  - id: "location-id"
    table: "locations"
    attribute: "location_id"
    all-foreign-keys:
      - table: "inventory"
        subattribute: "location_identifier"
        join-on: "id"

      - table: "locations"
        join-on: "location_id"

      - table: "locations"
        subattribute: "location_identifier"
        join-on: "id"

      - table: "sku_items"
        subattribute: "options.directed_put_away.preferred_location_identifier"
        join-on: "id"

      - table: "stock_details"
        subattribute: "location_identifier"
        join-on: "id"

  - id: "order-id"
    table: "orders"
    attribute: "order_id"
    all-foreign-keys:
      - table: "orders"
        join-on: "order_id"

  - id: "pallet-id"
    table: "pallets"
    attribute: "id"
    all-foreign-keys:
      - table: "inventory"
        subattribute: "pallet_identifier"
        join-on: "id"

      - table: "locations"
        subattribute: "item_traits.pallet_identifier"
        join-on: "id"

      - table: "stock_details"
        subattribute: "pallet_identifier"
        join-on: "id"

  - id: "receiver-id"
    table: "receivers"
    attribute: "id"
    all-foreign-keys:
      - table: "inventory"
        join-on: "receiver_id"

      - table: "stock_details"
        join-on: "receiver_id"                             

  - id: "receive-item-id"
    table: "stock_details"
    attribute: "receive_item_id"
    all-foreign-keys:
      - table: "stock_details"
        join-on: "receive_item_id"

      - table : "inventory"
        join-on: "receive_item_id" 

  - id: "supplier-id"
    table: "suppliers"
    attribute: "id"
    all-foreign-keys:
      - table: "inventory"
        subattribute: "supplier_identifier"
        join-on: "id"

      - table: "stock_details"
        subattribute: "supplier_identifier"
        join-on: "id"
---