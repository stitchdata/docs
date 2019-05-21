---
tap: "netsuite"
version: "1.0"

name: "PaymentMethod"
doc-link: "https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/paymentmethod.html"
singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/PaymentMethod.json"
description: |
  The `{{ table.name }}` table contains info about the customer payment methods in your {{ integration.display_name }} account.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "payment-method"

replication-method: "Full Table"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "payment-method-id"

  - name: "account"
    type: "varies"
    description: ""

  - name: "creditCard"
    type: "boolean, string"
    description: ""

  - name: "expressCheckoutArrangement"
    type: "string"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "isDebitCard"
    type: "boolean, string"
    description: ""

  - name: "isInactive"
    type: "boolean, string"
    description: ""

  - name: "isOnline"
    type: "boolean, string"
    description: ""

  - name: "merchantAccountsList"
    type: "varies"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "payPalEmailAddress"
    type: "string"
    description: ""

  - name: "undepFunds"
    type: "boolean, string"
    description: ""

  - name: "useExpressCheckout"
    type: "boolean, string"
    description: ""

  - name: "visualsList"
    type: "varies"
    description: ""
---