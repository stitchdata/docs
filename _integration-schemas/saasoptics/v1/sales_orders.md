---
tap: "saasoptics"
version: "1"
key: "sale-order"

name: "sales_orders"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-saasoptics/blob/master/tap_saasoptics/schemas/sales_orders.json"
description: |
  The `{{ table.name }}` table contains info about sales orders, which have historically been synced in through the Salesforce integration and processed into financial records within {{ integration.display_name }}.

replication-method: "Key-based Incremental"

api-method:
  name: "Sales Orders List"
  doc-link: "https://saasoptics.zendesk.com/hc/en-us/articles/360000738813-Sales-Orders-CR-"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: ""
    # foreign-key-id: "sale-order-id"

  - name: "created"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "close_date"
    type: "date-time"
    description: ""

  - name: "contract_channel"
    type: "string"
    description: ""

  - name: "contract_email"
    type: "string"
    description: ""

  - name: "contract_entry_date"
    type: "date-time"
    description: ""

  - name: "contract_is_job"
    type: "boolean"
    description: ""

  - name: "contract_lead_date"
    type: "date-time"
    description: ""

  - name: "contract_lead_source"
    type: "string"
    description: ""

  - name: "contract_notes"
    type: "string"
    description: ""

  - name: "contract_number"
    type: "string"
    description: ""

  - name: "contract_number_field1"
    type: "number"
    description: ""

  - name: "contract_number_field2"
    type: "number"
    description: ""

  - name: "contract_register_name"
    type: "string"
    description: ""

  - name: "contract_sf_id"
    type: "string"
    description: ""

  - name: "contract_text_field1"
    type: "string"
    description: ""

  - name: "contract_text_field2"
    type: "string"
    description: ""

  - name: "contract_unbalanced_revenue_exception"
    type: "boolean"
    description: ""

  - name: "created_by_username"
    type: "string"
    description: ""

  - name: "customer_account_number"
    type: "string"
    description: ""

  - name: "customer_alt_contact"
    type: "string"
    description: ""

  - name: "customer_alt_phone"
    type: "string"
    description: ""

  - name: "customer_autopay_enrollment"
    type: "string"
    description: ""

  - name: "customer_billing_addr3"
    type: "string"
    description: ""

  - name: "customer_billing_city"
    type: "string"
    description: ""

  - name: "customer_billing_country"
    type: "string"
    description: ""

  - name: "customer_billing_state"
    type: "string"
    description: ""

  - name: "customer_billing_street"
    type: "string"
    description: ""

  - name: "customer_billing_zip_code"
    type: "string"
    description: ""

  - name: "customer_code"
    type: "string"
    description: ""

  - name: "customer_contact"
    type: "string"
    description: ""

  - name: "customer_crm_id"
    type: "string"
    description: ""

  - name: "customer_currency"
    type: "string"
    description: ""

  - name: "customer_default_autorenewal_profile"
    type: "string"
    description: ""

  - name: "customer_default_cadence_template"
    type: "string"
    description: ""

  - name: "customer_default_email_from_so"
    type: "string"
    description: ""

  - name: "customer_default_enable_ach_payment"
    type: "boolean"
    description: ""

  - name: "customer_default_enable_cc_payment"
    type: "boolean"
    description: ""

  - name: "customer_default_invoice_template"
    type: "string"
    description: ""

  - name: "customer_default_theme"
    type: "string"
    description: ""

  - name: "customer_do_not_sync"
    type: "boolean"
    description: ""

  - name: "customer_email"
    type: "string"
    description: ""

  - name: "customer_enable_autopay"
    type: "boolean"
    description: ""

  - name: "customer_entity_use_code"
    type: "string"
    description: ""

  - name: "customer_fax"
    type: "string"
    description: ""

  - name: "customer_first_name"
    type: "string"
    description: ""

  - name: "customer_industry"
    type: "string"
    description: ""

  - name: "customer_invoice_email_preference"
    type: "boolean"
    description: ""

  - name: "customer_invoice_print_preference"
    type: "boolean"
    description: ""

  - name: "customer_item_sales_tax"
    type: "string"
    description: ""

  - name: "customer_last_name"
    type: "string"
    description: ""

  - name: "customer_market"
    type: "string"
    description: ""

  - name: "customer_name"
    type: "string"
    description: ""

  - name: "customer_notes"
    type: "string"
    description: ""

  - name: "customer_number"
    type: "string"
    description: ""

  - name: "customer_number_field1"
    type: "number"
    description: ""

  - name: "customer_number_field2"
    type: "number"
    description: ""

  - name: "customer_number_field3"
    type: "number"
    description: ""

  - name: "customer_parent"
    type: "string"
    description: ""

  - name: "customer_payment_terms"
    type: "string"
    description: ""

  - name: "customer_phone"
    type: "string"
    description: ""

  - name: "customer_resale_number"
    type: "string"
    description: ""

  - name: "customer_sales_rep"
    type: "string"
    description: ""

  - name: "customer_sales_tax_code"
    type: "string"
    description: ""

  - name: "customer_salutation"
    type: "string"
    description: ""

  - name: "customer_segment"
    type: "string"
    description: ""

  - name: "customer_sf_default_renewal_opportunity_rule"
    type: "string"
    description: ""

  - name: "customer_sf_opportunity_price_book_id"
    type: "string"
    description: ""

  - name: "customer_sf_owner_id"
    type: "string"
    description: ""

  - name: "customer_sfdc_object_id"
    type: "string"
    description: ""

  - name: "customer_shipping_addr3"
    type: "string"
    description: ""

  - name: "customer_shipping_city"
    type: "string"
    description: ""

  - name: "customer_shipping_country"
    type: "string"
    description: ""

  - name: "customer_shipping_state"
    type: "string"
    description: ""

  - name: "customer_shipping_street"
    type: "string"
    description: ""

  - name: "customer_shipping_zip_code"
    type: "string"
    description: ""

  - name: "customer_subsegment"
    type: "string"
    description: ""

  - name: "customer_text_field1"
    type: "string"
    description: ""

  - name: "customer_text_field2"
    type: "string"
    description: ""

  - name: "customer_text_field3"
    type: "string"
    description: ""

  - name: "customer_type"
    type: "string"
    description: ""

  - name: "customer_unbalanced_revenue_exception"
    type: "boolean"
    description: ""

  - name: "line_items"
    type: "array"
    description: ""
    subattributes:
      - name: "affected_transaction"
        type: "string"
        description: ""

      - name: "created"
        type: "date-time"
        description: ""

      - name: "created_by_username"
        type: "string"
        description: ""

      - name: "id"
        type: "integer"
        description: ""

      - name: "invoice_billing_addr1"
        type: "string"
        description: ""

      - name: "invoice_billing_addr2"
        type: "string"
        description: ""

      - name: "invoice_billing_addr3"
        type: "string"
        description: ""

      - name: "invoice_billing_city"
        type: "string"
        description: ""

      - name: "invoice_billing_country"
        type: "string"
        description: ""

      - name: "invoice_billing_state"
        type: "string"
        description: ""

      - name: "invoice_billing_zip_code"
        type: "string"
        description: ""

      - name: "invoice_cadence_template"
        type: "string"
        description: ""

      - name: "invoice_date"
        type: "date-time"
        description: ""

      - name: "invoice_do_not_sync"
        type: "boolean"
        description: ""

      - name: "invoice_ei_combine_all_description"
        type: "string"
        description: ""

      - name: "invoice_ei_combine_lines"
        type: "string"
        description: ""

      - name: "invoice_ei_theme"
        type: "string"
        description: ""

      - name: "invoice_email_from_so"
        type: "boolean" 
        description: ""

      - name: "invoice_enable_ach_payment"
        type: "boolean"
        description: ""

      - name: "invoice_enable_cc_payment"
        type: "boolean"
        description: ""

      - name: "invoice_ignore_date_when_syncing"
        type: "boolean"
        description: ""

      - name: "invoice_invoice_memo"
        type: "string"
        description: ""

      - name: "invoice_other"
        type: "string"
        description: ""

      - name: "invoice_payment_terms"
        type: "string"
        description: ""

      - name: "invoice_po_number"
        type: "string"
        description: ""

      - name: "invoice_qb_class"
        type: "string"
        description: ""

      - name: "invoice_qb_customer_message"
        type: "string"
        description: ""

      - name: "invoice_qb_payment_terms"
        type: "string"
        description: ""

      - name: "invoice_qb_sales_rep"
        type: "string"
        description: ""

      - name: "invoice_qb_template"
        type: "string"
        description: ""

      - name: "invoice_ship_date"
        type: "date-time"
        description: ""

      - name: "invoice_shipping_addr1"
        type: "string"
        description: ""

      - name: "invoice_shipping_addr2"
        type: "string"
        description: ""

      - name: "invoice_shipping_addr3"
        type: "string"
        description: ""

      - name: "invoice_shipping_city"
        type: "string"
        description: ""

      - name: "invoice_shipping_country"
        type: "string"
        description: ""

      - name: "invoice_shipping_state"
        type: "string"
        description: ""

      - name: "invoice_shipping_zip_code"
        type: "string"
        description: ""

      - name: "invoice_suppress_zero_value_line_items"
        type: "boolean"
        description: ""

      - name: "invoice_invoice_to_be_emailed"
        type: "boolean"
        description: ""

      - name: "invoice_to_be_printed"
        type: "boolean"
        description: ""

      - name: "line_item_id"
        type: "string"
        description: ""

      - name: "processed"
        type: "boolean"
        description: ""

      - name: "project_template"
        type: "string"
        description: ""

      - name: "renewed_transaction"
        type: "string"
        description: ""

      - name: "sfdc_object_type"
        type: "string"
        description: ""

      - name: "transaction_action"
        type: "string"
        description: ""

      - name: "transaction_amount"
        type: "number"
        description: ""

      - name: "transaction_amount_after_discount"
        type: "number"
        description: ""

      - name: "transaction_arr_amount"
        type: "number"
        description: ""

      - name: "transaction_billing_method"
        type: "string"
        description: ""

      - name: "transaction_conversion"
        type: "string"
        description: ""

      - name: "transaction_crm_opportunity_id"
        type: "string"
        description: ""

      - name: "transaction_crm_opportunity_line_item_id"
        type: "string"
        description: ""

      - name: "transaction_discount_amount"
        type: "number"
        description: ""

      - name: "transaction_duration"
        type: "string"
        description: ""

      - name: "transaction_effective_change_date"
        type: "date-time"
        description: ""

      - name: "transaction_effective_end_date"
        type: "date-time"
        description: ""

      - name: "transaction_end_date"
        type: "date-time"
        description: ""

      - name: "transaction_flagged"
        type: "string"
        description: ""

      - name: "transaction_foreign_exchange_rate"
        type: "number"
        description: ""

      - name: "transaction_generate_invoices"
        type: "boolean"
        description: ""

      - name: "transaction_generate_revenue"
        type: "boolean"
        description: ""

      - name: "transaction_ili_description"
        type: "string"
        description: ""

      - name: "transaction_ili_qb_class"
        type: "string"
        description: ""

      - name: "transaction_invoice_end_date"
        type: "date-time"
        description: ""

      - name: "transaction_invoice_quantity"
        type: "number"
        description: ""

      - name: "transaction_invoice_start_date"
        type: "date-time"
        description: ""

      - name: "transaction_item_class_name"
        type: "string"
        description: ""

      - name: "transaction_item_code"
        type: "string"
        description: ""

      - name: "transaction_item_name"
        type: "string"
        description: ""

      - name: "transaction_monthly_rate"
        type: "number"
        description: ""

      - name: "transaction_normalized_amount"
        type: "number"
        description: ""

      - name: "transaction_normalized_term"
        type: "string"
        description: ""

      - name: "transaction_notes"
        type: "string"
        description: ""

      - name: "transaction_number_field1"
        type: "number"
        description: ""

      - name: "transaction_number_field2"
        type: "number"
        description: ""

      - name: "transaction_order_date"
        type: "date-time"
        description: ""

      - name: "transaction_order_number"
        type: "string"
        description: ""

      - name: "transaction_quantity"
        type: "number"
        description: ""

      - name: "transaction_recognize"
        type: "boolean"
        description: ""

      - name: "transaction_renew_using_item"
        type: "string"
        description: ""

      - name: "transaction_renewal_amount"
        type: "number"
        description: ""

      - name: "transaction_renewal_amount_percentage"
        type: "number"
        description: ""

      - name: "transaction_renewal_duration"
        type: "string"
        description: ""

      - name: "transaction_renewal_factor"
        type: "string"
        description: ""

      - name: "transaction_renewal_probability"
        type: "number"
        description: ""

      - name: "transaction_renwal_quantity"
        type: "number"
        description: ""

      - name: "transaction_revenue_amount"
        type: "number"
        description: ""

      - name: "transaction_revenue_end_date"
        type: "date-time"
        description: ""

      - name: "transaction_revenue_recognition_method"
        type: "string"
        description: ""

      - name: "transaction_revenue_start_date"
        type: "date-time"
        description: ""

      - name: "transaction_sales_manager"
        type: "string"
        description: ""

      - name: "transaction_sales_rep"
        type: "string"
        description: ""

      - name: "transaction_sf_group_id"
        type: "string"
        description: ""

      - name: "transaction_sf_id"
        type: "string"
        description: ""

      - name: "transaction_sf_renewal_opportunity_rule"
        type: "string"
        description: ""

      - name: "transaction_start_date"
        type: "date-time"
        description: ""

      - name: "transaction_term_number"
        type: "integer"
        description: ""

      - name: "transaction_text_field1"
        type: "string"
        description: ""

      - name: "transaction_text_field2"
        type: "string"
        description: ""

      - name: "transaction_unbalanced_revenue_exemption"
        type: "boolean"
        description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "order_notes"
    type: "string"
    description: ""

  - name: "order_total"
    type: "string"
    description: ""

  - name: "project_name"
    type: "string"
    description: ""

  - name: "project_template"
    type: "string"
    description: ""

  - name: "quickbooks_job_account_number"
    type: "string"
    description: ""

  - name: "quickbooks_job_addr1"
    type: "string"
    description: ""

  - name: "quickbooks_job_addr2"
    type: "string"
    description: ""

  - name: "quickbooks_job_addr3"
    type: "string"
    description: ""

  - name: "quickbooks_job_alt_contact"
    type: "string"
    description: ""

  - name: "quickbooks_job_alt_phone"
    type: "string"
    description: ""

  - name: "quickbooks_job_city"
    type: "string"
    description: ""

  - name: "quickbooks_job_company_name"
    type: "string"
    description: ""

  - name: "quickbooks_job_contact"
    type: "string"
    description: ""

  - name: "quickbooks_job_country"
    type: "string"
    description: ""

  - name: "quickbooks_job_default_credit_memo_template"
    type: "string"
    description: ""

  - name: "quickbooks_job_default_invoice_template"
    type: "string"
    description: ""

  - name: "quickbooks_job_description"
    type: "string"
    description: ""

  - name: "quickbooks_job_email"
    type: "string"
    description: ""

  - name: "quickbooks_job_end_date"
    type: "date-time"
    description: ""

  - name: "quickbooks_job_fax"
    type: "string"
    description: ""

  - name: "quickbooks_job_first_name"
    type: "string"
    description: ""

  - name: "quickbooks_job_invoice_email_preference"
    type: "boolean"
    description: ""

  - name: "quickbooks_job_invoice_print_preference"
    type: "boolean"
    description: ""

  - name: "quickbooks_job_is_active"
    type: "boolean"
    description: ""

  - name: "quickbooks_job_last_name"
    type: "string"
    description: ""

  - name: "quickbooks_job_name"
    type: "string"
    description: ""

  - name: "quickbooks_job_payment_terms"
    type: "string"
    description: ""

  - name: "quickbooks_job_phone"
    type: "string"
    description: ""

  - name: "quickbooks_job_projected_end_date"
    type: "date-time"
    description: ""

  - name: "quickbooks_job_resale_number"
    type: "string"
    description: ""

  - name: "quickbooks_job_sales_rep"
    type: "string"
    description: ""

  - name: "quickbooks_job_salutation"
    type: "string"
    description: ""

  - name: "quickbooks_job_shipping_addr1"
    type: "string"
    description: ""

  - name: "quickbooks_job_shipping_addr2"
    type: "string"
    description: ""

  - name: "quickbooks_job_shipping_addr3"
    type: "string"
    description: ""

  - name: "quickbooks_job_shipping_city"
    type: "string"
    description: ""

  - name: "quickbooks_job_shipping_country"
    type: "string"
    description: ""

  - name: "quickbooks_job_shipping_state"
    type: "string"
    description: ""

  - name: "quickbooks_job_shipping_zip_code"
    type: "string"
    description: ""

  - name: "quickbooks_job_start_date"
    type: "date-time"
    description: ""

  - name: "quickbooks_job_state"
    type: "string"
    description: ""

  - name: "quickbooks_job_status"
    type: "string"
    description: ""

  - name: "quickbooks_job_type"
    type: "string"
    description: ""

  - name: "quickbooks_job_zip_code"
    type: "string"
    description: ""

  - name: "sales_order_id"
    type: "string"
    description: ""

  - name: "stage_name"
    type: "string"
    description: ""

  - name: "type"
    type: "string"
    description: ""
---