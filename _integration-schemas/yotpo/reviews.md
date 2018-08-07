---
tap: "yotpo"
version: "1.0"

name: "reviews"
doc-link: https://apidocs.yotpo.com/reference#section-what-are-reviews
singer-schema: https://github.com/singer-io/tap-yotpo/blob/master/tap_yotpo/schemas/reviews.json
description: |
  The `reviews` table contains data about reviews.

  **Note**: This table is similar to the `product_reviews` table, but doesn't contain custom fields. If you have or need custom fields, you may want to only replicate the `product_reviews` table to prevent redundant data.

replication-method: "Key-based Incremental"

api-method:
  name: Retrieve All Reviews
  doc-link: https://apidocs.yotpo.com/reference#retrieve-all-reviews

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The ID of the review."

  - name: "created_at"
    type: "string"
    replication-key: true
    description: "The time the review was created."

  - name: "updated_at"
    type: "string"
    description: "The time the review was last updated."

  - name: "votes_up"
    type: "number"
    description: "The number of upvotes the review contains."

  - name: "votes_down"
    type: "number"
    description: "The number of downvotes the review contains."

  - name: "score"
    type: "number"
    description: "The overall score of the review."

  - name: "content"
    type: "string"
    description: "The content of the review."

  - name: "title"
    type: "string"
    description: "The title of the review."

  - name: "email"
    type: "string"
    description: "The email address of the person who wrote the review."

  - name: "sentiment"
    type: "number"
    description: "The sentiment of the review."

  - name: "sku"
    type: "string"
    description: "The SKU associated with the product being reviewed."

  - name: "name"
    type: "string"
    description: "The name of the person who left the review."

  - name: "reviewer_type"
    type: "string"
    description: "The reviewer type. For example: `verified_buyer`"

  - name: "deleted"
    type: "boolean"
    description: "If `true`, the review was deleted."

  - name: "user_reference"
    type: "string"
    description: ""
---