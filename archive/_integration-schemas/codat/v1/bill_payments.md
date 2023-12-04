---
tap: "codat"
version: "1"
key: "bill-payment"

name: "bill_payments"
doc-link: "https://docs.codat.io/docs/billpayments-1"
singer-schema: "https://github.com/singer-io/tap-codat/blob/master/tap_codat/schemas/bill_payments.json"
description: |
  The {{ table.name }} table contains information about company bill payments in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
  name: "Get bill payments"
  doc-link: "https://docs.codat.io/reference/billpayments#billpayments_listpaged"

attributes:
  - name: "companyId"
    type: "string"
    primary-key: true
    description: "The company ID."
    foreign-key-id: "company-id"

  - name: "id"
    type: "string"
    primary-key: true
    description: "The bill payment ID."
    foreign-key-id: "bill-payment-id"

  - name: "modifiedDate"
    type: "string"
    description: "The date the bill payment was last modified."
    replication-key: true  
      
  - name: "currency"
    type: "string"
    description: ""

  - name: "currencyRate"
    type: "number"
    description: ""

  - name: "date"
    type: "string"
    description: ""

  - name: "lines"
    type: "array"
    description: ""
    subattributes:
      - name: "amount"
        type: "number"
        description: ""

      - name: "links"
        type: "array"
        description: ""
        subattributes:
          - name: "id"
            type: "string"
            description: ""

          - name: "type"
            type: "string"
            description: ""

  - name: "note"
    type: "string"
    description: ""

  - name: "sourceModifiedDate"
    type: "string"
    description: ""

  - name: "supplierRef"
    type: "object"
    description: ""
    subattributes:
      - name: "addresses"
        type: "array"
        description: ""
        subattributes:
          - name: "city"
            type: "string"
            description: ""

          - name: "country"
            type: "string"
            description: ""

          - name: "line1"
            type: "string"
            description: ""

          - name: "line2"
            type: "string"
            description: ""

          - name: "postalCode"
            type: "string"
            description: ""

          - name: "region"
            type: "string"
            description: ""

          - name: "type"
            type: "string"
            description: ""

      - name: "companyId"
        type: "string"
        description: ""
        foreign-key-id: "company-id"

      - name: "contactName"
        type: "string"
        description: ""

      - name: "emailAddress"
        type: "string"
        description: ""

      - name: "id"
        type: "string"
        description: ""
        foreign-key-id: "supplier-id"

      - name: "phone"
        type: "string"
        description: ""

      - name: "registrationNumber"
        type: "string"
        description: ""

      - name: "status"
        type: "string"
        description: ""

      - name: "supplierName"
        type: "string"
        description: ""

      - name: "taxNumber"
        type: "string"
        description: ""

  - name: "totalAmount"
    type: "number"
    description: ""
---