---
tap: "codat"
version: "1"
key: "account"

name: "accounts"
doc-link: "https://docs.codat.io/docs/accounts-1"
singer-schema: "https://github.com/singer-io/tap-codat/blob/master/tap_codat/schemas/accounts.json"
description: |
  The `{{ table.name }}` table contains info about the accounts in your {{ integration.display_name }} instance. In {{ integration.display_name }}, an account is a category used to record accounting transactions for a business.

replication-method: "Key-based Incremental"

api-method:
  name: "List accounts"
  doc-link: "https://docs.codat.io/reference/accounts#accounts_list"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The account ID."
    foreign-key-id: "account-id"

  - name: "companyId"
    type: "string"
    primary-key: true
    description: "The ID of the company associated with the account."
    foreign-key-id: "company-id"

  - name: "modifiedDate"
    type: "string"
    replication-key: true
    description: ""

  - name: "currency"
    type: "string"
    description: "The currency of the account."
    doc-link: "https://docs.codat.io/docs/currency"

  - name: "currentBalance"
    type: "number"
    description: "The current balance of the account."

  - name: "description"
    type: "string"
    description: ""

  - name: "fullyQualifiedName"
    type: "string"
    description: "The full name of the account. For example: `Liability.Current.VAT`"

  - name: "fullyQualifiedCategory"
    type: "string"
    description: ""

  - name: "isBankAccount"
    type: "boolean"
    description: "Indicates if the account is a bank account."

  - name: "name"
    type: "string"
    description: "The name of the account."
    foreign-key-id: "account-name"

  - name: "nominalCode"
    type: "string"
    description: "The reference given to each nominal account for a business."

  - name: "sourceModifiedDate"
    type: "string"
    description: ""

  - name: "status"
    type: "string"
    description: |
      The status of the account. Possible values are:

      - `Unknown`
      - `Active`
      - `Archived`
      - `Pending`

  - name: "type"
    type: "string"
    description: |
      The type of account. Possible values are:

      - `Unknown`
      - `Asset`
      - `Expense`
      - `Income`
      - `Liability`
      - `Equity`
---