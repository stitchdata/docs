---
tap: "dixa"
version: "1"
key: ""

name: "messages"
doc-link: "https://docs.dixa.io/openapi/dixa-api/tag/Messages/"
singer-schema: https://github.com/singer-io/tap-dixa/blob/main/tap_dixa/schemas/messages.json
description: |
  The `{{ table.name }}` table contains information about all messages in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
  name: "List messages"
  doc-link: "https://docs.dixa.io/openapi/dixa-api/tag/Messages/"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The message ID."
    foreign-key-id: "message-id"

  - name: "created_at"
    type: "integer"
    replication-key: true
    description: "The date the message was created. Measured in seconds since the Unix epoch."

  - name: "attached_files"
    type: "array"
    description: ""
    subattributes:
      - name: "items"
        type: "string"
        description: ""  

  - name: "author_email"
    type: "string"
    description: ""

  - name: "author_name"
    type: "string"
    description: ""

  - name: "bcc"
    type: "array"
    description: ""
    subattributes:
      - name: "items"
        type: "string"
        description: ""

  - name: "cc"
    type: "array"
    description: ""
    subattributes:
      - name: "items"
        type: "string"
        description: ""      

  - name: "chat_input_answer"
    type: "string"
    description: ""

  - name: "chat_input_question"
    type: "string"
    description: ""

  - name: "chat_menu_text"
    type: "string"
    description: ""

  - name: "created_at_datestring"
    type: "integer"
    description: ""

  - name: "csid"
    type: "integer"
    description: ""

  - name: "direction"
    type: "string"
    description: ""

  - name: "duration"
    type: "integer"
    description: ""

  - name: "from"
    type: "string"
    description: ""

  - name: "from_phone_number"
    type: "string"
    description: ""

  - name: "initial_channel"
    type: "string"
    description: ""

  - name: "is_automated_message"
    type: "boolean"
    description: ""

  - name: "recording_url"
    type: "string"
    description: ""

  - name: "text"
    type: "string"
    description: ""

  - name: "to"
    type: "array"
    description: ""
    subattributes:
      - name: "items"
        type: "string"
        description: ""

  - name: "to_phone_number"
    type: "string"
    description: ""

  - name: "voicemail_url"
    type: "string"
    description: ""
---