---
tap: "saasoptics"
version: "1"
key: "billing-description"

name: "billing_descriptions"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-saasoptics/blob/master/tap_saasoptics/schemas/billing_descriptions.json"
description: |
  The `{{ table.name }}` table contains info about billing line item descriptions.

replication-method: "Full Table"

api-method:
  name: "Billing Line Item Descriptions List"
  doc-link: "https://saasoptics.zendesk.com/hc/en-us/articles/115013751807-Billing-Line-Item-Descriptions-R-"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: ""
    # foreign-key-id: "billing-description-id"

  - name: "contents"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "notes"
    type: "string"
    description: ""
---