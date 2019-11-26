---
tap: "deputy"
version: "1.0"
key: "address"

name: "addresses"
doc-link: "https://www.deputy.com/api-doc/Resources/Address"

description: |
  The `{{ table.name }}` table contains info about addresses.

replication-method: "Key-based Incremental"

attributes:
  - name: "Modified"
    type: "integer"
    primary-key: true
    description: "The address ID."
    foreign-key-id: "address-id"

  - name: "Modified"
    type: "date-time"
    replication-key: true
    description: "The time the address was last modified."

  - name: "ContactName"
    type: "string"
    description: ""

  - name: "UnitNo"
    type: "string"
    description: ""

  - name: "StreetNo"
    type: "string"
    description: ""

  - name: "SuiteNo"
    type: "string"
    description: ""

  - name: "PoBox"
    type: "string"
    description: ""

  - name: "Street1"
    type: "string"
    description: ""

  - name: "Street2"
    type: "string"
    description: ""

  - name: "City"
    type: "string"
    description: ""

  - name: "State"
    type: "string"
    description: ""

  - name: "Postcode"
    type: "string"
    description: ""

  - name: "Country"
    type: "integer"
    description: ""

  - name: "Phone"
    type: "string"
    description: ""

  - name: "Notes"
    type: "string"
    description: ""

  - name: "Format"
    type: "integer"
    description: ""

  - name: "Saved"
    type: "boolean"
    description: ""

  - name: "Creator"
    type: "integer"
    description: ""
    foreign-key-id: "employee-id"

  - name: "Created"
    type: "date-time"
    description: ""
---