---
tap: "sendgrid-core"
version: "1"

name: "campaigns"
doc-link: 
singer-schema: https://github.com/singer-io/tap-sendgrid/blob/master/tap_sendgrid/schemas/campaigns.json
description: |
  The `{{ table.name }}` table contains info about all your campaigns.

replication-method: "Key-based Incremental"

replication-key:
  name: "timestamp"

api-method:
  name: "List all campaigns"
  doc-link: "https://sendgrid.com/docs/API_Reference/Web_API_v3/Marketing_Campaigns/campaigns.html#Get-all-Campaigns-GET" 

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The campaign ID."
    # foreign-key-id: "campaign-id"

  - name: "title"
    type: "string"
    description: "The display title of the campaign in the SendGrid Marketing Campaigns UI."

  - name: "subject"
    type: "string"
    description: "The subject of the campaign that recipients will see."

  - name: "sender_id"
    type: "integer"
    description: |
      The ID of the 'sender' identity. Recipients will see this as the "From" on your marketing emails.

  - name: "list_ids"
    type: "array"
    description: "The IDs of the lists the campaign is being sent to."
    subattributes:
      - name: "value"
        type: "integer"
        description: "The list ID."
        foreign-key-id: "list-id"

  - name: "segment_ids"
    type: "array"
    description: "The segment IDs the campaign is being sent to."
    subattributes:
      - name: "value"
        type: "integer"
        description: "The segment ID."
        foreign-key-id: "segment-id"

  - name: "categories"
    type: "array"
    description: "The categories associated with the campaigns."
    subattributes:
      - name: "value"
        type: "string"
        description: "The name of the category."

  - name: "suppression_group_id"
    type: "integer"
    description: "The ID of the suppression group that the marketing email belongs to, allowing recipients to opt-out of emails of this type."
    foreign-key-id: "suppression-group-id"

  - name: "custom_unsubscribe_url"
    type: "string"
    description: "The URL of the custom unsubscribe page provided for customers to unsubscribe from suppression groups."

  - name: "ip_pool"
    type: "string"
    description: "The pool of IPs that the email should be sent from."

  - name: "html_content"
    type: "string"
    description: "The HTML content of the marketing email."

  - name: "plain_content"
    type: "string"
    description: "The plain text content of the marketing email."

  - name: "status"
    type: "string"
    description: "The status of the campaign. For example: `Draft`"
---