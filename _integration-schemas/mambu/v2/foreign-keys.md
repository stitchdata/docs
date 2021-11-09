---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-foreign-keys/
## FOR INSTRUCTIONS & REFERENCE INFO

tap-reference: "mambu"

version: "2"

foreign-keys:
  - id: "activity-key"
    table: "activities"
    attribute: "encoded_key"
    all-foreign-keys:
      - table: "activities"

  - id: "branch-key"
    table: "branches"
    attribute: "encoded_key"
    all-foreign-keys:
      - table: "branches"
        join-on: "encoded_key"

      - table: "centres"
        join-on: "assigned_branch_key"

      - table: "deposit_transactions"
        join-on: "branch_key"

      - table: "groups"
        join-on: "assigned_branch_key"

      - table: "loan_accounts"
        join-on: "assigned_branch_key"

      - table: "loan_transactions"
        join-on: "branch_key"

      - table: "users"
        subattribute: "access.managed_branches"
        join-on: "branch_key"  

  - id: "centre-key"
    table: "centres"
    attribute: "encoded_key"
    all-foreign-keys:
      - table: "centres"
        join-on: "encoded_key"
      - table: "clients"
        join-on: "assigned_centre_key"
      - table: "deposit_transactions"
        join-on: "centre_key" 
      - table: "groups"
        join-on: "assigned_centre_key"
      - table: "loan_accounts"
        join-on: "assigned_centre_key" 
      - table: "loan_transactions"
        join-on: "centre_key"      

  - id: "client-key"
    table: "clients"
    attribute: "client_key"
    all-foreign-keys:
      - table: "activities"
      - table: "clients"
        join-on: "encoded_key"
      - table: "communications"
      - table: "groups"
        subattribute: "group_members"
        join-on: "clientKey"   

  - id: "communication-key"
    table: "communications"
    attribute: "encoded_key"
    all-foreign-keys:
      - table: "communications"
        join-on: "encoded_key"

  - id: "credit-arrangement-key"
    table: "credit_arrangements"
    attribute: "credit_arrangement_key"
    all-foreign-keys:
      - table: "credit_arrangements"
        join-on: "encoded_key"

      - table: "deposit_accounts"

      - table: "loan_accounts"

  - id: "custom-field-set-id"
    table: "custom_field_sets"
    attribute: "custom_fields.field_set_id"
    all-foreign-keys:
      - table: "branches"
      - table: "centres"
      - table: "clients"
      - table: "communications"
      - table: "credit_arrangements"
      - table: "custom_field_sets"
        join-on: "id"
      - table: "deposit_accounts"
      - table: "deposit_products"
        subattribute: "custom_field_values.custom_field.custom_field_set"
        join-on: "id"
      - table: "deposit_transactions"
      - table: "groups"
      - table: "loan_accounts"
      - table: "loan_products"
        subattribute: "custom_field_values.custom_field.custom_field_set"
        join-on: "id"
      - table: "loan_transactions"
      - table: "tasks"
      - table: "users"       
        
  - id: "custom-field-id"
    table: "custom_field_sets"
    attribute: "custom_fields.id"
    all-foreign-keys:
      - table: "branches"
      - table: "centres"
      - table: "clients"
      - table: "communications"
      - table: "credit_arrangements"
      - table: "custom_field_sets"
        subattribute: "custom_fields"
        join-on: "id"
      - table: "deposit_accounts"
      - table: "deposit_products"
        subattribute: "custom_field_values.custom_field"
        join-on: "id"
      - table: "deposit_products"
        subattribute: "custom_field_values"
        join-on: "custom_field_id"
      - table: "deposit_transactions"
      - table: "groups"
      - table: "loan_accounts"
      - table: "loan_products"
        subattribute: "custom_field_values.custom_field"
        join-on: "id"
      - table: "loan_products"
        subattribute: "custom_field_values"
        join-on: "custom_field_id"
      - table: "loan_transactions"
      - table: "tasks"
      - table: "users"

  - id: "deposit-id"
    table: "deposits"
    attribute: "deposit_id"
    all-foreign-keys:
      - table: "cards"
        join-on: "deposit_id"

  - id: "deposit-account-key"
    table: "deposit_accounts"
    attribute: "deposit_account_key"
    all-foreign-keys:
      - table: "communications"
      - table: "deposit_accounts"
        join-on: "encoded_key"
      - table: "loan_accounts"
        subattribute: "disbursement_details.transaction_details"
        join-on: "target_deposit_account_key"
      - table: "loan_accounts"
        subattribute: "funding_sources"
      - table: "loan_accounts"
        subattribute: "guarantors"

  - id: "deposit-product-id"
    table: "deposit_products"
    attribute: "id"
    all-foreign-keys:
      - table: "deposit_products"
        join-on: "id"

  - id: "deposit-transaction-key"
    table: "deposit_transactions"
    attribute: "transfer_details.linked_deposit_transaction_key"
    all-foreign-keys:
      - table: "deposit_transactions"
      - table: "loan_transactions"

  - id: "gl-account-code"
    table: "gl_accounts"
    attribute: "gl_code"
    all-foreign-keys:
      - table: "gl_accounts"
      - table: "gl_journal_entries"
        subattribute: "gl_account"

  - id: "group-key"
    table: "groups"
    attribute: "group_key"
    all-foreign-keys:
      - table: "communications"
      - table: "groups"
        join-on: "encoded_key"

  - id: "index-rate-key"
    table: "index_rate_sources"
    attribute: ""
    all-foreign-keys:
      - table: "index_rate_sources"

  - id: "installment-key"
    table: "installments"
    attribute: ""
    all-foreign-keys:
      - table: "installments"
        join-on: "encoded_key"
        
  - id: "loan-account-key"
    table: "loan_accounts"
    attribute: "encoded_key"
    all-foreign-keys:
      - table: "communications"
        join-on: "loan_account_key"
      - table: "loan_accounts"

  - id: "loan-product-key"
    table: "loan_products"
    attribute: ""
    all-foreign-keys:
      - table: "loan_products"
        join-on: "encoded_key"

  - id: "loan-transaction-key"
    table: "loan_transactions"
    attribute: "linked_loan_transaction_key"
    all-foreign-keys:
      - table: "deposit_transactions"
      - table: "deposit_transactions"
        subattribute: "transfer_details"
      - table: "loan_transactions"
        join-on: "encoded_key"
      - table: "loan_transactions"
      - table: "loan_transactions"
        join-on: "parent_loan_transaction_key"
      - table: "loan_transactions"
        subattribute: "transfer_details"
  
  - id: "user-key"
    table: "users"
    attribute: "user_key"
    all-foreign-keys:
      - table: "activities"
      - table: "clients"
        join-on: "assigned_user_key"
      - table: "communications"
      - table: "communications"
        join-on: "sender_key"
      - table: "deposit_transactions"
      - table: "gl_journal_entries"
      - table: "groups"
        join-on: "assigned_user_key"
      - table: "loan_accounts"
        join-on: "assigned_user_key" 
      - table: "loan_transactions"
      - table: "tasks"
        join-on: "created_by_user_key"
      - table: "tasks"
        join-on: "assigned_user_key"
      - table: "users"
        join-on: "encoded_key"              
---