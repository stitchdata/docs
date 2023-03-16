---
tap: "yotpo"
version: "1"

name: "reviews"
doc-link: https://apidocs.yotpo.com/reference#section-what-are-reviews
singer-schema: https://github.com/singer-io/tap-yotpo/blob/master/tap_yotpo/schemas/reviews.json
description: |
  The `{{ table.name }}` table contains data about reviews.

  **Note**: This table is similar to the `product_reviews` table, but doesn't contain custom fields. If you have or need custom fields, you may want to only replicate the `product_reviews` table to prevent redundant data.

  #### Attribution window {#review-attribution-window}

  When Stitch replicates data for this table, it will use an attribution window of {{ integration.attribution-window }} to fetch updated (or deleted) reviews. This means that every time a replication job runs, the last 30 days' worth of data will be replicated for this table.

  Refer to the [Replication](#replication) section for more info and examples of how the attribution window is used to query for data.

replication-method: "Key-based Incremental"
attribution-window: true

api-method:
  name: Retrieve All Reviews
  doc-link: https://apidocs.yotpo.com/reference#retrieve-all-reviews

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The ID of the review."
    foreign-key-id: "review-id"

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
    foreign-key-id: "email-address-id"

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