---
tap: "klaviyo"
version: "1"
key: "campaign"

name: "campaigns"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-klaviyo/blob/master/tap_klaviyo/schemas/campaigns.json"
description: |
  The {{ table.name }} table contains info about the campaigns in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
  name: "Get campaigns"
  doc-link: "https://apidocs.klaviyo.com/reference/campaigns#get-campaigns"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The campaign ID."

  - name: "campaign_type"
    type: "string"
    description: ""

  - name: "created"
    type: "string"
    description: ""

  - name: "excluded_lists"
    type: "array"
    description: ""
    subattributes: &lists
      - name: "id"
        type: "string"
        primary-key: true
        description: "The list ID."
        foreign-key-id: "list-id"

      - name: "created"
        type: "string"
        description: ""

      - name: "name"
        type: "string"
        description: ""
      
      - name: "object"
        type: "string"
        description: ""
      
      - name: "person_count"
        type: "integer"
        description: ""
      
      - name: "type"
        type: "string"
        description: ""
      
      - name: "updated"
        type: "string"
        description: ""

  - name: "from_email"
    type: "string"
    description: ""

  - name: "from_name"
    type: "string"
    description: ""

  - name: "is_segmented"
    type: "boolean"
    description: ""

  - name: "list_id"
    type: "string"
    description: ""

  - name: "lists"
    type: "array"
    description: ""
    subattributes: *lists

  - name: "message_type"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "num_recipients"
    type: "integer"
    description: ""

  - name: "object"
    type: "string"
    description: ""

  - name: "send_time"
    type: "date-time"
    description: ""

  - name: "sent_at"
    type: "date-time"
    description: ""

  - name: "status_id"
    type: "integer"
    description: ""

  - name: "status_label"
    type: "string"
    description: ""
  
  - name: "subject"
    type: "string"
    description: ""
  
  - name: "template"
    type: "object"
    description: ""
    subattributes:
      - name: "object"
        type: "string"
        description: ""
        
      - name: "id"
        type: "string"
        description: ""
        
      - name: "html"
        type: "string"
        description: ""
  
  - name: "template_id"
    type: "string"
    description: ""

  - name: "type"
    type: "string"
    description: ""
  
  - name: "updated"
    type: "string"
    description: ""
---