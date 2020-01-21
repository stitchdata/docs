---
tap: "chargebee"
version: "1"
key: "virtual-bank-account"

name: "virtual_bank_accounts"
doc-link: "https://apidocs.chargebee.com/docs/api/virtual_bank_accounts"
singer-schema: "https://github.com/singer-io/tap-chargebee/blob/master/tap_chargebee/schemas/virtual_bank_accounts.json"
description: |
  The `{{ table.name }}` table contains info about the virtual bank accounts in your {{ integration.display_name }} account. A virtual bank account is a unique account number that can be shared with your users while still protecting your sensitive bank account details.

replication-method: "Key-based Incremental"

api-method:
    name: "List virtual bank accounts"
    doc-link: "https://apidocs.chargebee.com/docs/api/virtual_bank_accounts#list_virtual_bank_accounts"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The virtual bank account number."
    #foreign-key-id: "virtual-bank-account-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the virtual bank account was last updated."

  - name: "account_number"
    type: "string"
    description: "The account number to which funds will be transferred."

  - name: "bank_name"
    type: "string"
    description: "The name of the bank."

  - name: "created_at"
    type: "date-time"
    description: "The time the virtual bank account was created."

  - name: "customer_id"
    type: "string"
    description: "The ID of the customer associated with the virtual bank account."
    foreign-key-id: "customer-id"

  - name: "deleted"
    type: "boolean"
    description: "Indicates if the virtual bank account has been deleted or not."

  - name: "email"
    type: "string"
    description: "The email address associated with the virtual bank account."

  - name: "gateway"
    type: "string"
    description: |
      The name of the gateway the virtual bank account is stored in. Refer to [{{ integration.display_name }}'s documentation](https://apidocs.chargebee.com/docs/api/virtual_bank_accounts#virtual_bank_account_gateway){:target="new"} for a full list of possible values.
    doc-link: "https://apidocs.chargebee.com/docs/api/virtual_bank_accounts#virtual_bank_account_gateway"

  - name: "gateway_account_id"
    type: "string"
    description: "The ID of the gateway account the virtual bank account is stored in."

  - name: "object"
    type: "string"
    description: ""

  - name: "reference_id"
    type: "string"
    description: "The ID provided by the gateway for the virtual bank account source."

  - name: "resource_version"
    type: "integer"
    description: "The version number of the virtual bank account. Each update of the virtual bank account results in an incremental change of this value. **Note**: This attribute will be present only if the credit note has been updated after 2016-09-28."

  - name: "routing_number"
    type: "string"
    description: "The routing number of the bank."

  - name: "swift_code"
    type: "string"
    description: "The swift code of the bank in which the account exists."
---