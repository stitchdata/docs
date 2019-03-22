---
tap: "xero"
version: "1.0"

name: "manual_journals"
doc-link: &api-doc https://developer.xero.com/documentation/api/manual-journals
singer-schema: https://github.com/singer-io/tap-xero/blob/master/tap_xero/schemas/manual_journals.json
description: |
  The `{{ table.name }}` table contains info about manual journals, which are used by accountants or bookkeepers to work directly with a general ledger. For example: To record accrued expenses or completed work that wasn't invoiced.

replication-method: "Key-based Incremental"

api-method:
  name: getManualJournals
  doc-link: *api-doc

attributes:
  - name: "ManualJournalID"
    type: "string"
    primary-key: true
    description: "The manual journal ID."
    # foreign-key-id: "manual-journal-id"

  - name: "UpdatedDateUTC"
    type: "date-time"
    replication-key: true
    description: "The date the manual journal was last updated, in UTC."

  - name: "Date"
    type: "date-time"
    description: "The date the journal was posted."

  - name: "LineAmountTypes"
    type: "string"
    description: |
      The type of amounts that the line items in the manual journal contain. Possible values are:

      - `Exclusive` - Line items are exclusive of tax
      - `Inclusive` - Line items are inclusive tax
      - `NoTax` - Line items have no tax
    doc-link: https://developer.xero.com/documentation/api/types#LineAmountTypes

  - name: "Status"
    type: "string"
    description: |
      The status of the manual journal. Possible values are:

      - `DRAFT`
      - `POSTED`
      - `DELETED`
      - `VOIDED`

  - name: "Narration"
    type: "string"
    description: "A description of the journal being posted."

  - name: "JournalLines"
    type: "array"
    description: "Details about the journal lines in the manual journal."
    subattributes:
      - name: "LineAmount"
        type: "number"
        description: "The total amount for the line. This will be a positive value for a debit, negative for a credit."

      - name: "Description"
        type: "string"
        description: "A description of the journal line."

      - name: "TaxAmount"
        type: "number"
        description: "The calculated tax amount, based on `TaxType` and `LineAmount`."

      - name: "AccountCode"
        type: "string"
        description: "The account code associated with the journal line."

      # - name: "IsBlank"
      #   type: "boolean"
      #   description: "If `true`, "

      - name: "TaxType"
        type: "string"
        description: |
          The tax type for the journal line. Refer to [{{ integration.display_name }}'s documentation](https://developer.xero.com/documentation/api/types#TaxTypes){:target="new"} for possible tax types.

      - name: "Tracking"
        type: ""
        description: |
          Details about the tracking details associated with the journal line.

          {{ integration.subsubtable-note | flatify | replace:"table_name","tracking_categories" }}

  - name: "Url"
    type: "string"
    description: "A URL link to a source document."

  - name: "ShowOnCashBasisReports"
    type: "boolean"
    description: "If `true`, the manual journal will show on Cash Basis Reports."

  - name: "HasAttachments"
    type: "boolean"
    description: "If `true`, the manual journal has an attachment."
---