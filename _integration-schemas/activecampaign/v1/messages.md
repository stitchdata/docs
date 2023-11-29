---
tap: "activecampaign"
version: "1"
key: ""

name: "messages"
doc-link: "https://developers.activecampaign.com/reference#messages"
singer-schema: "https://github.com/singer-io/tap-activecampaign/blob/master/tap_activecampaign/schemas/messages.json"
description: |
  The `{{ table.name }}` table contains information about messages for campaigns in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: "List all messages"
    doc-link: "https://developers.activecampaign.com/reference#list-all-messages"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The message ID."
    foreign-key-id: "message-id"

  - name: "mdate"
    type: "date-time"
    description: "The time the message was last modified."
    replication-key: true

  - name: "cdate"
    type: "date-time"
    description: ""
  - name: "charset"
    type: "string"
    description: ""
  - name: "ed_instanceid"
    type: "integer"
    description: ""
  - name: "ed_version"
    type: "integer"
    description: ""
  - name: "encoding"
    type: "string"
    description: ""
  - name: "format"
    type: "string"
    description: ""
  - name: "fromemail"
    type: "string"
    description: ""
  - name: "fromname"
    type: "string"
    description: ""
  - name: "hidden"
    type: "integer"
    description: ""
  - name: "html"
    type: "string"
    description: ""
  - name: "htmlfetch"
    type: "string"
    description: ""
  
  - name: "name"
    type: "string"
    description: ""
  - name: "preheader_text"
    type: "string"
    description: ""
  - name: "preview_data"
    type: "string"
    description: ""
  - name: "preview_mime"
    type: "string"
    description: ""
  - name: "priority"
    type: "integer"
    description: ""
  - name: "reply2"
    type: "string"
    description: ""
  - name: "subject"
    type: "string"
    description: ""
  - name: "text"
    type: "string"
    description: ""
  - name: "textfetch"
    type: "string"
    description: ""
  - name: "user"
    type: "integer"
    description: ""
  - name: "userid"
    type: "integer"
    description: "The user ID."
    foreign-key-id: "user-id"
---