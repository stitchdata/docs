---
tap: "listrak"
# version: ""

name: "message_sends"
doc-link:
singer-schema: https://github.com/singer-io/tap-listrak/blob/master/tap_listrak/schemas/message_sends.json
description: |
  The `message_sends` table contains info about contacts who were sent the specified message.

replication-method: "Full Table"

api-method:
  name: "ReportMessageContactSent"
  doc-link: https://webservices.listrak.com/v31/IntegrationService.asmx?op=ReportMessageContactSent 

attributes:
- name: "MsgID"
    type: "integer"
    description: ""

  - name: "EmailAddress"
    type: "string"
    description: ""
