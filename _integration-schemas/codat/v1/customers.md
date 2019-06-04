---
tap: "codat"
version: "1.0"
key: "customer"

name: "customers"
doc-link: "https://docs.codat.io/reference/customers"
singer-schema: "https://github.com/singer-io/tap-codat/blob/master/tap_codat/schemas/customers.json"
description: |
  The `{{ table.name }}` table contains info about the customers in your {{ integration.display_name }} instance. A customer is a person or organisation that buys goods or services.

replication-method: "Full Table"

api-method:
    name: "List customers"
    doc-link: "https://docs.codat.io/reference/customers#customers_listpaged"

attributes:
  - name: "companyId"
    type: "string"
    primary-key: true
    description: "The ID of the company associated with the customer."
    foreign-key-id: "company-id"

  - name: "id"
    type: "string"
    primary-key: true
    description: "The customer ID."
    foreign-key-id: "customer-id"

  - name: "addresses"
    type: "array"
    description: "A list of addresses associated with the customer."
    subattributes: &address
      - name: "city"
        type: "string"
        description: "The city."

      - name: "country"
        type: "string"
        description: "The country."

      - name: "line1"
        type: "string"
        description: "The first address line."

      - name: "line2"
        type: "string"
        description: "The second address line."

      - name: "postalCode"
        type: "string"
        description: "The zip or postal code."

      - name: "region"
        type: "string"
        description: "The region."

      - name: "type"
        type: "string"
        description: |
          The type of the address. Possible values are:

          - `Billing`
          - `Delivery`
          - `Unknown`

  - name: "contactName"
    type: "string"
    description: "The name of the main contact for the customer."

  - name: "contacts"
    type: "array"
    description: "An array of contacts associated with the customer."
    subattributes:
      - name: "address"
        type: "object"
        description: "The contact's address."
        subattributes: *address

      - name: "email"
        type: "string"
        description: "The contact's email address."

      - name: "modifiedDate"
        type: "date-time"
        description: "The time the contact was last modified."

      - name: "name"
        type: "string"
        description: "The contact's name."

      - name: "phone"
        type: "array"
        description: "A list of phone numbers for the contact."
        subattributes:
          - name: "number"
            type: "string"
            description: "The phone number."

          - name: "type"
            type: "string"
            description: |
              The type of phone number. Possible values are:

              - `Primary`
              - `Landline`
              - `Mobile`
              - `Fax`
              - `Unknown`

      - name: "status"
        type: "string"
        description: &status |
          The status. Possible values are:

          - `Active`
          - `Archived`
          - `Unknown`

  - name: "customerName"
    type: "string"
    description: "The name of the customer."

  - name: "defaultCurrency"
    type: "string"
    description: "The default currency the customer's transactional data is recorded in."

  - name: "emailAddress"
    type: "string"
    description: "The customer's email address."

  - name: "modifiedDate"
    type: "date-time"
    description: "The time the customer was last modified."

  - name: "phone"
    type: "string"
    description: "The phone number for the contact."

  - name: "registrationNumber"
    type: "string"
    description: "The company number."

  - name: "status"
    type: "string"
    description: *status

  - name: "taxNumber"
    type: "string"
    description: "The company tax number."
---