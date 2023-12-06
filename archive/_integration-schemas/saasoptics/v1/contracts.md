---
tap: "saasoptics"
version: "1"
key: "contract"

name: "contracts"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-saasoptics/blob/master/tap_saasoptics/schemas/contracts.json"
description: |
  The `{{ table.name }}` table contains info about the contracts in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
  name: "Contract List"
  doc-link: "https://saasoptics.zendesk.com/hc/en-us/articles/115013751607-Contracts-CRUD-"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: ""
    foreign-key-id: "contract-id"

  - name: "modified"
    type: "date-time"
    replication-key: true
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

      - name: "customer_type_ref_fullname"
        type: "string"
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

      - name: "job_description"
        type: "string"
        description: ""

      - name: "job_end_date"
        type: "date-time"
        description: ""

      - name: "job_projected_end_date"
        type: "date-time"
        description: ""

      - name: "job_start_date"
        type: "date-time"
        description: ""

      - name: "job_status"
        type: "string"
        description: ""

      - name: "job_type"
        type: "integer"
        description: ""

      - name: "last_name"
        type: "string"
        description: ""

      - name: "name"
        type: "string"
        description: ""

      - name: "parent_id"
        type: "string"
        description: ""

      - name: "payment_terms"
        type: "integer"
        description: ""
        foreign-key-id: "payment-term-id"

      - name: "phone"
        type: "string"
        description: ""

      - name: "resale_number"
        type: "string"
        description: ""

      - name: "sales_rep"
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

  - name: "channel"
    type: "string"
    description: ""

  - name: "customer"
    type: "integer"
    description: ""
    foreign-key-id: "customer-id"

  - name: "email"
    type: "string"
    description: ""

  - name: "entry_date"
    type: "date-time"
    description: ""

  - name: "is_job"
    type: "boolean"
    description: ""

  - name: "lead_date"
    type: "date-time"
    description: ""

  - name: "lead_source"
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

  - name: "qb_job_id"
    type: "string"
    description: ""

  - name: "register"
    type: "integer"
    description: ""
    foreign-key-id: "register-id"

  - name: "sf_id"
    type: "string"
    description: ""

  - name: "text_field1"
    type: "string"
    description: ""

  - name: "text_field2"
    type: "string"
    description: ""

  - name: "unbalanced_revenue_exception"
    type: "boolean"
    description: ""
---