---
tap: "outreach"
version: "1"
key: "call-disposition"

name: "call_dispositions"
doc-link: "https://api.outreach.io/api/v2/docs#callDisposition"
singer-schema: "https://github.com/singer-io/tap-outreach/blob/master/tap_outreach/schemas/call_dispositions.json"
description: |
  The `{{ table.name}}` table contains information about call dispositions from your call log in {{ integration.display_name }}.

replication-method: "Key-based Incremental"

api-method:
  name: "Get call dispositions"
  doc-link: "https://api.outreach.io/api/v2/docs#callDisposition"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The call disposition ID."
    #foreign-key-id: "disposition-id"

  - name: "updatedAt"
    type: "date-time"
    replication-key: true 
    description: "The time the call disposition was last updated." 

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
  - name: "outcome"
    type: "string"
    description: ""
---