---
tap: "netsuite-suite-analytics"
version: "1"
key: "service-item"

name: "service_items"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/serviceitem.html"
description: ""

replication-method: "Key-based Incremental"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "date_last_modified"
    type: "date-time"
    replication-key: true
    description: |
      The time the {{ table.key | replace: "-"," " }} was last modified.

  - name: "cost_0"
    type: "number"
    description: ""

  - name: "cost_category"
    type: "string"
    description: ""

  - name: "create_plan_on_event_type"
    type: "string"
    description: ""

  - name: "created"
    type: "date-time"
    description: ""

  - name: "date_of_last_transaction"
    type: "date-time"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "displayname"
    type: "string"
    description: ""

  - name: "expense_account_id"
    type: "integer"
    description: ""

  - name: "featureddescription"
    type: "string"
    description: ""

  - name: "full_name"
    type: "string"
    description: ""

  - name: "fx_adjustment_account_id"
    type: "integer"
    description: ""

  - name: "include_child_subsidiaries"
    type: "string"
    description: ""

  - name: "income_account_id"
    type: "integer"
    description: ""

  - name: "interco_expense_account_id"
    type: "integer"
    description: ""

  - name: "interco_income_account_id"
    type: "integer"
    description: ""

  - name: "is_moss"
    type: "string"
    description: ""

  - name: "isinactive"
    type: "string"
    description: ""

  - name: "isonline"
    type: "string"
    description: ""

  - name: "istaxable"
    type: "string"
    description: ""

  - name: "item_extid"
    type: "string"
    description: ""

  - name: "item_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "service-item-id"

  - name: "item_revenue_category"
    type: "string"
    description: ""

  - name: "manufacturing_charge_item"
    type: "string"
    description: ""

  - name: "matrix_type"
    type: "string"
    description: ""

  - name: "modified"
    type: "date-time"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "offersupport"
    type: "string"
    description: ""

  - name: "onspecial"
    type: "string"
    description: ""

  - name: "parent_id"
    type: "integer"
    description: ""

  - name: "payment_method_id"
    type: "integer"
    description: ""

  - name: "pref_purchase_tax_id"
    type: "integer"
    description: ""

  - name: "pref_sale_tax_id"
    type: "integer"
    description: ""

  - name: "prices_include_tax"
    type: "string"
    description: ""

  - name: "print_sub_items"
    type: "string"
    description: ""

  - name: "purchasedescription"
    type: "string"
    description: ""

  - name: "rate"
    type: "string"
    description: ""

  - name: "rev_rec_forecast_rule_id"
    type: "integer"
    description: ""

  - name: "rev_rec_rule_id"
    type: "integer"
    description: ""

  - name: "revenue_allocation_group"
    type: "string"
    description: ""

  - name: "specialsdescription"
    type: "string"
    description: ""

  - name: "storedescription"
    type: "string"
    description: ""

  - name: "storedetaileddescription"
    type: "string"
    description: ""

  - name: "storedisplayname"
    type: "string"
    description: ""

  - name: "subtype"
    type: "string"
    description: ""

  - name: "upc_code"
    type: "string"
    description: ""

  - name: "vendor_id"
    type: "integer"
    description: ""

  - name: "vendorname"
    type: "string"
    description: ""

  - name: "vsoe_deferral"
    type: "string"
    description: ""

  - name: "vsoe_delivered"
    type: "string"
    description: ""

  - name: "vsoe_discount"
    type: "string"
    description: ""

  - name: "vsoe_price"
    type: "number"
    description: ""
---