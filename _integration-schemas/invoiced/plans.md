---
tap: "invoiced"
version: "1"

name: "plans"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-invoiced/blob/master/tap_invoiced/schemas/plans.json"
description: |
  The `{{ table.name }}` table contains info about the plans in your {{ integration.display_name }} account. A plan describes a fixed amount that is billed to customers over a recurring interval.

replication-method: "Key-based Incremental"

api-method:
    name: "List all plans"
    doc-link: "https://www.invoiced.com/resources/docs/api/#list-all-plans"

attributes:
  - name: "amount"
    type: "number"
    description: "Plan amount. Not applicable when pricing mode is custom."
  - name: "catalog_item"
    type: "string"
    description: "Item ID the plan belongs to"
  - name: "created_at"
    type: "integer"
    description: "Timestamp when created"
  - name: "currency"
    type: "string"
    description: "3-letter ISO code"
  - name: "description"
    type: "string"
    description: ""
  - name: "id"
    type: "string"
    description: "The plan’s unique ID"
    primary-key: true
  - name: "interval"
    type: "string"
    description: "One of day, week, month, year. The frequency with which a subscription should be billed."
  - name: "interval_count"
    type: "integer"
    description: "The number of intervals between each subscription billing. Defaults to 1."
  - name: "metadata"
    type: "object"
    description: "A hash of key/value pairs that can store additional information about this object."
  - name: "name"
    type: "string"
    description: "Plan name"
  - name: "notes"
    type: "string"
    description: ""
  - name: "object"
    type: "string"
    description: "Object type, plan"
  - name: "pricing_mode"
    type: "string"
    description: "per_unit, volume, tiered or custom"
  - name: "quantity_type"
    type: "string"
    description: "constant or usage"
  - name: "tiers"
    type: "object"
    description: ""
  - name: "updated_at"
    type: "integer"
    description: "Timestamp when updated"
    replication-key: true
---