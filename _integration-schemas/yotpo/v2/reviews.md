---
tap: "yotpo"
version: "2"
key: ""

name: "reviews"
doc-link: https://apidocs.yotpo.com/reference#section-what-are-reviews
singer-schema: https://github.com/singer-io/tap-yotpo/tree/master/tap_yotpo/schemas/reviews.json
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

  - name: "updated_at"
    type: "string"
    replication-key: true
    description: "The time the review was last updated."

  - name: "archived"
    type: "boolean"
    description: ""

  - name: "content"
    type: "string"
    description: ""

  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "deleted"
    type: "boolean"
    description: ""

  - name: "email"
    type: "string"
    description: ""

  - name: "escalated"
    type: "boolean"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "reviewer_type"
    type: "string"
    description: ""

  - name: "score"
    type: "number"
    description: ""

  - name: "sentiment"
    type: "number"
    description: ""

  - name: "sku"
    type: "string"
    description: ""

  - name: "title"
    type: "string"
    description: ""

  - name: "user_reference"
    type: "string"
    description: ""

  - name: "votes_down"
    type: "number"
    description: ""

  - name: "votes_up"
    type: "number"
    description: ""
---