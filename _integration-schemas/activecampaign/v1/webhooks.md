---
tap: "activecampaign"
version: "1"
key: ""

name: "webhooks"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-activecampaign/blob/master/tap_activecampaign/schemas/webhooks.json"
description: |
  The `{{ table.name }}` table contains information about real-time updates about your contact and campaign activity in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
    name: "List all webhooks"
    doc-link: "https://developers.activecampaign.com/reference#get-a-list-of-webhook-events"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The webhook ID."
    #foreign-key-id: "webhook-id"

  - name: "cdate"
    type: "date-time"
    description: ""
  - name: "events"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""
    description: ""
 
  - name: "listid"
    type: "integer"
    description: "The list ID."
    foreign-key-id: "list-id"
  - name: "name"
    type: "string"
    description: ""
  - name: "sources"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""
  - name: "url"
    type: "string"
    description: ""
---
