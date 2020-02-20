---
tap: "eloqua"
version: "1"

name: "activity_web_visit"
key: "activity-web-visit"

doc-link: &doc-link "https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAC/op-api-bulk-2.0-activities-exports-post.html"
description: |
  The `{{ table.name }}` table contains info about `WebVisit` contact activities.

  **Note**: This table is replicated using the {{ integration.display_name }} Bulk API.
  
replication-method: "Key-based Incremental"

api-method:
    name: "Bulk: Create an activity export definition"
    doc-link: *doc-link

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The activity ID."
    foreign-key-id: "activity-id"

  - name: "updatedAt"
    type: "date-time"
    replication-key: true
    description: "The Unix timestamp for the date and time the activity was last updated."

  - name: "ActivityDate"
    type: "date-time"
    description: "The date the activity was performed expressed in 10 digit integer Unix time."

  - name: "ActivityType"
    type: "string"
    description: |
      The type of the activity. The value of this field will correspond with the suffix in the table's name. For example: If the table is named`{{ table.name }}`, this value would be `WebVisit`.

  - name: "AssetId"
    type: "string"
    description: "The ID of the associated asset."

  - name: "AssetType"
    type: "string"
    description: "The type of the associated asset."

  - name: "ContactId"
    type: "string"
    description: "The ID of the contact associated with the activity."
    foreign-key-id: "contact-id"

  - name: "Type"
    type: "string"
    description: "The asset's type in {{ integration.display_name }}."
---