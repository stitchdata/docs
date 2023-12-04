---
tap: "netsuite-suite-analytics"
version: "1"
key: "transaction"

name: "transactions"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/transaction.html"
description: |
  {{ integration.netsuite-replication-keys | flatify }}

  From NetSuite's documentation:

  > Credit and debit amounts are not exposed as columns in this table. However, you can query the `transaction_lines` table to obtain transaction credit and debit amounts. For more details, see [Connect Access to Transaction Credit and Debit Amounts](https://system.netsuite.com/app/help/helpcenter.nl?topic=DOC_section_4400769955){:target="new"}.
  
  > Item count and quantity values are not exposed as columns in in this table. However, you can query the `transaction_lines` table to obtain these values. For more details, see [Connect Access to Transaction Quantities](https://system.netsuite.com/app/help/helpcenter.nl?topic=DOC_section_1512507697){:target="new"}.

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

  - name: "last_modified_date"
    type: "date-time"
    replication-key: true
    description: |
      The time the {{ table.key | replace: "-"," " }} was last modified.

  - name: "account_based_number"
    type: "string"
    description: ""

  - name: "accounting_book_id"
    type: "integer"
    description: ""

  - name: "accounting_period_id"
    type: "integer"
    description: ""

  - name: "acct_corp_card_expenses_id"
    type: "integer"
    description: ""
    foreign-key-id: "account-id"

  - name: "amount_unbilled"
    type: "number"
    description: ""

  - name: "bill_pay_transaction"
    type: "string"
    description: ""

  - name: "billaddress"
    type: "string"
    description: ""

  - name: "billing_account_id"
    type: "integer"
    description: ""

  - name: "billing_instructions"
    type: "string"
    description: ""

  - name: "buildable"
    type: "integer"
    description: ""

  - name: "bulk_submission_id"
    type: "integer"
    description: ""

  - name: "carrier"
    type: "string"
    description: ""

  - name: "closed"
    type: "date-time"
    description: ""

  - name: "company_status_id"
    type: "integer"
    description: ""

  - name: "contract_cost_amount"
    type: "number"
    description: ""

  - name: "contract_defer_expense_acct_id"
    type: "integer"
    description: ""

  - name: "contract_expense_acct_id"
    type: "integer"
    description: ""

  - name: "contract_expense_src_acct_id"
    type: "integer"
    description: ""

  - name: "create_date"
    type: "date-time"
    description: ""

  - name: "created_by_id"
    type: "integer"
    description: ""

  - name: "created_from_id"
    type: "integer"
    description: ""

  - name: "currency_id"
    type: "integer"
    description: ""

  - name: "custom_form_id"
    type: "integer"
    description: ""

  - name: "date_actual_prod_end"
    type: "date-time"
    description: ""

  - name: "date_actual_prod_start"
    type: "date-time"
    description: ""

  - name: "date_bid_close"
    type: "date-time"
    description: ""

  - name: "date_bid_open"
    type: "date-time"
    description: ""

  - name: "date_contract_cost_accrual"
    type: "date-time"
    description: ""

  - name: "date_tax_point"
    type: "date-time"
    description: ""

  - name: "due_date"
    type: "date-time"
    description: ""

  - name: "email"
    type: "string"
    description: ""

  - name: "end_date"
    type: "date-time"
    description: ""

  - name: "entity_id"
    type: "integer"
    description: ""

  - name: "entity_tax_reg_num"
    type: "string"
    description: ""

  - name: "exchange_rate"
    type: "number"
    description: ""

  - name: "expected_close"
    type: "date-time"
    description: ""

  - name: "external_ref_number"
    type: "string"
    description: ""

  - name: "fax"
    type: "string"
    description: ""

  - name: "fob"
    type: "string"
    description: ""

  - name: "forecast_type"
    type: "string"
    description: ""

  - name: "include_in_forecast"
    type: "string"
    description: ""

  - name: "incoterm"
    type: "string"
    description: ""

  - name: "intercompany_transaction_id"
    type: "integer"
    description: ""

  - name: "is_actualprodenddate_manual"
    type: "string"
    description: ""

  - name: "is_actualprodstartdate_manual"
    type: "string"
    description: ""

  - name: "is_advanced_intercompany"
    type: "string"
    description: ""

  - name: "is_autocalculate_lag"
    type: "string"
    description: ""

  - name: "is_compliant"
    type: "string"
    description: ""

  - name: "is_created_from_merge"
    type: "string"
    description: ""

  - name: "is_cross_sub_transactions"
    type: "string"
    description: ""

  - name: "is_finance_charge"
    type: "string"
    description: ""

  - name: "is_firmed"
    type: "string"
    description: ""

  - name: "is_in_transit_payment"
    type: "string"
    description: ""

  - name: "is_intercompany"
    type: "string"
    description: ""

  - name: "is_merged_into_arrangements"
    type: "string"
    description: ""

  - name: "is_non_posting"
    type: "string"
    description: ""

  - name: "is_override_installments"
    type: "string"
    description: ""

  - name: "is_payment_hold"
    type: "string"
    description: ""

  - name: "is_reversal"
    type: "string"
    description: ""

  - name: "is_tax_point_date_override"
    type: "string"
    description: ""

  - name: "is_tax_reg_override"
    type: "string"
    description: ""

  - name: "is_wip"
    type: "string"
    description: ""

  - name: "item_revision"
    type: "integer"
    description: ""

  - name: "job_id"
    type: "integer"
    description: ""

  - name: "landed_cost_allocation_method"
    type: "string"
    description: ""

  - name: "last_sales_activity"
    type: "date-time"
    description: ""

  - name: "lead_source_id"
    type: "integer"
    description: ""

  - name: "location_id"
    type: "integer"
    description: ""

  - name: "lsa_link"
    type: "string"
    description: ""

  - name: "lsa_link_name"
    type: "string"
    description: ""

  - name: "memo"
    type: "string"
    description: ""

  - name: "memorized"
    type: "string"
    description: ""

  - name: "message"
    type: "string"
    description: ""

  - name: "needs_bill"
    type: "string"
    description: ""

  - name: "needs_revenue_commitment"
    type: "string"
    description: ""

  - name: "number_of_pricing_tiers"
    type: "integer"
    description: ""

  - name: "opening_balance_transaction"
    type: "string"
    description: ""

  - name: "ownership_transfer_id"
    type: "integer"
    description: ""

  - name: "packing_list_instructions"
    type: "string"
    description: ""

  - name: "partner_id"
    type: "integer"
    description: ""

  - name: "payment_terms_id"
    type: "integer"
    description: ""

  - name: "pn_ref_num"
    type: "string"
    description: ""

  - name: "probability"
    type: "number"
    description: ""

  - name: "product_label_instructions"
    type: "string"
    description: ""

  - name: "projected_total"
    type: "number"
    description: ""

  - name: "promotion_code_id"
    type: "integer"
    description: ""

  - name: "promotion_code_instance_id"
    type: "integer"
    description: ""

  - name: "purchase_order_instructions"
    type: "string"
    description: ""

  - name: "related_tranid"
    type: "string"
    description: ""

  - name: "renewal"
    type: "date-time"
    description: ""

  - name: "revenue_commitment_status"
    type: "string"
    description: ""

  - name: "revenue_committed"
    type: "date-time"
    description: ""

  - name: "revenue_status"
    type: "string"
    description: ""

  - name: "reversing_transaction_id"
    type: "integer"
    description: ""

  - name: "sales_effective_date"
    type: "date-time"
    description: ""

  - name: "sales_rep_id"
    type: "integer"
    description: ""

  - name: "scheduling_method_id"
    type: "string"
    description: ""

  - name: "shipaddress"
    type: "string"
    description: ""

  - name: "shipment_received"
    type: "date-time"
    description: ""

  - name: "shipping_item_id"
    type: "integer"
    description: ""

  - name: "start_date"
    type: "date-time"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "tax_reg_id"
    type: "integer"
    description: ""

  - name: "title"
    type: "string"
    description: ""

  - name: "trandate"
    type: "date-time"
    description: ""

  - name: "tranid"
    type: "string"
    description: ""

  - name: "trans_is_vsoe_bundle"
    type: "string"
    description: ""

  - name: "transaction_extid"
    type: "string"
    description: ""

  - name: "transaction_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "transaction-id"

  - name: "transaction_number"
    type: "string"
    description: ""

  - name: "transaction_partner"
    type: "string"
    description: ""

  - name: "transaction_source"
    type: "string"
    description: ""

  - name: "transaction_type"
    type: "string"
    description: ""

  - name: "transaction_website"
    type: "integer"
    description: ""

  - name: "transfer_location"
    type: "integer"
    description: ""

  - name: "use_item_cost_as_transfer_cost"
    type: "string"
    description: ""

  - name: "visible_in_customer_center"
    type: "string"
    description: ""

  - name: "weighted_total"
    type: "integer"
    description: ""
---