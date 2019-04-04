---
tap-reference: "yotpo"

version: "1.0"

foreign-keys:
  - id: "email-address-id"
    attribute: "email_address"
    table: "emails"
    all-foreign-keys:
      - table: "emails"
      - table: "unsubscribers"
        join-on: "user_email"

  - id: "order-id"
    attribute: "order_id"
    table: ""
    all-foreign-keys:
      - table: "emails"

  - id: "product-id"
    attribute: "product_id"
    table: "products"
    all-foreign-keys:
      - table: "products"
      - table: "product_reviews"

  - id: "product-review-id"
    attribute: "product_review_id"
    table: "product_reviews"
    all-foreign-keys:
      - table: "product_reviews"
        join-on: "id"

  - id: "review-id"
    attribute: "source_review_id"
    table: "reviews"
    all-foreign-keys:
      - table: "product_reviews"
      - table: "reviews"
        join-on: "id"
---