---
tap: "ringcentral"
version: "1.0"
key: ""

name: "messages"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-ringcentral/blob/master/tap_ringcentral/schemas/messages.json"
description: |
  The `{{ table.name }}` contains info about an extension mailbox's messages.

replication-method: "Key-based Incremental"

replication-key:
  name: "dateFrom : dateTo"

api-method:
    name: "Get Message List"
    doc-link: "https://developers.ringcentral.com/api-reference/Message-Store/listMessages"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The message ID."

  - name: "_contact_id"
    type: "integer"
    description: ""
    foreign-key-id: "contact-id"

  - name: "attachments"
    type: "anything"
    description: "The list of message attachments."

  - name: "availability"
    type: "string"
    description: "The message availability status."

  - name: "conversation"
    type: "anything"
    description: ""

  - name: "conversationId"
    type: "anything"
    primary-key: true
    description: "The conversation ID."


  - name: "coverIndex"
    type: "integer"
    description: ""

  - name: "creationTime"
    type: "date-time"
    description: "The datetime of when the message was created. This value is in ISO 8601 format, including the timezone."

  - name: "deleted"
    type: "anything"
    description: ""

  - name: "direction"
    type: "string"
    description: "The direction of the message - inbound or outbound."

  - name: "faxPageCount"
    type: "integer"
    description: "The page count of a fax message."

  - name: "faxResolution"
    type: "string"
    description: "The resolution of a fax message - high or low."

  - name: "from"
    type: "anything"
    description: "The sender's information."

  - name: "lastModifiedTime"
    type: "date-time"
    description: "The datetiime of when the messase was last modified. This value is in ISO 8601 format, including the timezone."

  - name: "messageStatus"
    type: "string"
    description: "The message's delivery status."

  - name: "priority"
    type: "string"
    description: "The message priority - normal or high."

  - name: "readStatus"
    type: "string"
    description: "The read status of a message - read or undread."

  - name: "smsSendingAttemptsCount"
    type: "anything"
    description: "The number of attempts made to send an outbout SMS."

  - name: "subject"
    type: "anything"
    description: "The message subject."

  - name: "to"
    type: "anything"
    description: "The recipeient's information."

  - name: "type"
    type: "string"
    description: "The message type."

  - name: "uri"
    type: "string"
    description: ""

  - name: "vmTranscriptionStatus"
    type: "anything"
    description: ""
---