---
tap: "bigcommerce"
version: "1.0"

name: "customers"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-bigcommerce/blob/master/tap_bigcommerce/schemas/customers.json"
description: |
  The `{{ table.name }}` table contains info about the customers in your {{ integration.display_name }} store.

replication-method: "Key-based Incremental"
api-method:
  name: "Get all customers"
  doc-link: "https://developer.bigcommerce.com/api-reference/customer-subscribers/customers-api/customers/getallcustomers"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The customer's ID."
    foreign-key-id: "customer-id"

  - name: "date_modified"
    type: "date-time"
    replication-key: true
    description: "The date the customer was last modified, in RFC 2822 format."

  - name: "accepts_marketing"
    type: "boolean"
    description: "Indicates whether the customer wants to receive marketing content from the store."

  - name: "company"
    type: "string"
    description: "The name of the company the customer works for."

  - name: "customer_group_id"
    type: "integer"
    description: "The group the customer belongs to."

  - name: "date_created"
    type: "date-time"
    description: "The date the customer was created, in RFC 2822 format."

  - name: "email"
    type: "string"
    description: "The customer's email address."

  - name: "first_name"
    type: "string"
    description: "The customer's first name."

  - name: "form_fields"
    type: "array"
    description: "Custom form fields associated with the customer."
    subattributes:
      - name: "name"
        type: "string"
        description: "The name of the form field."

      - name: "value"
        type: "string"
        description: "The value of the form field."

  - name: "last_name"
    type: "string"
    description: "The customer's last name."

  - name: "notes"
    type: "string"
    description: "Store-owner notes about the customer."

  - name: "phone"
    type: "string"
    description: "The customer's phone number."

  - name: "registration_ip_address"
    type: "string"
    description: "The customer's IP address when they signed up."

  - name: "reset_pass_on_login"
    type: "boolean"
    description: "Indicates if a password change will be forced on the customer's next login."

  - name: "store_credit"
    type: "number"
    description: "The amount of store credit the customer has."

  - name: "tax_exempt_category"
    type: "string"
    description: |
      Indicates the tax exempt category applied to the customer. This field can be blank, or can contain a single case-sensitive AvaTax code.

      Stores that subscribe to BigCommerce’s Avalara Premium integration will use this code to determine how/whether to apply sales tax. This doesn't affect sales-tax calculations for stores that do not subscribe to Avalara Premium.
---