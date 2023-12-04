---
tap: "saasoptics"
version: "1"
key: "customer"

name: "customers"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-saasoptics/blob/master/tap_saasoptics/schemas/customers.json"
description: |
  The `{{ table.name }}` table contains info about customers.

replication-method: "Key-based Incremental"

api-method:
  name: "Customer List"
  doc-link: "https://saasoptics.zendesk.com/hc/en-us/articles/115013751587-Customers-CRUD-"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: ""
    foreign-key-id: "customer-id"

  - name: "modified"
    type: "date-time"
    replication-key: true
    description: ""

  - name: "autopay_enrollment"
    type: "string"
    description: ""

  - name: "billing_profile"
    type: "object"
    description: ""
    subattributes:
      - name: "account_number"
        type: "string"
        description: ""

      - name: "addr1"
        type: "string"
        description: ""

      - name: "addr2"
        type: "string"
        description: ""

      - name: "addr3"
        type: "string"
        description: ""

      - name: "alt_contact"
        type: "string"
        description: ""

      - name: "alt_phone"
        type: "string"
        description: ""

      - name: "avatax_address_validation_timestamp"
        type: "date-time"
        description: ""

      - name: "city"
        type: "string"
        description: ""

      - name: "company_name"
        type: "string"
        description: ""

      - name: "contact"
        type: "string"
        description: ""

      - name: "country"
        type: "string"
        description: ""

      - name: "currency"
        type: "integer"
        description: ""

      - name: "customer_type"
        type: "integer"
        description: ""

      - name: "default_class"
        type: "integer"
        description: ""

      - name: "default_credit_memo_template"
        type: "integer"
        description: ""

      - name: "default_invoice_template"
        type: "integer"
        description: ""

      - name: "edit_sequence"
        type: "string"
        description: ""

      - name: "email"
        type: "string"
        description: ""

      - name: "entity_use_code"
        type: "integer"
        description: ""

      - name: "fax"
        type: "string"
        description: ""

      - name: "first_name"
        type: "string"
        description: ""

      - name: "full_name"
        type: "string"
        description: ""

      - name: "invoice_email_preference"
        type: "boolean"
        description: ""

      - name: "invoice_print_preference"
        type: "boolean"
        description: ""

      - name: "is_active"
        type: "boolean"
        description: ""

      - name: "item_sales_tax"
        type: "integer"
        description: ""

      - name: "last_name"
        type: "string"
        description: ""

      - name: "last_updated_by_qb"
        type: "boolean"
        description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "payment_method"
        type: "integer"
        description: ""

      - name: "payment_terms"
        type: "integer"
        description: ""

      - name: "phone"
        type: "string"
        description: ""

      - name: "resale_number"
        type: "string"
        description: ""

      - name: "sales_rep"
        type: "integer"
        description: ""

      - name: "sales_rep_fullname"
        type: "string"
        description: ""

      - name: "sales_tax_code"
        type: "integer"
        description: ""

      - name: "salutation"
        type: "string"
        description: ""

      - name: "shipping_addr1"
        type: "string"
        description: ""

      - name: "shipping_addr2"
        type: "string"
        description: ""

      - name: "shipping_addr3"
        type: "string"
        description: ""

      - name: "shipping_city"
        type: "string"
        description: ""

      - name: "shipping_country"
        type: "string"
        description: ""

      - name: "shipping_state"
        type: "string"
        description: ""

      - name: "shipping_zip_code"
        type: "string"
        description: ""

      - name: "state"
        type: "string"
        description: ""

      - name: "zip_code"
        type: "string"
        description: ""

  - name: "cc_email"
    type: "string"
    description: ""

  - name: "code"
    type: "string"
    description: ""

  - name: "crm_id"
    type: "string"
    description: ""

  - name: "default_autorenewal_profile"
    type: "string"
    description: ""

  - name: "default_email_from_so"
    type: "boolean"
    description: ""

  - name: "default_enable_ach_payment"
    type: "boolean"
    description: ""

  - name: "default_enable_cc_payment"
    type: "boolean"
    description: ""

  - name: "default_theme"
    type: "integer"
    description: ""

  - name: "do_not_sync"
    type: "boolean"
    description: ""

  - name: "einvoicing_id"
    type: "string"
    description: ""

  - name: "email"
    type: "string"
    description: ""

  - name: "enable_autopay"
    type: "boolean"
    description: ""

  - name: "escalation_email"
    type: "string"
    description: ""

  - name: "industry"
    type: "string"
    description: ""

  - name: "is_active"
    type: "boolean"
    description: ""

  - name: "market"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "notes"
    type: "string"
    description: ""

  - name: "number"
    type: "string"
    description: ""

  - name: "number_field1"
    type: "number"
    description: ""

  - name: "number_field2"
    type: "number"
    description: ""

  - name: "number_field3"
    type: "number"
    description: ""

  - name: "parent"
    type: "integer"
    description: ""

  - name: "qb_id"
    type: "string"
    description: ""

  - name: "recurly_id"
    type: "string"
    description: ""

  - name: "segment"
    type: "string"
    description: ""

  - name: "sf_default_renewal_opportunity_rule"
    type: "integer"
    description: ""

  - name: "sf_id"
    type: "string"
    description: ""

  - name: "sf_opportunity_price_book_id"
    type: "string"
    description: ""

  - name: "sf_owner_id"
    type: "string"
    description: ""

  - name: "stripe_id"
    type: "string"
    description: ""

  - name: "subsegment"
    type: "string"
    description: ""

  - name: "text_field1"
    type: "string"
    description: ""

  - name: "text_field2"
    type: "string"
    description: ""

  - name: "text_field3"
    type: "string"
    description: ""

  - name: "unbalanced_revenue_exception"
    type: "boolean"
    description: ""
---