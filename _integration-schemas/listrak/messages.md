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
  - name: "MsgID"
    type: "integer"
    primary-key: true
    description: "The message ID."
    foreign-key-id: "message-id"

  - name: "AverageOrderValue"
    type: "number"
    description: "The average order value associated with the message."

  - name: "ClickCount"
    type: "integer"
    description: "The current number of clicks for the message."

  - name: "ClickerCount"
    type: "integer"
    description: "The current number of contacts who clicked for the message."

  - name: "ClickerPercent"
    type: "number"
    description: "The percent of contacts who clicked the message."

  - name: "ConversionCount"
    type: "integer"
    description: "The current number of conversions for the message."

  - name: "DeliverCount"
    type: "integer"
    description: "The current number of messages delivered."

  - name: "ListID"
    type: "integer"
    description: "The ID of the list the message was sent to."
    foreign-key-id: "list-id"

  - name: "NewClickerCount"
    type: "integer"
    description: "The current number of new clickers for the message."

  - name: "OpenCount"
    type: "integer"
    description: "The current number of opens for the message."

  - name: "OpenPercent"
    type: "number"
    description: "The percentage of contacts who opened the message."

  - name: "OrderTotal"
    type: "number"
    description: "The order total associated with the message."

  - name: "ReadCount"
    type: "integer"
    description: "The current number of reads for the message."

  - name: "ReadPercent"
    type: "number"
    description: "The percentage of contacts who read the message."

  - name: "RemovePercent"
    type: "number"
    description: "The percentage of contacts who unsubscribed as a result of the message."

  - name: "RemoveCount"
    type: "integer"
    description: "The current number of unsubscribes for the message."

  - name: "RepeatClickerCount"
    type: "integer"
    description: "The current number of contacts who clicked multiple times for the message."

  - name: "SendDate"
    type: "string"
    description: "The date the message was sent."

  - name: "Subject"
    type: "string"
    description: "The subject of the message."
---