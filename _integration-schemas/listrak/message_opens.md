---
tap: "listrak"
# version: ""

name: "message_opens"
doc-link:
singer-schema: https://github.com/singer-io/tap-listrak/blob/master/tap_listrak/schemas/message_opens.json
description: |
  The `message_opens` table contains info about contact opens for a message.

replication-method: "Full Table"

api-method:
  name: "ReportRangeMessageContactOpen"
  doc-link: https://webservices.listrak.com/v31/IntegrationService.asmx?op=ReportRangeMessageContactOpen

attributes:
- name: "MsgID"
    type: "integer"
    description: ""

  - name: "OpenDate"
    type: "string"
    description: ""

  - name: "EmailAddress"
    type: "string"
    description: ""

  - name: "ContactID"
    type: "string"
    description: ""

Wrote out.md to the current directory!
