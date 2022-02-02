---
tap: "chargify"
version: "1"
key: "customer"

name: "customers"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-chargify/blob/master/tap_chargify/schemas/customers.json"
description: |
  The `{{ table.name }}` table contains info about customers associated with your {{ integration.display_name }} site.

replication-method: "Full Table"

api-method:
  name: "Read customers for a site"
  doc-link: "https://reference.chargify.com/v1/customers/list-customers-for-a-site"
  
attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The customer ID."
    foreign-key-id: "customer-id"

  - name: "address"
    type: "string"
    description: ""

  - name: "address_2"
    type: "string"
    description: ""

  - name: "cc_emails"
    type: "string"
    description: ""

  - name: "city"
    type: "string"
    description: ""

  - name: "country"
    type: "string"
    description: ""

  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "first_name"
    type: "string"
    description: ""

  - name: "last_name"
    type: "string"
    description: ""

  - name: "organization"
    type: "string"
    description: ""

  - name: "parent_id"
    type: "integer"
    description: ""
    foreign-key-id: "customer-id"

  - name: "phone"
    type: "string"
    description: ""

  - name: "portal_customer_created_at"
    type: "date-time"
    description: ""

  - name: "portal_invite_last_accepted_at"
    type: "date-time"
    description: ""

  - name: "portal_invite_last_sent_at"
    type: "date-time"
    description: ""

  - name: "reference"
    type: "integer"
    description: ""

  - name: "state"
    type: "string"
    description: ""

  - name: "tax_exempt"
    type: "boolean"
    description: ""

  - name: "updated_at"
    type: "date-time"
    description: ""

  - name: "vat_number"
    type: "string"
    description: ""

  - name: "verified"
    type: "boolean"
    description: ""

  - name: "zip"
    type: "string"
    description: ""
---