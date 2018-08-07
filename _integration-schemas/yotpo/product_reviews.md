---
tap: "yotpo"
version: "1.0"

name: "product_reviews"
doc-link: https://apidocs.yotpo.com/reference#section-what-are-reviews
singer-schema: https://github.com/singer-io/tap-yotpo/blob/master/tap_yotpo/schemas/product_reviews.json
description: |
  The `product_reviews` table contains data about reviews for a certain product.

replication-method: "Key-based Incremental"

api-method:
  name: Reviews for a Product
  doc-link: https://apidocs.yotpo.com/v1.0/reference#retrieve-reviews-for-a-specific-product

attributes:

  - name: "id"
    type: "integer"
    primary-key: true
    description: ""

  - name: "created_at"
    type: "string"
    replication-key: true
    description: ""

  - name: "score"
    type: "number"
    description: ""

  - name: "votes_up"
    type: "number"
    description: ""

  - name: "votes_down"
    type: "number"
    description: ""

  - name: "content"
    type: "string"
    description: ""

  - name: "title"
    type: "string"
    description: ""

  - name: "verified_buyer"
    type: "boolean"
    description: ""

  - name: "source_review_id"
    type: "number"
    description: ""

  - name: "sentiment"
    type: "number"
    description: ""

  - name: "product_id"
    type: "number"
    description: ""

  - name: "user"
    type: "object"
    description: ""

    object-attributes: 
    - name: "user_id"
      type: "number"
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

  - name: "images_data"
    type: "object"
    description: ""

    object-attributes: 
    - name: "id"
      type: "number"
      description: ""

    - name: "original_url"
      type: "string"
      description: ""

    - name: "thumb_url"
      type: "string"
      description: ""

  - name: "comment"
    type: "object"
    description: ""

    object-attributes: 
    - name: "id"
      type: "number"
      description: ""

    - name: "content"
      type: "string"
      description: ""

    - name: "created_at"
      type: "string"
      description: ""

    - name: "display_name"
      type: "string"
      description: ""

    - name: "comments_avatar"
      type: "string"
      description: ""
---
