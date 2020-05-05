---
tap: "outreach"
version: "1"
key: "call-purpose"

name: "call_purposes"
doc-link: "https://api.outreach.io/api/v2/docs#callPurpose"
singer-schema: "https://github.com/singer-io/tap-outreach/blob/master/tap_outreach/schemas/call_purposes.json"
description: |
  The `{{ table.name}}` table contains information about the purpose of calls in your {{ integration.display_name }} call logs.

replication-method: "Key-based Incremental"

api-method:
  name: "Get call purposes"
  doc-link: "https://api.outreach.io/api/v2/docs#callPurpose"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The call purpose ID."
    #foreign-key-id: "purpose-id"

  - name: "updatedAt"
    type: "date-time"
    replication-key: true
    description: "The time the call purpose was last updated."

  - name: "createdAt"
    type: "date-time"
    description: ""
  - name: "creatorId"
    type: "integer"
    description: ""
  - name: "name"
    type: "string"
    description: ""
  - name: "order"
    type: "integer"
    description: ""
---