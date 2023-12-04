---
tap: "quickbooks"
version: "2"
key: "profit-loss-report"

name: "profit_loss_report"
doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/most-commonly-used/profitandloss"
singer-schema: "https://github.com/singer-io/tap-quickbooks/blob/master/tap_quickbooks/schemas/profit_loss_report.json"
description: |
  The `{{ table.name }}` table contains reports about profit and loss recorded in your {{ integration.display_name }} instance.
 
replication-method: "Key-based Incremental"

replication-key:
  name: "ReportDate"

api-method:
  name: "Query a report"
  doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/most-commonly-used/profitandloss#query-a-report"

attributes:
  - name: "ReportDate"
    type: "string"
    primary-key: true
    description: "The date of the report."
    
  - name: "AccountingMethod"
    type: "string"
    description: "The accounting method used in the report."
    
  - name: "Details"
    type: "object"
    description: "The attributes selected when the report was created."
---