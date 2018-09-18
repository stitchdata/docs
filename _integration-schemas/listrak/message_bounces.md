---
tap: "listrak"
# version: ""

name: "message_bounces"
doc-link:
singer-schema: https://github.com/singer-io/tap-listrak/blob/master/tap_listrak/schemas/message_bounces.json
description: |
  The `message_bounces` table contains info about contact bounces for a message.

replication-method: "Full Table"

api-method:
  name: "ReportRangeMessageContactBounces"
  doc-link: https://webservices.listrak.com/v31/IntegrationService.asmx?op=ReportRangeMessageContactBounces

attributes:
  - name: "MsgID"
    type: "integer"
    primary-key: true
    description: "The ID of the message that bounced."
    foreign-key-id: "message-id"

  - name: "EmailAddress"
    type: "string"
    primary-key: true
    description: "The email address associated with the bounce."

  - name: "ContactID"
    type: "string"
    description: "The ID of the contact that the bounced message was sent to."
    foreign-key-id: "contact-id"

  - name: "BounceReason"
    type: "string"
    description: "An explanation for the reason for the bounce."

  - name: "BounceDetail"
    type: "string"
    description: "Additional detail about the bounce."

  - name: "BounceDate"
    type: "string"
    description: "The date that the bounce occurred."

  - name: "BounceCount"
    type: "integer"
    description: "The number of bounces for the message."
---