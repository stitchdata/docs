---
tap: "eloqua"
version: "1.0"

name: "activity_email_clickthrough"
key: "activity-email-clickthrough"

doc-link: &doc-link "https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAC/op-api-bulk-2.0-activities-exports-post.html"
description: |
  The `{{ table.name }}` table contains info about `EmailClickthrough` contact activities.

  **Note**: This table is replicated using the {{ integration.display_name }} Bulk API.

replication-method: "Key-based Incremental"

api-method:
    name: "Bulk: Create an activity export definition"
    doc-link: *doc-link

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The email clickthrough activity ID."
    foreign-key-id: "activity-id"

  - name: "updatedAt"
    type: "date-time"
    replication-key: true
    description: "The Unix timestamp for the date and time the activity was last updated."

  - name: "ActivityDate"
    type: "date-time"
    description: "The date the activity was performed expressed in 10 digit integer Unix time."

  - name: "ActivityId"
    type: "string"
    description: "The unique identifier of the activity per activity type."

  - name: "ActivityType"
    type: "string"
    description: "The type of the activity. This value will be `EmailClickthrough`."

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

  - name: "EmailClickedThruLink"
    type: "string"
    description: "The link clicked through for an activity."

  - name: "EmailRecipientId"
    type: "string"
    description: "The recipient ID associated with the activity."

  - name: "EmailSendType"
    type: "string"
    description: |
      The type of email send for an email activity. Possible values include: 

      - `BatchWizard`
      - `Quicksend`
      - `SOAPAPI`
      - `Salestools`
      - `FormProcessingStep`
      - `DCOServicesStep`
      - `ExternalTest`
      - `TestCenter`
      - `Deliverability`
      - `LowVolumeAPI`
      - `Campaign`

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

  - name: "SubjectLine"
    type: "string"
    description: "The subject line for an email activity."

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