---
tap: "activecampaign"
version: "1"
key: ""

name: "saved_responses"
doc-link: "https://developers.activecampaign.com/reference#saved-responses-1"
singer-schema: "https://github.com/singer-io/tap-activecampaign/blob/master/tap_activecampaign/schemas/saved_responses.json"
description: |
  The `{{ table.name }}` table contains information about email response templates in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: "List all saved responses"
    doc-link: "https://developers.activecampaign.com/reference#list-all-saved-responses"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The saved response ID."
    #foreign-key-id: "saved-response-id"

  - name: "mdate"
    type: "date-time"
    description: "The time the response was last modified."
    replication-key: true

  - name: "body"
    type: "string"
    description: ""
  - name: "cdate"
    type: "date-time"
    description: ""
  
  - name: "last_sent_user_id"
    type: "integer"
    description: "The user ID of the last sent response."
    foreign-key-id: "user-id"
  - name: "ldate"
    type: "date-time"
    description: ""

  - name: "subject"
    type: "string"
    description: ""
  - name: "title"
    type: "string"
    description: ""
---
