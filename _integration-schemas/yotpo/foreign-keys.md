---
tap-reference: "yotpo"

version: "1.0"

foreign-keys:
  - attribute: "product_id"
    table: "products"
    join-on: "id"

  - attribute: "source_review_id"
    table: "reviews"
    join-on: "id"

  - attribute: ""
    table: "emails"
    join-on: "id"
---