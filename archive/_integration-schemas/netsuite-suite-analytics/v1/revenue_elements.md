---
tap: "netsuite-suite-analytics"
version: "1"
key: "revenue-element"

name: "revenue_elements"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/revenue_elements.html"
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

  - name: "accounting_book_id"
    type: "integer"
    description: ""

  - name: "accounting_period_id"
    type: "integer"
    description: ""

  - name: "allocated_contract_cost_amount"
    type: "number"
    description: ""

  - name: "allocation_amount"
    type: "number"
    description: ""

  - name: "allocation_amount_foreign"
    type: "number"
    description: ""

  - name: "allocation_type"
    type: "string"
    description: ""

  - name: "alternate_quantity"
    type: "integer"
    description: ""

  - name: "alternate_unit_id"
    type: "integer"
    description: ""

  - name: "amortization_end_date"
    type: "date-time"
    description: ""

  - name: "amortization_schedule_id"
    type: "integer"
    description: ""

  - name: "amortization_start_date"
    type: "date-time"
    description: ""

  - name: "amortization_template_id"
    type: "integer"
    description: ""

  - name: "calculated_amount"
    type: "number"
    description: ""

  - name: "calculated_amount_foreign"
    type: "number"
    description: ""

  - name: "class_id"
    type: "integer"
    description: ""

  - name: "contract_cost_allocation_pct"
    type: "integer"
    description: ""

  - name: "contract_exp_offset_acct_id"
    type: "integer"
    description: ""

  - name: "contract_expense_account_id"
    type: "integer"
    description: ""

  - name: "cost_amortization_amount"
    type: "number"
    description: ""

  - name: "create_plan_on_event_type"
    type: "string"
    description: ""

  - name: "currency_id"
    type: "integer"
    description: ""

  - name: "date_created"
    type: "date-time"
    description: ""

  - name: "deferral_account_id"
    type: "integer"
    description: ""

  - name: "department_id"
    type: "integer"
    description: ""

  - name: "disc_sales_amount_foreign"
    type: "number"
    description: ""

  - name: "discounted_sales_amount"
    type: "number"
    description: ""

  - name: "end_date"
    type: "date-time"
    description: ""

  - name: "entity_id"
    type: "integer"
    description: ""

  - name: "exchange_rate"
    type: "number"
    description: ""

  - name: "expense_migrate_adjust_acct_id"
    type: "integer"
    description: ""

  - name: "fair_value"
    type: "number"
    description: ""

  - name: "fair_value_foreign"
    type: "number"
    description: ""

  - name: "forecast_end_date"
    type: "date-time"
    description: ""

  - name: "forecast_start_date"
    type: "date-time"
    description: ""

  - name: "fx_adjustment_account_id"
    type: "integer"
    description: ""

  - name: "is_bom_item_type"
    type: "string"
    description: ""

  - name: "is_fair_value_override"
    type: "string"
    description: ""

  - name: "is_fair_value_vsoe"
    type: "string"
    description: ""

  - name: "is_hold_rev_rec"
    type: "string"
    description: ""

  - name: "is_permit_discount"
    type: "string"
    description: ""

  - name: "is_posting_discount_applied"
    type: "string"
    description: ""

  - name: "item_id"
    type: "integer"
    description: ""

  - name: "item_labor_cost_amount"
    type: "number"
    description: ""

  - name: "item_resale_cost_amount"
    type: "number"
    description: ""

  - name: "labor_deferred_expense_acct_id"
    type: "integer"
    description: ""

  - name: "labor_expense_acct_id"
    type: "integer"
    description: ""

  - name: "last_merge_from_arrangement_id"
    type: "integer"
    description: ""

  - name: "location_id"
    type: "integer"
    description: ""

  - name: "new_standard_migrate_date"
    type: "date-time"
    description: ""

  - name: "parent_bom_element_id"
    type: "integer"
    description: ""

  - name: "pending_action"
    type: "string"
    description: ""

  - name: "quantity"
    type: "number"
    description: ""

  - name: "recognition_account_id"
    type: "integer"
    description: ""

  - name: "reference_id"
    type: "string"
    description: ""

  - name: "return_revenue_element_id"
    type: "integer"
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

  - name: "revenue_allocation_ratio"
    type: "integer"
    description: ""

  - name: "revenue_element_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "revenue-element-id"

  - name: "revenue_element_number"
    type: "string"
    description: ""

  - name: "revenue_migrate_adjust_acct_id"
    type: "integer"
    description: ""

  - name: "sales_amount"
    type: "number"
    description: ""

  - name: "sales_amount_foreign"
    type: "number"
    description: ""

  - name: "source_date"
    type: "date-time"
    description: ""

  - name: "source_id"
    type: "integer"
    description: ""

  - name: "source_transaction_id"
    type: "integer"
    description: ""

  - name: "source_type"
    type: "string"
    description: ""

  - name: "start_date"
    type: "date-time"
    description: ""

  - name: "subscription_line"
    type: "integer"
    description: ""

  - name: "subsidiary_id"
    type: "integer"
    description: ""

  - name: "term_in_days"
    type: "integer"
    description: ""

  - name: "term_in_months"
    type: "integer"
    description: ""

  - name: "unbilled_receivable_group"
    type: "string"
    description: ""
---