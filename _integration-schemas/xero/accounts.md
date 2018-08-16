---
tap: "xero"
version: "1.0"

name: "accounts"
doc-link: &api-doc https://developer.xero.com/documentation/api/accounts
singer-schema: https://github.com/singer-io/tap-xero/blob/master/tap_xero/schemas/accounts.json
description: |
  The `{{ table.name }}` table contains info about the various accounts (ex: banking) connected to your Xero account.

replication-method: "Key-based Incremental"

api-method:
  name: getAccounts
  doc-link: *api-doc

attributes:
  - name: "AccountId"
    type: "string"
    primary-key: true
    description: "The account ID."
    foreign-key-id: "account-id"

  - name: "UpdatedDateUTC"
    type: "date-time"
    replication-key: true
    description: "The date the account was last modified, in UTC."

  - name: "Code"
    type: "string"
    description: "The alpha-numeric account code."

  - name: "Name"
    type: "string"
    description: "The name of the account."

  - name: "Type"
    type: "string"
    description: |
      The account type. Refer to [Xero's documentation](https://developer.xero.com/documentation/api/types#AccountTypes) for a list of possible account types.
    doc-link: https://developer.xero.com/documentation/api/types#AccountTypes

  - name: "ReportingCodeName"
    type: "string"
    description: "The name of the account's reporting code, if set."

  - name: "SystemAccount"
    type: "string"
    description: "If a system account, this field will contain the type of system account. Refer to [Xero's documentation](https://developer.xero.com/documentation/api/types#SystemAccounts) for a list of possible system account types."
    doc-link: https://developer.xero.com/documentation/api/types#SystemAccounts

  - name: "BankAccountType"
    type: "string"
    description: |
      **For bank accounts only**. Possible values are:

      - `BANK`
      - `CREDITCARD`
      - `PAYPAL`
    doc-link: https://developer.xero.com/documentation/api/types#BankAccountTypes

  - name: "TaxType"
    type: "string"
    description: "The account's tax type. Refer to [Xero's documentation](https://developer.xero.com/documentation/api/types#TaxTypes) for a list of possible tax types."
    doc-link: https://developer.xero.com/documentation/api/types#TaxTypes

  - name: "Description"
    type: "string"
    description: "**Not applicable to bank accounts.** The description of the account."

  - name: "Class"
    type: "string"
    description: |
      The account's class. Possible values are:

      - `ASSET`
      - `EQUITY`
      - `EXPENSE`
      - `LIABILITY`
      - `REVENUE`
    doc-link: https://developer.xero.com/documentation/api/types#AccountClassTypes

  - name: "BankAccountNumber"
    type: "string"
    description: "**For bank accounts only**. If the account is a bank account (`Type: BANK`), this field will contain its bank account number."

  - name: "Status"
    type: "string"
    description: |
      The status of the account. Possible values are:

      - `ACTIVE`
      - `ARCHIVED`

  - name: "ShowInExpenseClaims"
    type: "boolean"
    description: "If `true`, the account code is available for use with expense claims."

  - name: "CurrencyCode"
    type: "string"
    description: "**For bank accounts only**. The currency code the account uses."
    foreign-key-id: "currency-code"

  - name: "ReportingCode"
    type: "string"
    description: "The reporting code for the account, if set."

  - name: "EnablePaymentsToAccount"
    type: "boolean"
    description: "If `true`, the account may have payments applied to it."

  - name: "HasAttachments"
    type: "boolean"
    description: "If `true`, the account has an attachment."
---