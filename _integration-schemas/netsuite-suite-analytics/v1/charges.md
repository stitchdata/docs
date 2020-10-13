---
tap: "netsuite-suite-analytics"
version: "1"
key: "charge"

name: "charges"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/charge.html"
description: |
  The `{{ table.name }}` table contains info about the charges in your Netsuite account, which represent billable amounts that your clients must pay.

  {{ integration.append-only-loading | flatify }}

replication-method: "Key-based Incremental"
loading-behavior: "Append-Only"

attributes:
  - name: "date_last_modified"
    type: "date-time"
    replication-key: true
    description: "The time the charge was last modified."

  - name: "charge_id"
    type: "integer"
    description: "The charge ID."
    foreign-key-id: "charge-id"

  - name: "amount"
    type: "number"
    description: "The amount of the charge."

  - name: "billing_account_id"
    type: "integer"
    description: "The billing account associated with the charge."

  - name: "billing_mode_id"
    type: "integer"
    description: "The billing mode of the charge."

  - name: "billing_schedule_id"
    type: "integer"
    description: "The billing schedule of the charge."
    foreign-key-id: "billing-schedule-id"

  - name: "category_0"
    type: "integer"
    description: "The category of the charge."

  - name: "charge_extid"
    type: "string"
    description: "The external ID of the charge."

  - name: "chargeemployee"
    type: "integer"
    description: "The employee of the charge."

  - name: "chargerule"
    type: "integer"
    description: "The rule of the charge."

  - name: "chargestage"
    type: "string"
    description: "The stage of the charge."

  - name: "chargetype"
    type: "integer"
    description: "The type of the charge."

  - name: "chargeuse"
    type: "string"
    description: "The use of the charge."

  - name: "class_0"
    type: "integer"
    description: "The class of the charge."

  - name: "currency"
    type: "integer"
    description: "The currency of the charge."

  - name: "customer"
    type: "integer"
    description: "The customer associated with the charge."

  - name: "date_0"
    type: "date-time"
    description: "The date of the charge in GMT."

  - name: "date_bill"
    type: "date-time"
    description: "The date of the bill associated with the charge in GMT."

  - name: "date_service_end"
    type: "date-time"
    description: "The end service date of the charge in GMT."

  - name: "date_service_start"
    type: "date-time"
    description: "The start service date of the charge in GMT."

  - name: "department"
    type: "integer"
    description: "The department associated with the charge."

  - name: "description"
    type: "string"
    description: "The description of the charge."

  - name: "group_order"
    type: "integer"
    description: "The group order of the charge."

  - name: "item"
    type: "integer"
    description: "The item associated with the charge."

  - name: "location_0"
    type: "integer"
    description: ""


  - name: "memo"
    type: "string"
    description: "The memo of the charge."

  - name: "quantity"
    type: "number"
    description: "The quantity of the charge."

  - name: "rate"
    type: "number"
    description: "The rate of the charge."

  - name: "run_id"
    type: "integer"
    description: "The run associated with the charge."

  - name: "sales_order"
    type: "integer"
    description: "The sales order associated with the charge."

  - name: "so_line"
    type: "integer"
    description: "The sales order of the line item associated with the charge."

  - name: "subscription_line_id"
    type: "integer"
    description: ""


  - name: "subsidiary_id"
    type: "integer"
    description: "The subsidiary associated with the charge."
    # foreign-key-id: "subsidiary-id"

  - name: "time_source"
    type: "integer"
    description: "The time source of the charges."

  - name: "unit_id"
    type: "integer"
    description: "The unit associated with the charge."
---