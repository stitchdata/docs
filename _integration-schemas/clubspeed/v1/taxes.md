---
tap: "clubspeed"
version: "1.0"

name: "taxes"
singer-schema: "https://github.com/singer-io/tap-clubspeed/blob/master/tap_clubspeed/schemas/taxes.json"
description: |
  The `{{ table.name }}` table contains info about tax calculations, which are typically applied to [`products`](#products).

replication-method: "Full Table"

attributes:
  - name: "taxId"
    type: "integer"
    primary-key: true
    description: "The tax ID."
    foreign-key-id: "tax-id"

  - name: "amount"
    type: "number"
    description: "The percentage of the tax. For example: `6.25` would indicate `6.25%`."

  - name: "deleted"
    type: "boolean"
    description: "Indicates whether the tax has been soft deleted."

  - name: "description"
    type: "string"
    description: "The description of the tax."

  - name: "gst"
    type: "number"
    description: "The percentage of the tax which should be considered GST, where applicable."
---