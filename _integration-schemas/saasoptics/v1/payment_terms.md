---
tap: "saasoptics"
version: "1"
key: "payment-terms"

name: "payment_terms"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-saasoptics/blob/master/tap_saasoptics/schemas/payment_terms.json"
description: |
  The `{{ table.name }}` table contains info about invoice payment terms. 

replication-method: "Full Table"

api-method:
  name: "Payment Terms List"
  doc-link: "https://saasoptics.zendesk.com/hc/en-us/articles/115003642673-Payment-Terms-R-"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: ""

  - name: "intacct_id"
    type: "string"
    description: ""

  - name: "intacct_modified"
    type: "date-time"
    description: ""

  - name: "intacct_recordno"
    type: "integer"
    description: ""

  - name: "is_active"
    type: "boolean"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "netsuite_id"
    type: "string"
    description: ""

  - name: "num_days"
    type: "number"
    description: ""
---