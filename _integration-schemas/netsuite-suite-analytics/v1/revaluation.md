---
tap: "netsuite-suite-analytics"
version: "1"
key: "revaluation"

name: "revaluation"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/revaluation.html"
description: ""

replication-method: "Full Table"
loading-behavior: "Append-Only"

attributes:
  - name: "account_id"
    type: "integer"
    description: ""

  - name: "balance"
    type: "integer"
    description: ""

  - name: "curr_fx_rate"
    type: "number"
    description: ""

  - name: "currency_id"
    type: "integer"
    description: ""

  - name: "entity_id"
    type: "integer"
    description: ""

  - name: "fx_balance"
    type: "number"
    description: ""

  - name: "is_tax_reg_override"
    type: "string"
    description: ""

  - name: "last_sales_activity"
    type: "date-time"
    description: ""

  - name: "legal_name"
    type: "string"
    description: ""

  - name: "lsa_link"
    type: "string"
    description: ""

  - name: "lsa_link_name"
    type: "string"
    description: ""

  - name: "net_variance"
    type: "number"
    description: ""

  - name: "prior_variance"
    type: "integer"
    description: ""

  - name: "promotion_code_instance_id"
    type: "integer"
    description: ""

  - name: "reval_class"
    type: "integer"
    description: ""

  - name: "reval_department"
    type: "integer"
    description: ""

  - name: "reval_line_id"
    type: "integer"
    description: ""

  - name: "reval_location"
    type: "integer"
    description: ""

  - name: "reval_memo"
    type: "string"
    description: ""

  - name: "reval_tran_id"
    type: "integer"
    description: ""

  - name: "reval_tran_period_id"
    type: "integer"
    description: ""

  - name: "reval_type"
    type: "string"
    description: ""

  - name: "subsidiary_id"
    type: "integer"
    description: ""

  - name: "tax_reg_id"
    type: "integer"
    description: ""

  - name: "total_variance"
    type: "integer"
    description: ""

  - name: "tran_date"
    type: "date-time"
    description: ""

  - name: "tran_fx_rate"
    type: "number"
    description: ""

  - name: "tran_id"
    type: "integer"
    description: ""

  - name: "variance"
    type: "number"
    description: ""

  - name: "variance_account_id"
    type: "integer"
    description: ""
    foreign-key-id: "account-id"
---