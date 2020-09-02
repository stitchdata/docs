---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-foreign-keys/
## FOR INSTRUCTIONS & REFERENCE INFO

tap-reference: "square"

version: "1"

foreign-keys: 
  - id: "bank-account-id"
    table: "bank_accounts"
    attribute: "id"
    all-foreign-keys:
      - table: "bank_accounts"
        join-on: "id"
      - table: "settlements"
        join-on: "bank_account_id" 

  # - id: "cash-drawer-id"
  #   table: "cash_drawer_shifts"
  #   attribute: "id"
  #   all-foreign-keys:
  #     - table: ""
  #       join-on: ""

  - id: "category-id"
    table: "categories"
    attribute: "category_id"
    all-foreign-keys:
      - table: "categories"
        join-on: "id"
      - table: "items"
        subattribute: "item_data"

  - id: "discount-id"
    table: "discounts"
    attribute: ""
    all-foreign-keys:
      - table: "discounts"
        join-on: "id"

  - id: "employee-id"
    table: "employees"
    attribute: "id"
    all-foreign-keys:
      - table: "employees"
        join-on: "id"
      - table: "shifts"
        join-on: "employee_id"  

  - id: "item-id"
    table: "items"
    attribute: "item_id"
    all-foreign-keys:
      - table: "items"
        join-on: "id"

      - table: "items"
        subattribute: "item_data.variations.item_variation_data"

      - table: "orders"
        subattribute: "item_data.variations.item_variation_data"

  - id: "location-id"
    table: "locations"
    attribute: "id"
    all-foreign-keys:
      - table: "bank_accounts"
      - table: "categories"
        subattribute: "absent_at_location_ids"
        join-on: "value"

      - table: "discounts"
        subattribute: "absent_at_location_ids"
        join-on: "value"

      - table: "employees"
        subattribute: "location_ids"
        join-on: "value" 

      - table: "inventories"

      - table: "items"
        subattribute: "absent_at_location_ids"
        join-on: "value" 

      - table: "items"
        subattribute: "item_data.variations.item_variation_data.location_overrides"

      - table: "items"
        subattribute: "item_data.variations.item_variation_data.present_at_location_ids"
        join-on: "value" 

      - table: "items"
        subattribute: "present_at_location_ids"
        join-on: "value"

      - table: "location"
        join-on: "id"

      - table: "modifier_lists"
        subattribute: "absent_at_location_ids"
        join-on: "value"

      - table: "orders"
        subattribute: "item_data.variations.item_variation_data.item_variation_data.location_overrides"

      - table: "orders"

      - table: "orders"
        subattribute: "refunds"

      - table: "orders"
        subattribute: "tenders"

      - table: "payments"

      - table: "refunds"

      - table: "shifts"

      - table: "taxes"
        subattribute: "absent_at_location_ids"
        join-on: "value"    

  - id: "modifier-list-id"
    table: "modifier_lists"
    attribute: "modifier_list_id"
    all-foreign-keys:
      - table: "items"
        subattribute: "item_data.modifier_list_info"

      - table: "modifier_lists"
        join-on: "id"
      - table: "modifier_lists"
        subattribute: "modifier_list_data.modifiers.modifier_data"

  - id: "order-id"
    table: "orders"
    attribute: "id"
    all-foreign-keys:
      - table: "orders"
        join-on: "id"
      - table: "orders"
        join-on: "order_id"
      - table: "orders"
        subattribute: "returns"
        join-on: "source_order_id"
      - table: "payments"
        join-on: "order_id"  
      - table: "refunds"
        join-on: "order_id"     

  - id: "payment-id"
    table: "payments"
    attribute: "id"
    all-foreign-keys:
      - table: "orders"
        join-on: "payment_id"
      - table: "orders"
        subattribute: "tenders"
      - table: "payments"
        join-on: "id"
      - table: "refunds"
        join-on: "payment_id"

  - id: "refund-id"
    table: "refunds"
    attribute: "id"
    all-foreign-keys:
      - table: "orders"
        subattribute: "refund_ids"
        join-on: "value"  
      - table: "orders"
        subattribute: "refunds"
        join-on: "id" 
      - table: "payments"
        join-on: "order_id"
      - table: "payments"
        subattribute: "refund_ids"
        join-on: "value"
      - table: "refunds"
        join-on: "id"

  - id: "role-id"
    table: "roles"
    attribute: "id"
    all-foreign-keys:
      - table: "roles"
        join-on: "id" 

  - id: "tax-id"
    table: "taxes"
    attribute: "id"
    all-foreign-keys:
      - table: "items"
        subattribute: "item_data.tax_ids"
        join-on: "value" 

      - table: "taxes"
        join-on: "id"

  - id: "tender-id"
    table: ""
    attribute: "tender_id"
    all-foreign-keys:
      - table: "orders"
      - table: "orders"
        subattribute: "refunds"
      - table: "orders"
        subattribute: "tenders"
        join-on: "id"                           
---