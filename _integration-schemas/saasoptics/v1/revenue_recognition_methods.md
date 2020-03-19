---
tap: "saasoptics"
version: "1"
key: "revenue-recognition-method"

name: "revenue_recognition_methods"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-saasoptics/blob/master/tap_saasoptics/schemas/revenue_recognition_methods.json"
description: |
  The `{{ table.name }}` table contains info about revenue recognition methods, which are the methods for calculating and generating revenue records for a transaction.

replication-method: "Full Table"

api-method:
  name: "Revenue Recognition Methods List"
  doc-link: "https://saasoptics.zendesk.com/hc/en-us/articles/115003617774-Revenue-Recognition-Methods-R-"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: ""
    foreign-key-id: "revenue-recognition-method-id"

  - name: "name"
    type: "string"
    description: ""
---