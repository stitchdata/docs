---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-foreign-keys/
## FOR INSTRUCTIONS & REFERENCE INFO

tap-reference: "mambu"

version: "1"

foreign-keys:
  - id: "branch-encoded-key"
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

  - id: "centre-encoded-key"
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

  - id: "client-encoded-key"
    table: "clients"
    attribute: "encoded_key"
    all-foreign-keys:
      - table: "communications"
        join-on: "client_key"

      # - table: "deposit_accounts"
      #   join-on: "account_holder_key" 

      - table: "groups"
        subattribute: "group_members"
        join-on: "clientKey"   

  - id: "communications-encoded-key"
    table: "communications"
    attribute: "encoded_key"
    all-foreign-keys:
      - table: "communications"
        join-on: "encoded_key"

  - id: "credit-arrangement-key"
    table: "credit_arrangements"
    attribute: "encoded_key"
    all-foreign-keys:
      - table: "credit_arrangements"
        join-on: "encoded_key"

      - table: "deposit_accounts"
        join-on: "credit_arrangement_key"

      - table: "loan_accounts"
        join-on: "credit_arrangement_key" 

  - id: "custom-field-set-id"
    table: "custom_field_sets"
    attribute: "custom_field_set_id"
    all-foreign-keys:
      - table: "branches"
        subattribute: "custom_field_sets"
        join-on: "custom_field_set_id"

      - table: "centres"
        subattribute: "custom_field_sets"
        join-on: "custom_field_set_id"

      - table: "clients"
        subattribute: "custom_field_sets"
        join-on: "custom_field_set_id"

      - table: "credit_arrangements"
        subattribute: "custom_field_sets"
        join-on: "custom_field_set_id"

      - table: "communications"
        subattribute: "custom_field_sets"
        join-on: "custom_field_set_id"

      - table: "deposit_accounts"
        subattribute: "custom_field_sets"
        join-on: "custom_field_set_id"

      - table: "deposit_transactions"
        subattribute: "custom_field_sets"
        join-on: "custom_field_set_id"

      - table: "groups"
        subattribute: "custom_field_sets"
        join-on: "custom_field_set_id"  

      - table: "loan_accounts"
        subattribute: "custom_field_sets"
        join-on: "custom_field_set_id"

      - table: "loan_transactions"
        subattribute: "custom_field_sets"
        join-on: "custom_field_set_id"

      - table: "tasks"
        subattribute: "custom_field_sets"
        join-on: "custom_field_set_id" 

      - table: "users"
        subattribute: "custom_field_sets"
        join-on: "custom_field_set_id"           
        
  - id: "custom-field-id"
    table: "custom_field_sets"
    attribute: "custom_field_id"
    all-foreign-keys:
      - table: "branches"
        subattribute: "custom_field_sets.custom_field_values"
        join-on: "custom_field_id"

      - table: "centres"
        subattribute: "custom_field_sets.custom_field_values"
        join-on: "custom_field_id"

      - table: "clients"
        subattribute: "custom_field_sets.custom_field_values"
        join-on: "custom_field_id" 

      - table: "communications"
        subattribute: "custom_field_sets.custom_field_values"
        join-on: "custom_field_id" 

      - table: "credit_arrangements"
        subattribute: "custom_field_sets.custom_field_values"
        join-on: "custom_field_id"

      - table: "custom_field_sets"
        subattribute: "custom_fields"
        join-on: "id"

      - table: "deposit_accounts"
        subattribute: "custom_field_sets.custom_field_values"
        join-on: "custom_field_id" 

      - table: "deposit_transactions"
        subattribute: "custom_field_sets.custom_field_values"
        join-on: "custom_field_id"

      - table: "groups"
        subattribute: "custom_field_sets.custom_field_values"
        join-on: "custom_field_id" 

      - table: "loan_accounts"
        subattribute: "custom_field_sets.custom_field_values"
        join-on: "custom_field_id"

      - table: "loan_transactions"
        subattribute: "custom_field_sets.custom_field_values"
        join-on: "custom_field_id"

      - table: "tasks"
        subattribute: "custom_field_sets.custom_field_values"
        join-on: "custom_field_id" 

      - table: "users"
        subattribute: "custom_field_sets.custom_field_values"
        join-on: "custom_field_id"

  - id: "deposit-account-encoded-key"
    table: "deposit_accounts"
    attribute: "encoded_key"
    all-foreign-keys:
      - table: "communications"
        join-on: "deposit_account_key"

  - id: "deposit-product-id"
    table: "deposit_products"
    attribute: "id"
    all-foreign-keys:
      - table: "deposit_products"
        join-on: "id"

  - id: "group-encoded-key"
    table: "groups"
    attribute: "encoded_key"
    all-foreign-keys:
      - table: "communications"
        join-on: "group_key"

  - id: "linked-deposit-transaction-key"
    table: "deposit_transactions"
    attribute: "linked_deposit_transaction_key"
    all-foreign-keys:
      - table: "deposit_transactions"
        subattribute: "transfer_details"
        join-on: "linked_deposit_transaction_key"

      - table: "loan_transactions"
        subattribute: "transfer_details"
        join-on: "linked_deposit_transaction_key"  

  - id: "linked-loan-transaction-key"
    table: "loan_transactions"
    attribute: "linked_loan_transaction_key"
    all-foreign-keys:
      - table: "deposit_transactions"
        join-on: "linked_loan_transaction_key"

      - table: "loan_transactions"
        join-on: "linked_loan_transaction_key"  
        
  - id: "loan-account-encoded-key"
    table: "loan_accounts"
    attribute: "encoded_key"
    all-foreign-keys:
      - table: "communications"
        join-on: "loan_account_key"

  - id: "loan-transaction-encoded-key"
    table: "loan_transactions"
    attribute: "encoded_key"
    all-foreign-keys:
      - table: "loan_transactions"
        join-on: "encoded_key" 
        
  - id: "parent-loan-key"
    table: "loan_transactions"
    attribute: "parent_loan_transaction_key"
    all-foreign-keys:
      - table: "loan_transactions"
        join-on: "parent_loan_transaction_key" 
  
  - id: "user-encoded-key"
    table: "users"
    attribute: "encoded_key"
    all-foreign-keys:
      - table: "clients"
        join-on: "assigned_user_key"

      - table: "communications"
        join-on: "user_key"

      - table: "communications"
        join-on: "sender_key"

      - table: "deposit_transactions"
        join-on: "user_key"

      - table: "groups"
        join-on: "assigned_user_key"

      - table: "loan_accounts"
        join-on: "assigned_user_key" 

      - table: "loan_transactions"
        join-on: "user_key" 

      - table: "tasks"
        join-on: "created_by_user_key"

      - table: "tasks"
        join-on: "assigned_user_key"               
      

  # - id: "branch-id"
  #   table: "branches"
  #   attribute: "id"
  #   all-foreign-keys:
  #     - table: "branches"
  #       join-on: "id"

  # - id: "deposit-id"
  #   table: "deposits"
  #   attribute: "deposit_id"
  #   all-foreign-keys:
  #     - table: "cards"
  #       join-on: "deposit_id"
        
  # - id: "reference-token"
  #   table: "cards"
  #   attribute: "reference_token"
  #   all-foreign-keys:
  #     - table: "cards"
  #       join-on: "reference_token"
  
  # - id: "center-id"
  #   table: "centres"
  #   attribute: "id"
  #   all-foreign-keys:
  #     - table: "centres"
  #       join-on: "id"
        
  # - id: "client-id"
  #   table: "clients"
  #   attribute: "id"
  #   all-foreign-keys:
  #     - table: "clients"
  #       join-on: "id"

  # - id: "credit-arrangement-id"
  #   table: "credit_arrangements"
  #   attribute: "id"
  #   all-foreign-keys:
  #     - table: "credit_arrangements"
  #       join-on: "id"
     
  # - id: "loan-accounts-id"
  #   table: "loan_accounts"
  #   attribute: "id"
  #   all-foreign-keys:
  #     - table: "loan_accounts"
  #       join-on: "id"  

  # - id: "loan-product-id"
  #   table: "loan_products"
  #   attribute: "id"
  #   all-foreign-keys:
  #     - table: "loan_products"
  #       join-on: "id" 
  
  # - id: "task-id"
  #   table: "tasks"
  #   attribute: "id"
  #   all-foreign-keys:
  #     - table: "tasks"
  #       join-on: "id" 
        
  # - id: "user-id"
  #   table: "users"
  #   attribute: "id"
  #   all-foreign-keys:
  #     - table: "users"
  #       join-on: "id"
---