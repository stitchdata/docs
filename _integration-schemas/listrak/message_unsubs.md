---
tap: "listrak"
# version: ""

name: "message_unsubs"
doc-link:
singer-schema: https://github.com/singer-io/tap-listrak/blob/master/tap_listrak/schemas/message_unsubs.json
description: |
  The `message_unsubs` table contains info about contacts who requested to be removed from a list from the supplied message.

replication-method: "Full Table"

api-method:
  name: "ReportRangeMessageContactRemoval"
  doc-link: https://webservices.listrak.com/v31/IntegrationService.asmx?op=ReportRangeMessageContactRemoval

attributes:
  - name: "MsgID"
    type: "integer"
    primary-key: true
    description: "The ID of the message that resulted in the unsubscribe."
    foreign-key: true

  - name: "EmailAddress"
    type: "string"
    primary-key: true
    description: "The email address that requested the unsubscribe."

  - name: "ContactID"
    type: "string"
    description: "The ID of the contact who unsubscribed."
    foreign-key: true

  - name: "AdditionDate"
    type: "string"
    description: "The date the contact initially subscribed."

  - name: "RemovalDate"
    type: "string"
    description: "The date the contact unsubscribed."

  - name: "RemovalMethod"
    type: "string"
    description: "The method the contact used to unsubscribe."
---