---
tap: "netsuite-suite-analytics"
version: "1"
key: "opportunity-line"

name: "opportunity_lines"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/opportunity_lines.html"
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

  - name: "account_id"
    type: "integer"
    description: ""
    foreign-key-id: "account-id"

  - name: "amount"
    type: "number"
    description: ""

  - name: "amount_foreign_linked"
    type: "number"
    description: ""

  - name: "amount_linked"
    type: "number"
    description: ""

  - name: "amount_pending"
    type: "number"
    description: ""

  - name: "amount_taxable"
    type: "number"
    description: ""

  - name: "amount_taxed"
    type: "number"
    description: ""

  - name: "class_id"
    type: "integer"
    description: ""
    foreign-key-id: "class-id"

  - name: "company_id"
    type: "integer"
    description: ""
    foreign-key-id: "company-id"

  - name: "date_cleared"
    type: "date-time"
    description: ""

  - name: "date_closed"
    type: "date-time"
    description: ""

  - name: "department_id"
    type: "integer"
    description: ""
    foreign-key-id: "department-id"

  - name: "do_not_display_line"
    type: "string"
    description: ""

  - name: "do_not_print_line"
    type: "string"
    description: ""

  - name: "expense_category_id"
    type: "integer"
    description: ""
    foreign-key-id: "expense-category-id"

  - name: "gross_amount"
    type: "integer"
    description: ""

  - name: "has_cost_line"
    type: "string"
    description: ""

  - name: "is_cost_line"
    type: "string"
    description: ""

  - name: "is_custom_line"
    type: "string"
    description: ""

  - name: "is_exclude_from_rate_request"
    type: "string"
    description: ""

  - name: "is_item_value_adjustment"
    type: "string"
    description: ""

  - name: "isbillable"
    type: "string"
    description: ""

  - name: "iscleared"
    type: "string"
    description: ""

  - name: "isnonreimbursable"
    type: "string"
    description: ""

  - name: "istaxable"
    type: "string"
    description: ""

  - name: "item_count"
    type: "number"
    description: ""

  - name: "item_id"
    type: "integer"
    description: ""
    foreign-key-id: "item-id"

  - name: "item_received"
    type: "string"
    description: ""

  - name: "item_unit_price"
    type: "string"
    description: ""

  - name: "kit_part_number"
    type: "integer"
    description: ""

  - name: "location_id"
    type: "integer"
    description: ""
    foreign-key-id: "location-id"

  - name: "memo"
    type: "string"
    description: ""

  - name: "net_amount"
    type: "integer"
    description: ""

  - name: "non_posting_line"
    type: "string"
    description: ""

  - name: "number_billed"
    type: "number"
    description: ""

  - name: "number_revenue_committed"
    type: "number"
    description: ""

  - name: "opportunity_discount_line"
    type: "string"
    description: ""

  - name: "opportunity_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "opportunity-id"

  - name: "opportunity_line_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""

  - name: "opportunity_order"
    type: "integer"
    description: ""

  - name: "payment_method_id"
    type: "integer"
    description: ""
    foreign-key-id: "payment-method-id"

  - name: "payroll_item_id"
    type: "integer"
    description: ""
    foreign-key-id: "payroll-item-id"

  - name: "payroll_wage_base_amount"
    type: "number"
    description: ""

  - name: "payroll_year_to_date_amount"
    type: "number"
    description: ""

  - name: "period_closed"
    type: "date-time"
    description: ""

  - name: "price_type_id"
    type: "integer"
    description: ""
    foreign-key-id: "price-type-id"

  - name: "quantity_received_in_shipment"
    type: "number"
    description: ""

  - name: "receivebydate"
    type: "date-time"
    description: ""

  - name: "reimbursement_type"
    type: "string"
    description: ""

  - name: "related_company_id"
    type: "integer"
    description: ""
    foreign-key-id: "entity-id"

  - name: "shipdate"
    type: "date-time"
    description: ""

  - name: "shipment_received"
    type: "date-time"
    description: ""

  - name: "subsidiary_id"
    type: "integer"
    description: ""
    foreign-key-id: "subsidiary-id"

  - name: "tax_item_id"
    type: "integer"
    description: ""
    foreign-key-id: "item-id"

  - name: "tax_type"
    type: "string"
    description: ""

  - name: "tobeemailed"
    type: "string"
    description: ""

  - name: "tobefaxed"
    type: "string"
    description: ""

  - name: "tobeprinted"
    type: "string"
    description: ""
---