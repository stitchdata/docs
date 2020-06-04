---
tap: "netsuite-suite-analytics"
version: "1"
key: "vendor-currency"

name: "vendor_currencies"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/vendor_currencies.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "currency_id"
    type: "integer"
    description: ""

  - name: "in_transit_balance_foreign"
    type: "number"
    description: ""

  - name: "openbalance_foreign"
    type: "number"
    description: ""

  - name: "unbilled_orders_foreign"
    type: "number"
    description: ""

  - name: "vendor_id"
    type: "integer"
    description: ""
---