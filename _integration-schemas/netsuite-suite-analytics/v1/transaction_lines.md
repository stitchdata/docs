---
tap: "netsuite-suite-analytics"
version: "1"
key: "transaction-line"

name: "transaction_lines"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/transaction_lines.html"
description: |
  From NetSuite's documentation:

  > Credit and debit amounts are not exposed as columns in this table. However, you can query this table to obtain transaction credit and debit amounts.
  
  > To obtain landed cost category names, you can include the `memo` column in your query. For each line where `is_landed_cost` is set to `Yes`, text is written to this column in the format `<Landed Cost Category Name>:<Item Name>`.

replication-method: "Key-based Incremental"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "date_last_modified_gmt"
    type: "date-time"
    replication-key: true
    description: |
      The time the {{ table.key | replace: "-"," " }} was last modified.

  - name: "account_id"
    type: "integer"
    description: ""
    foreign-key-id: "account-id"

  - name: "alt_sales_amount"
    type: "number"
    description: ""

  - name: "amortization_residual"
    type: "string"
    description: ""

  - name: "amount"
    type: "number"
    description: ""

  - name: "amount_foreign"
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

  - name: "amount_settlement"
    type: "number"
    description: ""

  - name: "amount_taxable"
    type: "number"
    description: ""

  - name: "amount_taxed"
    type: "number"
    description: ""

  - name: "bill_variance_status"
    type: "string"
    description: ""

  - name: "billing_schedule_id"
    type: "integer"
    description: ""
    foreign-key-id: "billing-schedule-id"

  - name: "billing_subsidiary_id"
    type: "integer"
    description: ""

  - name: "bom_quantity"
    type: "number"
    description: ""

  - name: "catch_up_period_id"
    type: "integer"
    description: ""

  - name: "charge_rule_id"
    type: "integer"
    description: ""

  - name: "charge_type"
    type: "integer"
    description: ""

  - name: "class_id"
    type: "integer"
    description: ""

  - name: "company_id"
    type: "integer"
    description: ""

  - name: "component_id"
    type: "integer"
    description: ""

  - name: "component_yield"
    type: "integer"
    description: ""

  - name: "cost_estimate_type"
    type: "string"
    description: ""

  - name: "date_cleared"
    type: "date-time"
    description: ""

  - name: "date_closed"
    type: "date-time"
    description: ""

  - name: "date_created"
    type: "date-time"
    description: ""

  - name: "date_last_modified"
    type: "date-time"
    description: |
      The time the {{ table.key | replace: "-"," " }} was last modified.

  - name: "date_requested"
    type: "date-time"
    description: ""

  - name: "date_revenue_committed"
    type: "date-time"
    description: ""

  - name: "delay_rev_rec"
    type: "string"
    description: ""

  - name: "department_id"
    type: "integer"
    description: ""

  - name: "do_not_display_line"
    type: "string"
    description: ""

  - name: "do_not_print_line"
    type: "string"
    description: ""

  - name: "do_restock"
    type: "string"
    description: ""

  - name: "estimated_cost"
    type: "number"
    description: ""

  - name: "estimated_cost_foreign"
    type: "number"
    description: ""

  - name: "expected_receipt_date"
    type: "date-time"
    description: ""

  - name: "expense_category_id"
    type: "integer"
    description: ""

  - name: "gl_number"
    type: "string"
    description: ""

  - name: "gl_sequence"
    type: "string"
    description: ""

  - name: "gl_sequence_id"
    type: "integer"
    description: ""

  - name: "gross_amount"
    type: "integer"
    description: ""

  - name: "has_cost_line"
    type: "string"
    description: ""

  - name: "is_allocation"
    type: "string"
    description: ""

  - name: "is_amortization_rev_rec"
    type: "string"
    description: ""

  - name: "is_commitment_confirmed"
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

  - name: "is_fx_variance"
    type: "string"
    description: ""

  - name: "is_item_value_adjustment"
    type: "string"
    description: ""

  - name: "is_landed_cost"
    type: "string"
    description: ""

  - name: "is_scrap"
    type: "string"
    description: ""

  - name: "is_vsoe_allocation_line"
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

  - name: "item_received"
    type: "string"
    description: ""

  - name: "item_source"
    type: "string"
    description: ""

  - name: "item_unit_price"
    type: "string"
    description: ""

  - name: "kit_part_number"
    type: "integer"
    description: ""

  - name: "landed_cost_source_line_id"
    type: "integer"
    description: ""

  - name: "location_id"
    type: "integer"
    description: ""

  - name: "match_bill_to_receipt"
    type: "string"
    description: ""

  - name: "memo"
    type: "string"
    description: ""

  - name: "needs_revenue_element"
    type: "string"
    description: ""

  - name: "net_amount"
    type: "integer"
    description: ""

  - name: "net_amount_foreign"
    type: "integer"
    description: ""

  - name: "non_posting_line"
    type: "string"
    description: ""

  - name: "number_billed"
    type: "number"
    description: ""

  - name: "operation_sequence_number"
    type: "integer"
    description: ""

  - name: "order_priority"
    type: "number"
    description: ""

  - name: "payment_method_id"
    type: "integer"
    description: ""

  - name: "payroll_item_id"
    type: "integer"
    description: ""

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

  - name: "project_task_id"
    type: "integer"
    description: ""

  - name: "purchase_contract_id"
    type: "integer"
    description: ""

  - name: "quantity_allocated"
    type: "number"
    description: ""

  - name: "quantity_committed"
    type: "number"
    description: ""

  - name: "quantity_packed"
    type: "number"
    description: ""

  - name: "quantity_picked"
    type: "number"
    description: ""

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

  - name: "rev_rec_end_date"
    type: "date-time"
    description: ""

  - name: "rev_rec_rule_id"
    type: "integer"
    description: ""

  - name: "rev_rec_start_date"
    type: "date-time"
    description: ""

  - name: "revenue_element_id"
    type: "integer"
    description: ""

  - name: "schedule_id"
    type: "integer"
    description: ""

  - name: "shipdate"
    type: "date-time"
    description: ""

  - name: "shipment_received"
    type: "date-time"
    description: ""

  - name: "shipping_group_id"
    type: "integer"
    description: ""
    foreign-key-id: "transaction-shipping-group-id"

  - name: "source_subsidiary_id"
    type: "integer"
    description: ""
    foreign-key-id: "subsidiary-id"

  - name: "subscription_line_id"
    type: "integer"
    description: ""

  - name: "subsidiary_id"
    type: "integer"
    description: ""
    foreign-key-id: "subsidiary-id"

  - name: "tax_item_id"
    type: "integer"
    description: ""

  - name: "tax_type"
    type: "string"
    description: ""

  - name: "term_in_months"
    type: "integer"
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

  - name: "transaction_discount_line"
    type: "string"
    description: ""

  - name: "transaction_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "transaction-id"

  - name: "transaction_line_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "transaction-line-id"

  - name: "transaction_order"
    type: "integer"
    description: ""

  - name: "transfer_order_item_line"
    type: "integer"
    description: ""

  - name: "transfer_order_line_type"
    type: "string"
    description: ""

  - name: "unique_key"
    type: "integer"
    description: ""

  - name: "unit_cost_override"
    type: "number"
    description: ""

  - name: "unit_of_measure_id"
    type: "integer"
    description: ""

  - name: "vsoe_allocation"
    type: "number"
    description: ""

  - name: "vsoe_amt"
    type: "number"
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