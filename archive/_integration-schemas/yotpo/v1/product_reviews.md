---
tap: "yotpo"
version: "1"

name: "product_reviews"
doc-link: https://apidocs.yotpo.com/reference#section-what-are-reviews
singer-schema: https://github.com/singer-io/tap-yotpo/blob/master/tap_yotpo/schemas/product_reviews.json
description: |
  The `{{ table.name }}` table contains data about reviews for a certain product.

  **Note**: This table is similar to the `reviews` table, but also contains custom fields. If you don't have or need custom product fields, you may only want to replicate the `reviews` table to prevent redundant data.

replication-method: "Key-based Incremental"

api-method:
  name: Reviews for a Product
  doc-link: https://apidocs.yotpo.com/v1.0/reference#retrieve-reviews-for-a-specific-product

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The review ID."
    foreign-key-id: "product-review-id"

  - name: "created_at"
    type: "string"
    replication-key: true
    description: "The time the review was created."

  - name: "score"
    type: "number"
    description: "The review's score."

  - name: "votes_up"
    type: "number"
    description: "The number of upvotes in the review."

  - name: "votes_down"
    type: "number"
    description: "The number of downvotes in the review."

  - name: "content"
    type: "string"
    description: "If applicable, the comments left by the reviewer about the product."

  - name: "title"
    type: "string"
    description: "The title of the review."

  - name: "verified_buyer"
    type: "boolean"
    description: "If `true`, the reviewer is a verified buyer."

  - name: "source_review_id"
    type: "number"
    description: "If applicable, the source review ID."
    foreign-key-id: "source-review-id"

  - name: "sentiment"
    type: "number"
    description: "The sentiment of the review."

  - name: "product_id"
    type: "number"
    description: "The ID of the product that was reviewed."
    foreign-key-id: "product-id"

  - name: "user"
    type: "object"
    description: "Details about the user who wrote the review."
    subattributes: 
      - name: "user_id"
        type: "number"
        description: "The ID of the user who wrote the review."
        # foreign-key-id: "user-id"

      - name: "display_name"
        type: "string"
        description: "The display name of the user user who wrote the review."

      - name: "social_image"
        type: "string"
        description: "If applicable, the image associated with the user's social profile."

      - name: "user_type"
        type: "string"
        description: "The user's type."

      - name: "is_social_connected"
        type: "number"
        description: ""

  - name: "images_data"
    type: "object"
    description: "Details about images associated with the review."
    subattributes: 
      - name: "id"
        type: "number"
        description: "The image ID."

      - name: "original_url"
        type: "string"
        description: "The URL of the original image."

      - name: "thumb_url"
        type: "string"
        description: "The URL of the thumbnail version of the image."

  - name: "comment"
    type: "object"
    description: "Details about the comments left in the review."
    subattributes: 
      - name: "id"
        type: "number"
        description: "The comment ID."
        # foreign-key-id: "comment-id"

      - name: "content"
        type: "string"
        description: "The content of the comment."

      - name: "created_at"
        type: "string"
        description: "The time the comment was created."

      - name: "display_name"
        type: "string"
        description: "The display name of the comment."

      - name: "comments_avatar"
        type: "string"
        description: "If applicable, the avatar associated with the comment."
---