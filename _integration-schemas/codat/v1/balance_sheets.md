---
tap: "codat"
version: "1"
key: "balance-sheet"

name: "balance_sheets"
doc-link: "https://docs.codat.io/docs/balance-sheet-2"
singer-schema: "https://github.com/singer-io/tap-codat/blob/master/tap_codat/schemas/balance_sheets.json"
description: |
  The `{{ table.name }}` table contains info about the balance sheets in your {{ integration.display_name }} instance. A balance sheet is a snapshot at a point in time of a company's accounts.

replication-method: "Full Table"

api-method:
    name: "List balance sheets for a company"
    doc-link: "https://docs.codat.io/reference/financials#financials_balancesheet"

attributes:
  - name: "companyId"
    type: "string"
    primary-key: true
    description: "The ID of the company the balance sheet is for."

  - name: "currency"
    type: "string"
    description: "The currency of the balance sheet."

  - name: "mostRecentAvailableMonth"
    type: "string"
    description: "The most recent available month from which report data can be shown."

  - name: "reports"
    type: "array"
    description: "A list of balance sheet reports."
    subattributes:
      - name: "assets"
        type: "array"
        description: "A list of asset report lines."
        subattributes: &report
          - name: "accountId"
            type: "string"
            description: "The account ID."
            foreign-key-id: "account-id"

          - name: "name"
            type: "string"
            description: "The name of the account."

          - name: "value"
            type: "number"
            description: "The balance of the account."

      - name: "date"
        type: "date-time"
        description: "The specified point in time for the balance sheet."

      - name: "equity"
        type: "array"
        description: "A list of equity report lines."
        subattributes: *report

      - name: "liabilities"
        type: "array"
        description: "A list of liability report lines."
        subattributes: *report

      - name: "netAssets"
        type: "number"
        description: "The value of net assets for the company, in their base currency."

  - name: "status"
    type: "string"
    description: ""
---