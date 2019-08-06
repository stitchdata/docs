---
tap: "deputy"
version: "1.0"
key: "country"

name: "countries"
doc-link: "https://www.deputy.com/api-doc/Resources/Country"

description: |
  The `{{ table.name }}` table contains info about countries.

replication-method: "Key-based Incremental"

attributes:
  - name: "Modified"
    type: "integer"
    primary-key: true
    description: "The country ID."
    foreign-key-id: "country-id"

  - name: "Modified"
    type: "date-time"
    replication-key: true
    description: "The time the country was last modified."

  - name: "Code"
    type: "string"
    description: ""

  - name: "CodeA3"
    type: "string"
    description: ""

  - name: "Region"
    type: "string"
    description: ""

  - name: "Active"
    type: "boolean"
    description: ""

  - name: "SortOrder"
    type: "integer"
    description: ""

  - name: "Country"
    type: "string"
    description: ""

  - name: "ZipVAlidatePreg"
    type: "string"
    description: ""

  - name: "PhoneDisplayPreg"
    type: "string"
    description: ""

  - name: "Creator"
    type: "integer"
    description: ""
    foreign-key-id: "employee-id"

  - name: "Created"
    type: "date-time"
    description: ""
---