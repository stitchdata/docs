---
tap-reference: "yotpo"

version: "1.0"

foreign-keys:
  - id: "email-address-id"
    attribute: "email_address"
    table: "emails"
    join-on: "email_address"
    all-foreign-keys:
      - table: "emails"
      - table: "unsubscribers"
        join-on: "user_email"

  - id: "order-id"
    attribute: "order_id"
    table: ""
    join-on: "order_id"
    all-foreign-keys:
      - table: "emails"
      - table: ""

  - id: "product-id"
    attribute: "product_id"
    table: "products"
    join-on: "id"
    all-foreign-keys:
      - table: "products"
      - table: "product_reviews"

  - id: "product-review-id"
    attribute: "product_review_id"
    table: "product_reviews"
    join-on: "id"
    all-foreign-keys:
      - table: "product_reviews"
        join-on: "id"

  - id: "review-id"
    attribute: "source_review_id"
    table: "reviews"
    join-on: "id"
    all-foreign-keys:
      - table: "product_reviews"
      - table: "reviews"
        join-on: "id"
---