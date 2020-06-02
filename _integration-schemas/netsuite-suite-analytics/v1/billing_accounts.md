---
tap: "netsuite-suite-analytics"
version: "1"
key: "billing-account"

name: "billing_accounts"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/billingaccount.html"
description: |
  The `{{ table.name }}` table contains info about the billing accounts in your NetSuite account. A billing account is a record used to show all billing information for a customer or subcustomer. A billing account contains billing-specific information, including billing schedule, default payment terms, bill-to address, and currency.

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
    description: "The time the billing account was last modified."

  - name: "billing_account_id"
    type: "integer"
    netsuite-primary-key: true
    description: "The billing account ID. {{ integration.netsuite-primary-key-description | flatify }}"
    foreign-key-id: "billing-account-id"

  - name: "address_book_id"
    type: "integer"
    description: "The address book associated with the billing account."
    # foreign-key-id: "address-book-id"

  - name: "bill_to_address_book_id"
    type: "integer"
    description: "The bill to address book for the billing account."
    foreign-key-id: "address-book-id"

  - name: "billing_account_extid"
    type: "integer"
    description: "The billing account's external ID."

  - name: "billing_account_memo"
    type: "string"
    description: "Memo for the billing account."

  - name: "billing_account_name"
    type: "string"
    description: "The name of the billing account."

  - name: "billing_account_number"
    type: "string"
    description: "The billing account number."

  - name: "billing_schedule_id"
    type: "integer"
    description: "The billing schedule for the billing account."
    foreign-key-id: "billing-schedule-id"

  - name: "class_id"
    type: "integer"
    description: "The class for the billing account."
    # foreign-key-id: "class-id"

  - name: "currency_id"
    type: "integer"
    description: "The currency for the billing account."
    # foreign-key-id: "currency-id"

  - name: "customer_id"
    type: "integer"
    description: "The customer for the billing account."
    # foreign-key-id: "customer-id"

  - name: "date_created"
    type: "date-time"
    description: "The date the billing account was created."

  - name: "date_last_actual_bill"
    type: "date-time"
    description: "The date of the last actual bill for the billing account."

  - name: "date_last_bill_cycle"
    type: "date-time"
    description: "The date of the last bill cycle for the billing account."

  - name: "date_next_bill_cycle"
    type: "date-time"
    description: "The date of the next bill cycle for the billing account."

  - name: "date_start"
    type: "date-time"
    description: "The start date of the billing account."

  - name: "department_id"
    type: "integer"
    description: "The department of the billing account."
    # foreign-key-id: "department-id"

  - name: "has_off_cycle_bill_request"
    type: "string"
    description: "Whether off-cycle billing is used for the billing account."

  - name: "is_customer_default"
    type: "string"
    description: "Whether the customer is the default for the billing account."

  - name: "is_inactive"
    type: "string"
    description: "Whether the billing account is inactive."

  - name: "location_id"
    type: "integer"
    description: "The location of the billing account."
    # foreign-key-id: "location-id"

  - name: "ship_to_address_book_id"
    type: "integer"
    description: "The ship to address book for the billing account."
    foreign-key-id: "address-book-id"
---