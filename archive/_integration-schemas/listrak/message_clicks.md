---
tap: "listrak"
version: "1"

name: "message_clicks"
doc-link:
singer-schema: https://github.com/singer-io/tap-listrak/blob/master/tap_listrak/schemas/message_clicks.json
description: |
  The `{{ table.name }}` table contains info about contact clicks for a message.

replication-method: "Full Table"

api-method:
  name: "ReportRangeMessageContactClick"
  doc-link: https://webservices.listrak.com/v31/IntegrationService.asmx?op=ReportRangeMessageContactClick

attributes:
  - name: "MsgID"
    type: "integer"
    primary-key: true
    description: "The message ID that contains the link that was clicked."
    foreign-key-id: "message-id"

  - name: "EmailAddress"
    type: "string"
    primary-key: true
    description: "The email address of the contact who clicked the link."

  - name: "ContactID"
    type: "string"
    description: "The ID of the contact who clicked the link."
    foreign-key-id: "contact-id"

  - name: "LinkUrl"
    type: "string"
    description: "The URL of the link."

  - name: "ClickDate"
    type: "string"
    description: "The date the contact clicked the link."

  - name: "LinkDescription"
    type: "string"
    description: "A description of the link."
---