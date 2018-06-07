---
tap: "listrak"
# version: ""

name: "message bounces"
doc-link:
singer-schema: https://github.com/singer-io/tap-listrak/blob/master/tap_listrak/schemas/message_bounces.json
description: |
  The `message_bounces` table contains info about contact bounces for a message.

api-method:
  name: "ReportRangeMessageContactBounces"
  doc-link: https://webservices.listrak.com/v31/IntegrationService.asmx?op=ReportRangeMessageContactBounces

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

  - name: "BounceReason"
    type: "string"
    description: ""

  - name: "BounceDetail"
    type: "string"
    description: ""

  - name: "BounceDate"
    type: "string"
    description: ""

  - name: "BounceCount"
    type: "integer"
    description: ""
