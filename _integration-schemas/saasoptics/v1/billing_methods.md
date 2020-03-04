---
tap: "saasoptics"
version: "1"
key: "billing-method"

name: "billing_methods"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-saasoptics/blob/master/tap_saasoptics/schemas/billing_methods.json"
description: |
  The `{{ table.name }}` table contains info about billing methods, which are used to specify billing/invoice frequencies for transactions in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
  name: "Billing Methods List"
  doc-link: "https://saasoptics.zendesk.com/hc/en-us/articles/115003604433-Billing-Methods-R-"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: ""
    foreign-key-id: "billing-method-id"

  - name: "name"
    type: "string"
    description: ""
---