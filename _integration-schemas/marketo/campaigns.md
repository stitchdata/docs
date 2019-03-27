---
tap: "marketo"
version: "2.0"

name: "campaigns"
doc-link: 
singer-schema: https://github.com/singer-io/tap-marketo/blob/master/tap_marketo/schemas/campaigns.json
description: |
  The `{{ table.name }}` table contains info about the campaigns in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"
api-method:
  name: "getCampaigns"
  doc-link: http://developers.marketo.com/rest-api/endpoint-reference/lead-database-endpoint-reference/#!/Campaigns/getCampaignsUsingGET

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The ID of the campaign."
    # foreign-key-id: "campaign-id"

  - name: "updatedAt"
    type: "date-time"
    replication-key: true
    description: "The time the campaign was most recently updated."

  - name: "createdAt"
    type: "date-time"
    description: "The time the campaign was created."

  - name: "active"
    type: "boolean"
    description: "Indicates if the campaign is active. Applicable only to trigger campaigns."

  - name: "description"
    type: "string"
    description: "The description of the Smart campaign."

  - name: "name"
    type: "string"
    description: "The name of the Smart campaign."

  - name: "programId"
    type: "integer"
    description: "The ID of the parent program, if applicable."
    foreign-key-id: "program-id"

  - name: "programName"
    type: "string"
    description: "The name of the parent program, if applicable."

  - name: "type"
    type: "string"
    description: "The type of Smart campaign. Possible values are `batch` or `trigger`."

  - name: "workspaceName"
    type: "string"
    description: "The name of the parent workspace, if applicable."
---