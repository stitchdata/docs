---
tap: "eloqua"
version: "1.0"

name: "activity_email_open"
key: "activity-email-open"

doc-link: &doc-link "https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAC/op-api-bulk-2.0-activities-exports-post.html"
description: |
  The `{{ table.name }}` table contains info about `EmailOpen` contact activities.

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
    description: "The type of the activity. This value will be `EmailOpen`."

  - name: "AssetId"
    type: "string"
    description: "The ID of the associated asset."

  - name: "AssetName"
    type: "string"
    description: "The name of the associated asset."

  - name: "AssetType"
    type: "string"
    description: "The type of the associated asset."

  - name: "CampaignId"
    type: "integer"
    description: "The ID of the campaign associated with the activity."
    foreign-key-id: "campaign-id"

  - name: "ContactId"
    type: "string"
    description: "The ID of the contact associated with the activity."
    foreign-key-id: "contact-id"

  - name: "EmailAddress"
    type: "string"
    description: "The email address of the contact who performed the activity."

  - name: "EmailRecipientId"
    type: "string"
    description: "The recipient ID associated with the activity."

  - name: "EmailWebLink"
    type: "string"
    description: "The link for viewing the email in a web browser window for an email activity."

  - name: "ExternalId"
    type: "string"
    description: "The GUID of the visitor who performed the activity."

  - name: "DeploymentId"
    type: "string"
    description: "The ID of the email deployment for an email activity."

  - name: "IpAddress"
    type: "string"
    description: "The IP address of the visitor who performed the activity."

  - name: "Type"
    type: "string"
    description: "The asset's type in {{ integration.display_name }}."

  - name: "VisitorId"
    type: "string"
    description: "The ID of the visitor who performed the activity."

  - name: "VisitorExternalId"
    type: "string"
    description: "The GUID of the visitor who performed the activity."
---