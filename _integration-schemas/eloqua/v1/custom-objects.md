---
tap: "eloqua"
version: "1.0"

name: "Custom Objects"
key: "custom-objects"

doc-link: &doc-link "https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAC/op-api-bulk-2.0-customobjects-parentid-exports-post.html"
description: |
  For each custom object in your {{ integration.display_name }} account, Stitch will display a table as available for selection. The name of the table will be the normalized name of the object, using snake case (spaces replaced with underscores) and removing special characters. For example: If your account contains an `Enrichement Attributes` custom object, there will be a corresponding `enrichment_attributes` available for selection in Stitch.

  **Note**: This table is replicated using the {{ integration.display_name }} Bulk API.

replication-method: "Key-based Incremental"

api-method:
    name: "Bulk: Create an export definition for a custom object"
    doc-link: *doc-link

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The custom object ID."

  - name: "UpdatedAt"
    type: "date-time"
    replication-key: true
    description: "The Unix timestamp for the date and time the record was last updated."

  - name: "CreatedAt"
    type: "date-time"
    description: "The date and time the record was created, expressed in Unix time."

  - name: "DataCardIDExt"
    type: "string"
    description: ""

  - name: "Custom Fields"
    type: "varies"
    description: |
      The fields associated with the custom object in your {{ integration.display_name }} account.
---