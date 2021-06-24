---
# -------------------------- #
#        Table Details       #
# -------------------------- #

tap: "mambu"
version: "2"
key: "loan-repayment"

name: "loan_repayments"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-mambu/blob/master/tap_mambu/schemas/loan_repayments.json"
description: |
  This is a child table of `loan_accounts`, containing information exclusively about loan repayments.
  

# -------------------------- #
#    Replication Details     #
# -------------------------- #

api-method:
  name: "Get repayments for a loan account (v1.0)"
  doc-link: "https://api.mambu.com/v1/#loan-accounts-get-repayments-for-a-loan-account"

replication-method: "Full Table"

dependent-table-key: "loan_accounts"


# -------------------------- #
#       Table Attributes     #
# -------------------------- #

attributes:
  - name: "encoded_key"
    type: "string"
    primary-key: true
    description: "The unique loan repayment encoded key."
    # foreign-key-id: "loan-repayment-key"

  - name: "due_date"
    type: "date-time"
    description: ""
  
  - name: "fees_due"
    type: "string"
    description: ""

  - name: "fees_paid"
    type: "string"
    description: ""

  - name: "interest_due"
    type: "string"
    description: ""

  - name: "interest_paid"
    type: "string"
    description: ""

  - name: "parent_account_key"
    type: "string"
    description: ""

  - name: "penalty_due"
    type: "string"
    description: ""

  - name: "penalty_paid"
    type: "string"
    description: ""

  - name: "principal_due"
    type: "string"
    description: ""

  - name: "principal_paid"
    type: "string"
    description: ""

  - name: "state"
    type: "string"
    description: ""

  - name: "tax_fees_due"
    type: "string"
    description: ""

  - name: "tax_fees_paid"
    type: "string"
    description: ""

  - name: "tax_interest_due"
    type: "string"
    description: ""

  - name: "tax_interest_paid"
    type: "string"
    description: ""

  - name: "tax_penalty_due"
    type: "string"
    description: ""

  - name: "tax_penalty_paid"
    type: "string"
    description: ""
---