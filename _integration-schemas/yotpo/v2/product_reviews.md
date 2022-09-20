---
tap: "yotpo"
version: "2"
key: ""

name: "product_reviews"
doc-link: https://apidocs.yotpo.com/reference/about-storefront-reviews
singer-schema: https://github.com/singer-io/tap-yotpo/tree/master/tap_yotpo/schemas/product_reviews.json
description: |
  The `{{ table.name }}` table contains data about reviews for a certain product.

  **Note**: This table is similar to the `reviews` table, but also contains custom fields. If you don't have or need custom product fields, you may only want to replicate the `reviews` table to prevent redundant data.

replication-method: "Key-based Incremental"

api-method:
  name: Retrieve reviews for a Product
  doc-link: https://apidocs.yotpo.com/reference/retrieve-reviews-for-a-product

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The review ID."
    foreign-key-id: "product-review-id"

  - name: "created_at"
    type: "date-time"
    replication-key: true
    description: "The time the review was created."

  - name: "comment"
    type: "object"
    description: ""
    subattributes:
      - name: "id"
        type: "integer"
        description: ""

      - name: "content"
        type: "string"
        description: ""

      - name: "created_at"
        type: "date-time"
        description: ""

      - name: "display_name"
        type: "string"
        description: ""

      - name: "comments_avatar"
        type: "string"
        description: ""


  - name: "content"
    type: "string"
    description: ""

  - name: "custom_fields"
    type: "object"
    description: ""

  - name: "deleted"
    type: "boolean"
    description: ""

  - name: "domain_key"
    type: "string"
    description: ""

  - name: "images_data"
    type: "array"
    description: ""
    subattributes:
      - name: "id"
        type: "integer"
        description: ""

      - name: "original_url"
        type: "string"
        description: ""

      - name: "thumb_url"
        type: "string"
        description: ""


  - name: "name"
    type: "string"
    description: ""

  - name: "product_id"
    type: "integer"
    description: ""

  - name: "product_yotpo_id"
    type: "string"
    description: ""

  - name: "score"
    type: "number"
    description: ""

  - name: "sentiment"
    type: "number"
    description: ""

  - name: "source_review_id"
    type: "number"
    description: ""

  - name: "title"
    type: "string"
    description: ""

  - name: "user"
    type: "object"
    description: ""
    subattributes:
    - name: "user_id"
      type: "integer"
      description: ""

    - name: "display_name"
      type: "string"
      description: ""

    - name: "social_image"
      type: "string"
      description: ""

    - name: "user_type"
      type: "string"
      description: ""

    - name: "is_social_connected"
      type: "number"
      description: ""


  - name: "verified_buyer"
    type: "boolean"
    description: ""

  - name: "votes_down"
    type: "integer"
    description: ""

  - name: "votes_up"
    type: "integer"
    description: ""
---