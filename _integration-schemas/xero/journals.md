---
tap: "xero"
version: "1.0"

name: "journals"
doc-link: &api-doc https://developer.xero.com/documentation/api/journals
singer-schema: https://github.com/singer-io/tap-xero/blob/master/tap_xero/schemas/journals.json
description: |
  The `journals` table contains info about journal entries.

replication-method: "Incremental"

api-method:
  name: getJournals
  doc-link: *api-doc

attributes:
  - name: "JournalID"
    type: "string"
    primary-key: true
    description: "The journal ID."

  - name: "If-Modified-Since"
    type: "date-time"
    replication-key: true
    description: "**Note**: This is not a field that will be replicated to your data warehouse. This is a filter Stitch uses in its API calls to retrieve only new and updated data."

  - name: "JournalDate"
    type: "date-time"
    description: "The date the journal was posted."

  - name: "JournalNumber"
    type: "string"
    description: "A Xero-generated journal number."

  - name: "CreatedDateUTC"
    type: "date-time"
    description: "The date the journal was created, in UTC."

  - name: "Reference"
    type: "string"
    description: "The reference for the journal."

  - name: "SourceID"
    type: "string"
    description: |
      The identifier for the source transaction. Use the `SourceType` value to identify the type of transaction that created the journal.

      For example: If `SourceType: ARPREPAYMENT`, this field would contain a `PrepaymentID`, which you can use to join this table to the `prepayments` table.

  - name: "SourceType"
    type: "string"
    description: |
      The type of transaction that created the journal. Refer to [Xero's documentation](https://developer.xero.com/documentation/api/Types#JournalSourceTypes) for a list of possible values.
    doc-link: https://developer.xero.com/documentation/api/Types#JournalSourceTypes

  - name: "JournalLines"
    type: "array"
    description: "Details about the journal lines in the journal."
    array-attributes:
      - name: "JournalLineID"
        type: "string"
        description: "The journal line ID."

      - name: "AccountID"
        type: "string"
        description: "The account ID associated with the journal line."
        foreign-key: true

      - name: "AccountType"
        type: "string"
        description: "The type of the account."

      - name: "AccountCode"
        type: "string"
        description: "The account code associated with the account."

      - name: "TaxName"
        type: "string"
        description: "The tax type of the account."

      - name: "Description"
        type: "string"
        description: "The description from the source transaction line item."

      - name: "GrossAmount"
        type: "number"
        description: "The gross amount of the journal line, calculated as `NetAmount + TaxAmount`."

      - name: "NetAmount"
        type: "number"
        description: "The net amount of the journal line. This value will be positive for a debit and negative for a credit."

      - name: "AccountName"
        type: "string"
        description: "The name of the account."

      - name: "TaxAmount"
        type: "number"
        description: "The total tax on the journal line."

      - name: "TrackingCategories"
        type: "array"
        description: ""
        array-attributes:

---