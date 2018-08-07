---
tap: "yotpo"
version: "1.0"

name: "reviews"
doc-link: https://apidocs.yotpo.com/reference#section-what-are-reviews
singer-schema: https://github.com/singer-io/tap-yotpo/blob/master/tap_yotpo/schemas/reviews.json
description: |
  The `reviews` table contains data about reviews

replication-method: "Key-based Incremental"

api-method:
  name: Retrieve All Reviews
  doc-link: https://apidocs.yotpo.com/reference#retrieve-all-reviews

attributes:

  - name: "id"
    type: "integer"
    primary-key: true
    description: ""

  - name: "created_at"
    type: "string"
    replication-key: true
    description: ""

  - name: "updated_at"
    type: "string"
    description: ""

  - name: "votes_up"
    type: "number"
    description: ""

  - name: "votes_down"
    type: "number"
    description: ""

  - name: "score"
    type: "number"
    description: ""

  - name: "content"
    type: "string"
    description: ""

  - name: "title"
    type: "string"
    description: ""

  - name: "email"
    type: "string"
    description: ""

  - name: "sentiment"
    type: "number"
    description: ""

  - name: "sku"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "reviewer_type"
    type: "string"
    description: ""

  - name: "deleted"
    type: "boolean"
    description: ""

  - name: "user_reference"
    type: "string"
    description: ""
---
