---
tap: "ringcentral"
version: "1.0"
key: ""

name: "call_log"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-ringcentral/blob/master/tap_ringcentral/schemas/call_log.json"
description: |
  The `{{ table.name }}` contains info about your call logs.

replication-method: "Key-based Incremental"

replication-key:
  name: "dateFrom : dateTo"

api-method:
    name: "Get User Call Log Records"
    doc-link: "https://developers.ringcentral.com/api-reference/Call-Log/readUserCallLog"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The call log record ID."

  - name: "_contact_id"
    type: "integer"
    description: ""
    foreign-key-id: "contact-id"

  - name: "action"
    type: "string"
    description: "The type of call operation."

  - name: "deleted"
    type: "anything"
    description: "Deleted calls. This value will return 'True' only if a call was deleted."

  - name: "direction"
    type: "string"
    description: "The call direction - inbound or outbound."

  - name: "duration"
    type: "integer"
    description: "The duration of the call recorded, in seconds."

  - name: "extension"
    type: "object"
    description: "The extension of the person a call was made on behalf of."
    subattributes:
      - name: "id"
        type: "integer"
        description: "The internal ID of the caller extension."

      - name: "uri"
        type: "string"
        description: "The link to the extension."

  - name: "from"
    type: "object"
    description: "The caller."
    subattributes:
      - name: "extensionId"
        type: "string"
        description: "The internal extension ID."

      - name: "location"
        type: "string"
        description: "The city of the caller's area code, if the phoneNumber field is not empty."

      - name: "name"
        type: "string"
        description: "The name of the caller."

      - name: "phoneNumber"
        type: "string"
        description: "The caller's phone number."

  - name: "message"
    type: "anything"
    description: "The linked voicemail/fax message."
    subattributes:
      - name: "id"
        type: "string"
        description: "The message ID."
        foreign-key-id: "message-id"

      - name: "type"
        type: "string"
        description: "The type of the message."

      - name: "uri"
        type: "string"
        description: "Link to the message resource."

  - name: "reason"
    type: "anything"
    description: "The reason of a call result."

  - name: "reasonDescription"
    type: "anything"
    description: ""

  - name: "result"
    type: "string"
    description: "The status of the call operation."

  - name: "sessionId"
    type: "string"
    description: "The call session ID."
    foreign-key-id: "session-id"

  - name: "startTime"
    type: "date-time"
    description: "The start datetime of a call. This value is in ISO 8601 format, including the timezone."

  - name: "to"
    type: "object"
    description: "The callee."
    subattributes:
      - name: "extensionId"
        type: "string"
        description: "The internal extension ID."

      - name: "location"
        type: "string"
        description: "The city of the callee's area code, if the phoneNumber field is not empty."

      - name: "name"
        type: "string"
        description: "The name of the callee."

      - name: "phoneNumber"
        type: "string"
        description: "The callee's phone number."

  - name: "type"
    type: "string"
    description: "The call type - voice or fax."

  - name: "uri"
    type: "string"
    description: "The canonical URI of a call log record."
---