---
tap: "iterable"
version: "1"
key: ""

name: "campaigns"
doc-link: https://api.iterable.com/api/docs#campaigns_campaigns
singer-schema: https://github.com/singer-io/tap-iterable/tree/master/tap_iterable/schemas/campaigns.json
description: |
  The **{{ table.name }}** table contains information about campaigns in your {{ integration.display_name }} projcect.

replication-method: "Key-based Incremental"

api-method:
  name: "Get campaigns"
  doc-link: "https://api.iterable.com/api/docs#campaigns_campaigns"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The campaign ID."
    foreign-key-id: "campaign-id"

  - name: "updatedAt"
    type: "date-time"
    replication-key: true
    description: "The time the campaign was updated."  

  - name: "campaignState"
    type: "string"
    description: ""

  - name: "createdAt"
    type: "date-time"
    description: ""

  - name: "createdByUserId"
    type: "string"
    description: ""

  - name: "endedAt"
    type: "date-time"
    description: ""

  - name: "labels"
    type: "array"
    description: ""
    subattributes:
      - name: "items"
        type: ""
        description: ""

  - name: "listIds"
    type: "array"
    description: ""
    subattributes:
      - name: "items"
        type: "integer"
        description: ""

  - name: "messageMedium"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "recurringCampaignId"
    type: "integer"
    description: ""

  - name: "sendSize"
    type: "number"
    description: ""

  - name: "startAt"
    type: "date-time"
    description: ""

  - name: "suppressionListIds"
    type: "array"
    description: ""
    subattributes:
      - name: "items"
        type: "integer"
        description: ""

  - name: "templateId"
    type: "integer"
    description: "The template ID."
    foreign-key-id: "template-id"

  - name: "type"
    type: "string"
    description: ""

  - name: "updatedByUserId"
    type: "string"
    description: ""

  - name: "workflowId"
    type: "integer"
    description: ""

---
