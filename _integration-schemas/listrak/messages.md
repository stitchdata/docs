---
tap: "listrak"
# version: ""

name: "messages"
doc-link:
singer-schema: https://github.com/singer-io/tap-listrak/blob/master/tap_listrak/schemas/messages.json
description: |
  The `messages` table contains info about message statistics.

replication-method: "Full Table"

api-method:
  name: "ReportListMessageActivity"
  doc-link: https://webservices.listrak.com/v31/IntegrationService.asmx?op=ReportListMessageActivity

attributes:
- name: "ClickCount"
    type: "integer"
    description: ""

  - name: "SendDate"
    type: "string"
    description: ""

  - name: "OrderTotal"
    type: "number"
    description: ""

  - name: "RemovePercent"
    type: "number"
    description: ""

  - name: "RemoveCount"
    type: "integer"
    description: ""

  - name: "ClickerPercent"
    type: "number"
    description: ""

  - name: "DeliverCount"
    type: "integer"
    description: ""

  - name: "ReadCount"
    type: "integer"
    description: ""

  - name: "Subject"
    type: "string"
    description: ""

  - name: "ConversionCount"
    type: "integer"
    description: ""

  - name: "ListID"
    type: "integer"
    description: ""

  - name: "NewClickerCount"
    type: "integer"
    description: ""

  - name: "OpenCount"
    type: "integer"
    description: ""

  - name: "OpenPercent"
    type: "number"
    description: ""

  - name: "RepeatClickerCount"
    type: "integer"
    description: ""

  - name: "MsgID"
    type: "integer"
    description: ""

  - name: "ClickerCount"
    type: "integer"
    description: ""

  - name: "ReadPercent"
    type: "number"
    description: ""

  - name: "AverageOrderValue"
    type: "number"
    description: ""

Wrote out.md to the current directory!
