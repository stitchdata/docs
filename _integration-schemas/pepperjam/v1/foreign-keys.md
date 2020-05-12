---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-foreign-keys/
## FOR INSTRUCTIONS & REFERENCE INFO

tap-reference: "pepperjam"

version: "1"

foreign-keys:
  - id: "advanced-link-id"
    table: "creative_advanced"
    attribute: "id"
    all-foreign-keys:
      - table: "creative_advanced"
        join-on: "id"

  - id: "banner-id"
    table: "creative_banner"
    attribute: "id"
    all-foreign-keys:
      - table: "creative_banner"
        join-on: "id"

  - id: "coupon-id"
    table: "creative_coupon"
    attribute: "id"
    all-foreign-keys:
      - table: "creative_coupon"
        join-on: "id"

  - id: "type-id"
    table: "creative_generic"
    attribute: "type"
    all-foreign-keys:
      - table: "creative_generic"
        join-on: "type"
      - table: "creative_performance"
        join-on: "creative_type"
      - table: "creative_performance_by_publisher"
        join-on: "creative_type"  

  - id: "creative-id"
    table: "creative_performance"
    attribute: "creative-id"
    all-foreign-keys:
      - table: "creative_performance"
        join-on: "creative_id"
      - table: "creative_performance_by_publisher"
        join-on: "creative_id"

  - id: "date-id"
    table: "creative_performance"
    attribute: "date"
    all-foreign-keys:
      - table: "creative_performance"
        join-on: "date"
      - table: "creative_performance_by_publisher"
        join-on: "date"  

  - id: "publisher-id"
    table: "publisher"
    attribute: "id"
    all-foreign-keys:
      - table: "publisher"
        join-on: "id"
      - table: "creative_performance_by_publisher"
        join-on: "publisher_id"
      - table: "publisher_performance"
        join-on: "publisher_id"


  - id: "product-id"
    table: "creative_product"
    attribute: "id"
    all-foreign-keys:
      - table: "creative_product"
        join-on: "id"
      - table: "itemized_list_product"
        join-on: "id"  

  - id: "promotion-id"
    table: "creative_promotion"
    attribute: "id"
    all-foreign-keys:
      - table: "creative_promotion"
        join-on: "id"

  - id: "text-id"
    table: "creative_text"
    attribute: "id"
    all-foreign-keys:
      - table: "creative_text"
        join-on: "id"

  - id: "group-id"
    table: "group"
    attribute: "id"
    all-foreign-keys:
      - table: "group"
        join-on: "id"

  - id: "member-id"
    table: "group_member"
    attribute: "id"
    all-foreign-keys:
      - table: "group_member"
        join-on: "id"

  - id: "itemized-list-id"
    table: "itemized_list"
    attribute: "id"
    all-foreign-keys:
      - table: "itemized_list"
        join-on: "id"

  - id: "order-id"
    table: "publisher_performance"
    attribute: "order_id"
    all-foreign-keys:
      - table: "publisher_performance"
        join-on: "order_id"

  - id: "sale-date-id"
    table: "publisher_performance"
    attribute: "sale_date"
    all-foreign-keys:
      - table: "publisher_performance"
        join-on: "sale_date"

  - id: "term-id"
    table: "term"
    attribute: "id"
    all-foreign-keys:
      - table: "term"
        join-on: "id"

  - id: "transaction-id"
    table: "transaction_details"
    attribute: "transaction_id"
    all-foreign-keys:
      - table: "transaction_details"
        join-on: "transaction_id"
        
  - id: ""
    table: ""
    attribute: ""
    all-foreign-keys:
      - table: ""
        join-on: ""                                    
---