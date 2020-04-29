---
tap: "saasoptics"
version: "1"
key: "register"

name: "registers"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-saasoptics/blob/master/tap_saasoptics/schemas/registers.json"
description: |
  The `{{ table.name }}` table contains info about registers, which can contain one or more [contracts](#contracts).

replication-method: "Key-based Incremental"

api-method:
  name: "Registers List"
  doc-link: "https://saasoptics.zendesk.com/hc/en-us/articles/115013751707-Registers-R-"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: ""
    foreign-key-id: "register-id"

  - name: "modified"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "currency_code"
    type: "string"
    description: ""

  - name: "default_qb_ar_account"
    type: "string"
    description: ""

  - name: "generated_invoice_number_prefix"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""
---