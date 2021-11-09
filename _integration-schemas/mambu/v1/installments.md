---
# -------------------------- #
#        Table Details       #
# -------------------------- #

tap: "mambu"
version: "1"
key: "installment"

name: "installments"
doc-link: "https://api.mambu.com/#mambu-api-v2-installments"
singer-schema: "https://github.com/singer-io/tap-mambu/tree/v1.3.3/tap_mambu/schemas/installments.json"
description: |
  This table contains information about installments for a loan.


# -------------------------- #
#    Replication Details     #
# -------------------------- #

api-method:
  name: "Get all installments (v2.0)"
  doc-link: "https://api.mambu.com/#installments-getall"

replication-method: "Key-based Incremental"


# -------------------------- #
#       Table Attributes     #
# -------------------------- #

attributes:
  - name: "encoded_key"
    type: "string"
    primary-key: true
    description: "The unique installments encoded key."
    #foreign-key-id: "installments-encoded-key"

  - name: "last_paid_date"
    type: "date-time"
    replication-key: true
    description: "The date of the the last paid installment."
      
  - name: "due_date"
    type: "date-time"
    description: ""
  
  - name: "fee"
    type: "object"
    description: ""
    subattributes:
      - name: "amount"
        type: "object"
        description: ""
        subattributes:
          - name: "due"
            type: "number"
            description: ""
          - name: "expected"
            type: "number"
            description: ""
          - name: "paid"
            type: "number"
            description: ""
      - name: "tax"
        type: "object"
        description: ""
        subattributes:
          - name: "due"
            type: "number"
            description: ""
          - name: "expected"
            type: "number"
            description: ""
          - name: "paid"
            type: "number"
            description: ""
  - name: "interest"
    type: "object"
    description: ""
    subattributes:
      - name: "amount"
        type: "object"
        description: ""
        subattributes:
          - name: "due"
            type: "number"
            description: ""
          - name: "expected"
            type: "number"
            description: ""
          - name: "paid"
            type: "number"
            description: ""
      - name: "tax"
        type: "object"
        description: ""
        subattributes:
          - name: "due"
            type: "number"
            description: ""
          - name: "expected"
            type: "number"
            description: ""
          - name: "paid"
            type: "number"
            description: ""
  
  - name: "number"
    type: "string"
    description: ""
  - name: "penalty"
    type: "object"
    description: ""
    subattributes:
      - name: "amount"
        type: "object"
        description: ""
        subattributes:
          - name: "due"
            type: "number"
            description: ""
          - name: "expected"
            type: "number"
            description: ""
          - name: "paid"
            type: "number"
            description: ""
      - name: "tax"
        type: "object"
        description: ""
        subattributes:
          - name: "due"
            type: "number"
            description: ""
          - name: "expected"
            type: "number"
            description: ""
          - name: "paid"
            type: "number"
            description: ""
  - name: "principal"
    type: "object"
    description: ""
    subattributes:
      - name: "amount"
        type: "object"
        description: ""
        subattributes:
          - name: "due"
            type: "number"
            description: ""
          - name: "expected"
            type: "number"
            description: ""
          - name: "paid"
            type: "number"
            description: ""
  - name: "repaid_date"
    type: "date-time"
    description: ""
  - name: "state"
    type: "string"
    description: ""
---
