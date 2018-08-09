---
tap: "uservoice"
# version: "1.0"

name: "features"
doc-link: https://developer.uservoice.com/docs/api/v2/reference/#/Feature
singer-schema: https://github.com/singer-io/tap-uservoice/blob/master/tap_uservoice/streams/feature_statuses.py
description: |
  The `{{ table.name }}` table contains info about planned product features.

replication-method: "Key-based Incremental"

api-method:
  name: List features
  doc-link: https://developer.uservoice.com/docs/api/v2/reference/#list-features

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The feature ID."

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the feature was last updated."

  - name: "description"
    type: "string"
    description: "A description of the feature."

  - name: "is_blocker"
    type: "boolean"
    description: ""

  - name: "links"
    type: "object"
    description: ""
    object-attributes: 
    - name: "created_by"
      type: "integer"
      description: "The ID of the user who created the feature."
      foreign-key: true
      table: "users"

    - name: "feature_status"
      type: "integer"
      description: "The status of the feature."

    - name: "product_area"
      type: "integer"
      description: "The product area of the feature."

    - name: "updated_by"
      type: "integer"
      description: "The ID of the user who last updated the feature."
      foreign-key: true
      table: "users"

  - name: "name"
    type: "string"
    description: "The name of the feature."

  - name: "suggestions_count"
    type: "integer"
    description: "The total number of suggestions associated with the feature."

  - name: "supporter_mrr_cents"
    type: "integer"
    description: "The total amount of supporter MRR for the feature, in cents."

  - name: "supporting_accounts_count"
    type: "integer"
    description: "The total number of supporting accounts associated with the feature."

  - name: "supporting_users_count"
    type: "integer"
    description: "The total number of supporting users associated with the feature."
---