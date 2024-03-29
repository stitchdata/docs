---
tap: "quickbooks"
version: "2"
key: "journal-entry"

name: "journal_entries"
doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/journalentry"
singer-schema: "https://github.com/singer-io/tap-quickbooks/blob/master/tap_quickbooks/schemas/journal_entries.json"
description: |
  The `{{ table.name }}` table contains info about the journal entries in your {{ integration.display_name }} instance. A journal entry is a transaction that:

  - Contains a pair of distribution lines, including a debit and a credit
  - Each distribution line has an account from the Chart of Accounts
  - The total of the debit column equals the total of the credit column

replication-method: "Key-based Incremental"

replication-key:
  name: "Metadata.LastUpdatedTime"

api-method:
  name: "Query a journal entry"
  doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/journalentry/#query-a-journalentry"

attributes:
  - name: "Id"
    type: "string"
    primary-key: true
    description: "The journal entry ID."
    foreign-key-id: "journal-entry-id"

  - name: "Adjustment"
    type: "boolean"
    description: ""

  - name: "CurrencyRef"
    type: "object"
    description: "Details about the currency the journal entry is in."
    subattributes: &name-value
      - name: "name"
        type: "string"
        description: ""

      - name: "value"
        type: "string"
        description: ""

  - name: "DocNumber"
    type: "string"
    description: ""

  - name: "domain"
    type: "string"
    description: ""

  - name: "ExchangeRate"
    type: "decimal"
    description: ""
  
  - name: "GlobalTaxCalculation"
    type: "string"
    description: ""

  - name: "HomeTotalAmt"
    type: "number"
    description: ""

  - name: "JournalCodeRef"
    type: "object"
    description: ""
    subattributes: *name-value

  - name: "Line"
    type: "array"
    description: ""
    subattributes:
      - name: "Amount"
        type: "decimal"
        description: ""

      - name: "Description"
        type: "string"
        description: ""

      - name: "DescriptionLineDetail"
        type: "object"
        description: ""
        subattributes:
          - name: "ServiceDate"
            type: "date-time"
            description: ""
            
          - name: "TaxCodeRef"
            type: "object"
            description: ""
            subattributes: *name-value

      - name: "DetailType"
        type: "string"
        description: ""

      - name: "Id"
        type: "string"
        description: ""

      - name: "JournalEntryLineDetail"
        type: "object"
        description: ""
        subattributes:
          - name: "AccountRef"
            type: "object"
            description: "Details about the account associated with the journal entry line item."
            subattributes: *name-value
            
          - name: "Entity"
            type: "object"
            description: ""
            subattributes:
              - name: "EntityRef"
                type: "object"
                description: ""
                subattributes: *name-value

              - name: "value"
                type: "string"
                description: ""

          - name: "TaxApplicableOn"
            type: "string"
            description: ""

          - name: "TaxInclusiveAmt"
            type: "decimal"
            description: ""

          - name: "PostingType"
            type: "string"
            description: ""

      - name: "LineNum"
        type: "decimal"
        description: ""

  - name: "MetaData"
    type: "object"
    description: ""
    subattributes:
      - name: "CreateTime"
        type: "date-time"
        description: ""

      - name: "LastUpdatedTime"
        type: "date-time"
        description: ""

  - name: "PrivateNote"
    type: "string"
    description: ""

  - name: "RecurDate"
    type: "object"
    description: ""
    subattributes: *name-value

  - name: "SyncToken"
    type: "string"
    description: ""

  - name: "TaxRateRef"
    type: "object"
    description: ""
    subattributes: *name-value

  - name: "TotalAmt"
    type: "number"
    description: ""

  - name: "TransactionLocationType"
    type: "string"
    description: ""

  - name: "TxnDate"
    type: "date-time"
    description: ""

  - name: "TxnTaxDetail"
    type: "object"
    description: ""
    subattributes:
      - name: "TaxLine"
        type: "array"
        description: ""
        subattributes:
          - name: "Amount"
            type: "decimal"
            description: ""

          - name: "DetailType"
            type: "string"
            description: ""

          - name: "TaxLineDetail"
            type: "object"
            description: ""
            subattributes:
              - name: "NetAmountTaxable"
                type: "decimal"
                description: ""

              - name: "OverrideDeltaAmount"
                type: "number"
                description: ""

              - name: "PercentBased"
                type: "boolean"
                description: ""

              - name: "TaxInclusiveAmount"
                type: "number"
                description: ""

              - name: "TaxPercent"
                type: "decimal"
                description: ""

              - name: "TaxRateRef"
                type: "object"
                description: "Details about the tax rate associated with the tax line."
                subattributes:
                  - name: "value"
                    type: "string"
                    description: "The tax rate ID."
                    foreign-key-id: "tax-rate-id"

      - name: "TotalTax"
        type: "decimal"
        description: ""

      - name: "TxnTaxCodeRef"
        type: "object"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: "The tax code ID."
            foreign-key-id: "tax-code-id"
---