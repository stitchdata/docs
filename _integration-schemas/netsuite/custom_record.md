---
tap: "netsuite"
version: "1.0"

name: "customrecord_[custom_record_name]"
doc-link: "https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/customrecord.html"
# singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/Transaction.json"
description: |
  For each custom record type in {{ integration.display_name }}, a table for that custom record type will be available for selection in Stitch.

  Custom record tables are named `{{ table.name }}`, where `[custom_record_name]` is the value of the ID field in the Custom Record Setup page in {{ integration.display_name }}.

  For example: If a custom record were named `promo discount` in {{ integration.display_name }}, the corresponding table for those records would be named `{{ table.name | replace: "[custom_record_name]","promo_discount" }}`. If the ID field in the Custom Record Setup page is left blank, {{ integration.display_name }} will auto-assign a numerical ID to the record. In Stitch, the table for the custom record would then be something like `customrecord_123`, where `123` is the ID auto-assigned by {{ integration.display_name }}.

  **Note**: The Replication Method Stitch uses to replicate custom record types depends on how custom records are configured in {{ integration.display_name }}. Refer to the [Custom records](#custom-records) section for more info.

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "custom-record"

replication-method: "Key-based Incremental"

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

      **Note**: This field will only contain values if the custom record type has **Show Last Modified** enabled in {{ integration.display_name }}. Refer to the [Custom records](#custom-records) section for more info.

  - name: "Fields selected by you"
    description: |
      Custom record tables will contain the same attributes of the custom record type in {{ integration.display_name }}. The table schema for custom record types will vary depending on the attributes you set to replicate in Stitch.
---