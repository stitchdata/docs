---
tap: "sailthru"
version: "0.2"
key: ""

name: "lists"
doc-link: "https://getstarted.sailthru.com/audience/managing-lists/lists-overview/"
singer-schema: "https://github.com/singer-io/tap-sailthru/blob/master/tap_sailthru/schemas/lists.json"
description: |
  The `{{ table.name }}` table contains basic information about lists in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
    name: "get Lists"
    doc-link: "https://getstarted.sailthru.com/developers/api/list/"

attributes:
  - name: "list_id"
    type: "string"
    primary-key: true
    description: "The list ID."
    #foreign-key-id: "list-id"

  - name: "create_time"
    type: "date-time"
    description: ""
  - name: "email_count"
    type: "integer"
    description: ""
  
  - name: "name"
    type: "string"
    description: ""
  - name: "type"
    type: "string"
    description: ""
  - name: "valid_count"
    type: "integer"
    description: ""
---
