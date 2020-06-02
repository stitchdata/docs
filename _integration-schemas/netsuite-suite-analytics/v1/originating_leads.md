---
tap: "netsuite-suite-analytics"
version: "1"
key: "originating-lead"

name: "originating_leads"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/originatinglead.html"
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

  - name: "accountnumber"
    type: "string"
    description: ""

  - name: "altemail"
    type: "string"
    description: ""

  - name: "alternate_contact_id"
    type: "integer"
    description: ""

  - name: "altphone"
    type: "string"
    description: ""

  - name: "amount_complete"
    type: "number"
    description: ""

  - name: "billaddress"
    type: "string"
    description: ""

  - name: "calculated_end"
    type: "date-time"
    description: ""

  - name: "category_0"
    type: "string"
    description: ""

  - name: "city"
    type: "string"
    description: ""

  - name: "comments"
    type: "string"
    description: ""

  - name: "companyname"
    type: "string"
    description: ""

  - name: "consol_days_overdue"
    type: "integer"
    description: ""

  - name: "consol_deposit_balance"
    type: "integer"
    description: ""

  - name: "consol_deposit_balance_foreign"
    type: "integer"
    description: ""

  - name: "consol_openbalance"
    type: "integer"
    description: ""

  - name: "consol_openbalance_foreign"
    type: "integer"
    description: ""

  - name: "consol_unbilled_orders"
    type: "integer"
    description: ""

  - name: "consol_unbilled_orders_foreign"
    type: "integer"
    description: ""

  - name: "converted_to_contact_id"
    type: "integer"
    description: ""

  - name: "converted_to_id"
    type: "integer"
    description: ""

  - name: "cost_estimate"
    type: "number"
    description: ""

  - name: "country"
    type: "string"
    description: ""

  - name: "create_date"
    type: "date-time"
    description: ""

  - name: "credithold"
    type: "string"
    description: ""

  - name: "creditlimit"
    type: "number"
    description: ""

  - name: "currency_id"
    type: "integer"
    description: ""

  - name: "customer_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""

  - name: "customer_type_id"
    type: "integer"
    description: ""

  - name: "date_closed"
    type: "date-time"
    description: ""

  - name: "date_convsersion"
    type: "date-time"
    description: ""

  - name: "date_first_order"
    type: "date-time"
    description: ""

  - name: "date_first_sale"
    type: "date-time"
    description: ""

  - name: "date_gross_lead"
    type: "date-time"
    description: ""

  - name: "date_last_order"
    type: "date-time"
    description: ""

  - name: "date_last_sale"
    type: "date-time"
    description: ""

  - name: "date_lead"
    type: "date-time"
    description: ""

  - name: "date_prospect"
    type: "date-time"
    description: ""

  - name: "days_overdue"
    type: "integer"
    description: ""

  - name: "default_order_priority"
    type: "number"
    description: ""

  - name: "default_receivables_account_id"
    type: "integer"
    description: ""

  - name: "deposit_balance"
    type: "number"
    description: ""

  - name: "deposit_balance_foreign"
    type: "integer"
    description: ""

  - name: "email"
    type: "string"
    description: ""

  - name: "expected_close"
    type: "date-time"
    description: ""

  - name: "fax"
    type: "string"
    description: ""

  - name: "first_sale_period_id"
    type: "integer"
    description: ""

  - name: "first_visit"
    type: "date-time"
    description: ""

  - name: "firstname"
    type: "string"
    description: ""

  - name: "full_name"
    type: "string"
    description: ""

  - name: "home_phone"
    type: "string"
    description: ""

  - name: "is_exempt_time"
    type: "string"
    description: ""

  - name: "is_explicit_conversion"
    type: "string"
    description: ""

  - name: "is_job"
    type: "string"
    description: ""

  - name: "is_person"
    type: "string"
    description: ""

  - name: "is_productive_time"
    type: "string"
    description: ""

  - name: "is_utilized_time"
    type: "string"
    description: ""

  - name: "isemailhtml"
    type: "string"
    description: ""

  - name: "isemailpdf"
    type: "string"
    description: ""

  - name: "isinactive"
    type: "string"
    description: ""

  - name: "istaxable"
    type: "string"
    description: ""

  - name: "job_end"
    type: "date-time"
    description: ""

  - name: "job_start"
    type: "date-time"
    description: ""

  - name: "job_type_id"
    type: "integer"
    description: ""

  - name: "last_modified_date"
    type: "date-time"
    description: ""

  - name: "last_sale_period_id"
    type: "integer"
    description: ""

  - name: "last_sales_activity"
    type: "date-time"
    description: ""

  - name: "last_visit"
    type: "date-time"
    description: ""

  - name: "lastname"
    type: "string"
    description: ""

  - name: "lead_source_id"
    type: "integer"
    description: ""

  - name: "line1"
    type: "string"
    description: ""

  - name: "line2"
    type: "string"
    description: ""

  - name: "line3"
    type: "string"
    description: ""

  - name: "loginaccess"
    type: "string"
    description: ""

  - name: "lsa_link"
    type: "string"
    description: ""

  - name: "lsa_link_name"
    type: "string"
    description: ""

  - name: "middlename"
    type: "string"
    description: ""

  - name: "mobile_phone"
    type: "string"
    description: ""

  - name: "multiple_price_id"
    type: "integer"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "openbalance"
    type: "integer"
    description: ""

  - name: "openbalance_foreign"
    type: "integer"
    description: ""

  - name: "parent_id"
    type: "integer"
    description: ""

  - name: "partner_id"
    type: "integer"
    description: ""

  - name: "payment_terms_id"
    type: "integer"
    description: ""

  - name: "phone"
    type: "string"
    description: ""

  - name: "primary_contact_id"
    type: "integer"
    description: ""

  - name: "print_on_check_as"
    type: "string"
    description: ""

  - name: "probability"
    type: "number"
    description: ""

  - name: "projected_end"
    type: "date-time"
    description: ""

  - name: "referrer"
    type: "string"
    description: ""

  - name: "reminderdays"
    type: "integer"
    description: ""

  - name: "renewal"
    type: "date-time"
    description: ""

  - name: "resalenumber"
    type: "string"
    description: ""

  - name: "rev_rec_forecast_rule_id"
    type: "integer"
    description: ""

  - name: "rev_rec_forecast_template"
    type: "integer"
    description: ""

  - name: "revenue_estimate"
    type: "number"
    description: ""

  - name: "sales_rep_id"
    type: "integer"
    description: ""

  - name: "sales_territory_id"
    type: "integer"
    description: ""

  - name: "salutation"
    type: "string"
    description: ""

  - name: "ship_complete"
    type: "string"
    description: ""

  - name: "shipaddress"
    type: "string"
    description: ""

  - name: "state"
    type: "string"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "status_descr"
    type: "string"
    description: ""

  - name: "status_probability"
    type: "number"
    description: ""

  - name: "status_read_only"
    type: "string"
    description: ""

  - name: "stitch_custom_field"
    type: "number"
    description: ""

  - name: "stitch_custom_field_check_box"
    type: "string"
    description: ""

  - name: "stitch_custom_field_currency"
    type: "number"
    description: ""

  - name: "stitch_custom_field_decimal"
    type: "number"
    description: ""

  - name: "subsidiary_id"
    type: "integer"
    description: ""

  - name: "tax_item_id"
    type: "integer"
    description: ""

  - name: "third_party_acct"
    type: "string"
    description: ""

  - name: "third_party_carrier"
    type: "string"
    description: ""

  - name: "third_party_country"
    type: "string"
    description: ""

  - name: "third_party_zip_code"
    type: "string"
    description: ""

  - name: "top_level_parent_id"
    type: "integer"
    description: ""
    foreign-key-id: "customer-id"

  - name: "unbilled_orders"
    type: "number"
    description: ""

  - name: "unbilled_orders_foreign"
    type: "integer"
    description: ""

  - name: "url"
    type: "string"
    description: ""

  - name: "use_percent_complete_override"
    type: "string"
    description: ""

  - name: "web_lead"
    type: "string"
    description: ""

  - name: "zipcode"
    type: "string"
    description: ""
---