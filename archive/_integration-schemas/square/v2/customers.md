---
tap: "square"
version: "2"
key: "square"

name: "customers"
doc-link: "https://developer.squareup.com/reference/square/customers-api/list-customers"
singer-schema: "https://github.com/singer-io/tap-square/blob/master/tap_square/schemas/customers.json"
description: |
  The `{{ table.name }}` contains information about customer profiles associated with your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
  name: "List customers (v2)"
  doc-link: "https://developer.squareup.com/reference/square/customers-api/list-customers"

attributes:
attributes:
  - name: "address"
    type: "object"
    description: ""
    subattributes:
    - name: "locality"
      type: "string"
      description: ""

    - name: "sublocality"
      type: "string"
      description: ""

    - name: "sublocality_2"
      type: "string"
      description: ""

    - name: "sublocality_3"
      type: "string"
      description: ""

    - name: "administrative_district_level_1"
      type: "string"
      description: ""

    - name: "administrative_district_level_2"
      type: "string"
      description: ""

    - name: "administrative_district_level_3"
      type: "string"
      description: ""

    - name: "country"
      type: "string"
      description: ""

    - name: "address_line_1"
      type: "string"
      description: ""

    - name: "address_line_2"
      type: "string"
      description: ""

    - name: "address_line_3"
      type: "string"
      description: ""

    - name: "postal_code"
      type: "string"
      description: ""

    - name: "first_name"
      type: "string"
      description: ""

    - name: "last_name"
      type: "string"
      description: ""


  - name: "birthday"
    type: "date-time"
    description: ""


  - name: "birthday"
    type: "string"
    description: ""


  - name: "company_name"
    type: "string"
    description: ""

  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "creation_source"
    type: "string"
    description: ""

  - name: "email_address"
    type: "string"
    description: ""

  - name: "family_name"
    type: "string"
    description: ""

  - name: "given_name"
    type: "string"
    description: ""

  - name: "group_ids"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "id"
    type: "string"
    description: ""

  - name: "nickname"
    type: "string"
    description: ""

  - name: "note"
    type: "string"
    description: ""

  - name: "phone_number"
    type: "string"
    description: ""

  - name: "preferences"
    type: "object"
    description: ""
    subattributes:
    - name: "email_unsubscribed"
      type: "boolean"
      description: ""


  - name: "reference_id"
    type: "string"
    description: ""

  - name: "segment_ids"
    type: "array"
    description: ""
    subattributes:
    - name: "items"
      type: "string"
      description: ""

  - name: "tax_ids"
    type: "object"
    description: ""
    subattributes:
    - name: "eu_vat"
      type: "string"
      description: ""


  - name: "updated_at"
    type: "date-time"
    description: ""
    replication-key: true

  - name: "version"
    type: "integer"
    description: ""
---