---
tap: "codat"
version: "1"
key: "profit-and-loss"

name: "profit_and_loss"
doc-link: "https://docs.codat.io/docs/profit-and-loss-2"
singer-schema: "https://github.com/singer-io/tap-codat/blob/master/tap_codat/schemas/profit_and_loss.json"
description: |
  The `{{ table.name }}` table contains profit and loss report data for a company over a time period.

replication-method: "Full Table"

api-method:
  name: "List latest profit and loss for a company"
  doc-link: "https://docs.codat.io/reference/financials#financials_profitandloss"

attributes:
  - name: "companyId"
    type: "string"
    primary-key: true
    description: "The company ID."
    foreign-key-id: "company-id"

  - name: "currency"
    type: "string"
    description: "The base currency for the company."

  - name: "mostRecentAvailableMonth"
    type: "string"
    description: "The most recent available month from which report data can be shown."

  - name: "reportBasis"
    type: "string"
    description: |
      The basis of the report. Possible values are:

      - `Accrual`
      - `Cash`
      - `Unknown`

  - name: "reports"
    type: "array"
    description: "A list of profit and loss reports."
    subattributes:
      - name: "costOfSales"
        type: "array"
        description: "A list of line items for cost of sales."
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

      - name: "expenses"
        type: "array"
        description: "A list of line items for expenses."
        subattributes: *report

      - name: "fromDate"
        type: "string"
        description: "The date from which the report data begins."

      - name: "grossProfit"
        type: "number"
        description: "The gross profit of the company for the given date range (`fromDate - toDate`)."

      - name: "income"
        type: "array"
        description: "A list of line items for other income."
        subattributes: *report

      - name: "netOperatingProfit"
        type: "number"
        description: "The net operating profit of the company for the given date range (`fromDate - toDate`)."

      - name: "netOtherIncome"
        type: "number"
        description: "The net other income of the company for the given date range (`fromDate - toDate`)."

      - name: "netProfit"
        type: "number"
        description: "The net profit of the company for the given date range (`fromDate - toDate`)."

      - name: "otherExpenses"
        type: "array"
        description: "A list of line items for other expenses."
        subattributes: *report

      - name: "otherIncome"
        type: "array"
        description: "A list of line items for other income."
        subattributes: *report

      - name: "toDate"
        type: "string"
        description: "The date for which the report data ends."
---