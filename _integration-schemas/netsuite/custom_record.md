---
tap: "netsuite"
version: "1.0"

name: "customrecord_[custom_record_type]"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/Transaction.json"
description: |
  For each custom record type in {{ integration.display_name }}, a table for that custom record type will be available for selection in Stitch.

  Custom record tables are named `{{ table.name }}`, where `[custom_record_type]` is the name of the custom record in {{ integration.display_name }}. For example: If a custom record were named `promo discount` in {{ integration.display_name }}, the corresponding table for those records would be named `{{ table.name | replace: "[custom_record_type]","promo_discount" }}`.

replication-method: "Key-based Incremental"

api-method:
    name: ""
    doc-link: ""

attributes:
  - name: "internalId"
    type: "integer"
    primary-key: true
    description: "The unique ID for the record."

  - name: "lastModifiedDate"
    type: "date-time"
    replication-key: true
    description: |
      The time the record was last updated.

  - name: "Fields selected by you"
    description: |
      Custom record tables will contain the same attributes of the custom record type in {{ integration.display_name }}. The table schema for custom record types will vary depending on the attributes you set to replicate in Stitch.
---