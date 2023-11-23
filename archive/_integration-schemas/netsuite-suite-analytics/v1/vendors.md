---
tap: "netsuite-suite-analytics"
version: "1"
key: "vendor"

name: "vendors"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/vendor.html"
description: |
  {{ integration.netsuite-replication-keys | flatify }}

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

  - name: "accountnumber"
    type: "string"
    description: ""

  - name: "altemail"
    type: "string"
    description: ""

  - name: "altphone"
    type: "string"
    description: ""

  - name: "billaddress"
    type: "string"
    description: ""

  - name: "billing_class_id"
    type: "integer"
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

  - name: "country"
    type: "string"
    description: ""

  - name: "create_date"
    type: "date-time"
    description: ""

  - name: "creditlimit"
    type: "number"
    description: ""

  - name: "currency_id"
    type: "integer"
    description: ""

  - name: "email"
    type: "string"
    description: ""

  - name: "expense_account_id"
    type: "integer"
    description: ""

  - name: "fax"
    type: "string"
    description: ""

  - name: "full_name"
    type: "string"
    description: ""

  - name: "home_phone"
    type: "string"
    description: ""

  - name: "in_transit_balance"
    type: "integer"
    description: ""

  - name: "incoterm"
    type: "string"
    description: ""

  - name: "is1099eligible"
    type: "string"
    description: ""

  - name: "is_person"
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

  - name: "labor_cost"
    type: "integer"
    description: ""

  - name: "last_sales_activity"
    type: "date-time"
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

  - name: "mobile_phone"
    type: "string"
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

  - name: "payables_account_id"
    type: "integer"
    description: ""

  - name: "payment_terms_id"
    type: "integer"
    description: ""

  - name: "phone"
    type: "string"
    description: ""

  - name: "printoncheckas"
    type: "string"
    description: ""

  - name: "purchaseorderamount"
    type: "number"
    description: ""

  - name: "purchaseorderquantity"
    type: "number"
    description: ""

  - name: "purchaseorderquantitydiff"
    type: "number"
    description: ""

  - name: "receiptamount"
    type: "number"
    description: ""

  - name: "receiptquantity"
    type: "number"
    description: ""

  - name: "receiptquantitydiff"
    type: "number"
    description: ""

  - name: "represents_subsidiary_id"
    type: "integer"
    description: ""
    foreign-key-id: "subsidiary-id"

  - name: "shipaddress"
    type: "string"
    description: ""

  - name: "state"
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

  - name: "subsidiary"
    type: "integer"
    description: ""
    foreign-key-id: "subsidiary-id"

  - name: "taxidnum"
    type: "string"
    description: ""

  - name: "time_approver_id"
    type: "integer"
    description: ""
    foreign-key-id: "employee-id"

  - name: "unbilled_orders"
    type: "integer"
    description: ""

  - name: "unbilled_orders_foreign"
    type: "integer"
    description: ""

  - name: "url"
    type: "string"
    description: ""

  - name: "vendor_extid"
    type: "string"
    description: ""

  - name: "vendor_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "vendor-id"

  - name: "vendor_type_id"
    type: "integer"
    description: ""
    foreign-key-id: "vendor-type-id"

  - name: "zipcode"
    type: "string"
    description: ""
---