---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-foreign-keys/
## FOR INSTRUCTIONS & REFERENCE INFO

tap-reference: "3plcentral"

version: "1.0"

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
        join-on: "customer_identifier.id" 
      - table: "orders"
        join-on: "customer_identifier.id"
      - table: "locations"
        join-on: "customer_identifier.id"
      - table: "orders"
        join-on: "batch_identifier.name_key.customer_identifier.id"
      - table: "orders"
        join-on: "retailer_info.name_key.customer_identifier.id" 
      - table: "sku_items"
        join-on: "customer_identifier.id"           

  - id: "item-id"
    table: "sku_items"
    attribute: "item_id"
    all-foreign-keys:
      - table: "sku_items"
        join-on: "item_id"
      - table: "stock_summaries"
        join-on: "item_id"
      - table: "locations"
        join-on: "item_traits.item_identifier.id"    

  - id: "location-id"
    table: "locations"
    attribute: "location_id"
    all-foreign-keys:
      - table: "locations"
        join-on: "location_id"
      - table: "inventory"
        join-on: "location_identifier.id"
      - table: "stock_details"
        join-on: "location_identifier.id"
      - table: locations
        join-on: "location_identifier.id"  
        
  - id: "supplier-id"
    table: "suppliers"
    attribute: "id"
    all-foreign-keys:
      - table: "stock_details"
        join-on: "supplier_identifier.id"
      - table: "inventory"
        join-on: "supplier_identifier.id"
        
  - id: "facility-id"
    table: "facilities"
    attribute: "facility_id"
    all-foreign-keys:
      - table: "locations"
        join-on: "facility_id"
      - table: "stock_summaries"
        join-on: "facility_id"
      - table: "inventory"
        join-on: "facility_identifier.id"
      - table: "orders"
        join-on: "facility_identifier.id"       
      - table: "customers"
        join-on: "facilities.id"
      - table: "customers"
        join-on: "primary_facility_identifier.id"
      - table: "locations"
        join-on: "item_traits.pallet_identifier.name_key.facility_identifier.id"    
      - table: "locations"
        join-on: "location_identifier.name_key.facility_identifier.id"
      - table: "sku_items"
        join-on: "options.directed_put_away.preferred_location_identifier.name_key.facility_identifier.id" 
      - table: "stock_details"
        join-on: "location_identifier.name_key.facility_identifier.id"   

  - id: "order-id"
    table: "orders"
    attribute: "order_id"
    all-foreign-keys:
      - table: "orders"
        join-on: "order_id"
        
  - id: "receive-item-id"
    table: "stock_details"
    attribute: "receive_item_id"
    all-foreign-keys:
      - table: "stock_details"
        join-on: "receive_item_id"
      - table : "inventory"
        join-on: "receive_item_id" 
     
  - id: "item-identifier"
    table: "sku_items"
    attribute: "item_identifier"
    subattributes: "id"
    all-foreign-keys:
      - table: "sku_items"
        join-on: "item_identifier.id"
      - table: "stock_details"
        join-on: "item_identifier.id"
      - table: "inventory"
        join-on: "item_identifier.id"
        
  - id: "pallet-id"
    table: "pallets"
    attribute: "id"
    all-foreign-keys:
      - table: "inventory"
        join-on: "pallet_identifier.id"

  - id: "receiver-id"
    table: "receivers"
    attribute: "id"
    all-foreign-keys:
      - table: "stock_details"
        join-on: "receiver-id"                                                           
---