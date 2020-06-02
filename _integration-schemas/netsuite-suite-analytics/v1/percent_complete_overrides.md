---
tap: "netsuite-suite-analytics"
version: "1"
key: "percent-complete-override"

name: "percent_complete_overrides"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/percent_complete_overrides.html"
description: |
  **Note**: This table’s data is available only to NetSuite accounts that have Advanced Revenue Management enabled.

replication-method: "Full Table"

attributes:
  - name: "accounting_period_id"
    type: "integer"
    description: ""

  - name: "comments"
    type: "string"
    description: ""

  - name: "percent_complete"
    type: "integer"
    description: ""
---