---
tap: "listrak"
# version: ""

name: "message_clicks"
doc-link:
singer-schema: https://github.com/singer-io/tap-listrak/blob/master/tap_listrak/schemas/message_clicks.json
description: |
  The `message_clicks` table contains info about contact clicks for a message.

replication-method: "Full Table"

api-method:
  name: "ReportRangeMessageContactClick"
  doc-link: https://webservices.listrak.com/v31/IntegrationService.asmx?op=ReportRangeMessageContactClick

attributes:
  - name: "MsgID"
    type: "integer"
    description: ""

  - name: "ContactID"
    type: "string"
    description: ""

  - name: "EmailAddress"
    type: "string"
    description: ""

  - name: "LinkUrl"
    type: "string"
    description: ""

  - name: "ClickDate"
    type: "string"
    description: ""

  - name: "LinkDescription"
    type: "string"
    description: ""
