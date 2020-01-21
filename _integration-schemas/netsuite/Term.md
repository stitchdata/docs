---
tap: "netsuite"
version: "1"

name: "Term"
doc-link: ""
# singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/Term.json"
description: |
  The `{{ table.name }}` table contains info about the terms in your {{ integration.display_name }} account. Terms are used to specify when payment is due on customer invoices.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "term"

replication-method: "Full Table"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "term-id"

  - name: "dateDriven"
    type: "boolean, string"
    description: ""

  - name: "dayDiscountExpires"
    type: "integer, string"
    description: ""

  - name: "dayOfMonthNetDue"
    type: "integer, string"
    description: ""

  - name: "daysUntilExpiry"
    type: "integer, string"
    description: ""

  - name: "daysUntilNetDue"
    type: "integer, string"
    description: ""

  - name: "discountPercent"
    type: "number, string"
    description: ""

  - name: "discountPercentDateDriven"
    type: "number, string"
    description: ""

  - name: "dueNextMonthIfWithinDays"
    type: "integer, string"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "isInactive"
    type: "boolean, string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "preferred"
    type: "boolean, string"
    description: ""
---