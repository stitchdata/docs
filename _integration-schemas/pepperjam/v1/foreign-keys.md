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

  - id: "affiliate-id"
    table: ""
    attribute: "affiliate_id"
    all-foreign-keys:
      - table: "creative_advanced"
        subattribute: "private_affiliates"
        join-on: "id"
      - table: "creative_banner"
        subattribute: "private_affiliates"
        join-on: "id"
      - table: "creative_coupon"
        subattribute: "private_affiliates"
        join-on: "id"
      - table: "creative_text"
        subattribute: "private_affiliates"
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

  - id: "creative-id"
    table: ""
    attribute: "creative_id"
    all-foreign-keys:
      - table: "creative_performance"
      - table: "creative_performance_by_publisher"
      - table: "transaction_details"

  - id: "group-id"
    table: "group"
    attribute: "group_id"
    all-foreign-keys:
      - table: "creative_performance"
      - table: "creative_performance_by_publisher"
      - table: "group"
        join-on: "id"
      - table: "group_member"
      - table: "publisher"
        subattribute: "group"
        join-on: "id"
      - table: "publisher_performance"
      - table: "transaction_details"
      - table: "transaction_history"

  - id: "itemized-list-id"
    table: "itemized_list"
    attribute: "list_id"
    all-foreign-keys:
      - table: "itemized_list"
        join-on: "id"
      - table: "itemized_list_product"

  - id: "itemized-list-product-id"
    table: "itemized_list_product"
    attribute: "id"
    all-foreign-keys:
      - table: "itemized_list_product"
        join-on: "id"

  - id: "member-id"
    table: "group_member"
    attribute: "id"
    all-foreign-keys:
      - table: "group_member"
        join-on: "id"

  - id: "order-id"
    table: "publisher_performance"
    attribute: "order_id"
    all-foreign-keys:
      - table: "publisher_performance"
      - table: "transaction_details"
      - table: "transaction_history"

  - id: "publisher-id"
    table: "publisher"
    attribute: "publisher_id"
    all-foreign-keys:
      - table: "publisher"
        join-on: "id"
      - table: "creative_performance_by_publisher"
      - table: "publisher_performance"
      - table: "transaction_details"
      - table: "transaction_history"

  - id: "product-id"
    table: "creative_product"
    attribute: "id"
    all-foreign-keys:
      - table: "creative_product"
        join-on: "id"

  - id: "promotion-id"
    table: "creative_promotion"
    attribute: "id"
    all-foreign-keys:
      - table: "creative_advanced"
        subattribute: "promotions"
        join-on: "id"
      - table: "creative_banner"
        subattribute: "promotions"
        join-on: "id"
      - table: "creative_coupon"
        subattribute: "promotions"
        join-on: "id"
      - table: "creative_promotion"
        join-on: "id"
      - table: "creative_text"
        subattribute: "promotions"
        join-on: "id"

  - id: "term-id"
    table: "term"
    attribute: "id"
    all-foreign-keys:
      - table: "publisher"
        subattribute: "term"
        join-on: "id"
      - table: "term"
        join-on: "id"

  - id: "text-id"
    table: "creative_text"
    attribute: "id"
    all-foreign-keys:
      - table: "creative_text"
        join-on: "id"

  - id: "transaction-id"
    table: ""
    attribute: "transaction_id"
    all-foreign-keys:
      - table: "transaction_details" 
      - table: "transaction_history"

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
---