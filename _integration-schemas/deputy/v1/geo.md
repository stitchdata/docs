---
tap: "deputy"
version: "1"
key: "geo"

name: "geo"
doc-link: "https://www.deputy.com/api-doc/Resources/Geo"

description: |
  The `{{ table.name }}` table contains info about geographic locations.

replication-method: "Key-based Incremental"

attributes:
  - name: "Modified"
    type: "integer"
    primary-key: true
    description: "The geo ID."
    #foreign-key-id: "geo-id"

  - name: "Modified"
    type: "date-time"
    replication-key: true
    description: "The time the geo was last modified."

  - name: "Orm"
    type: "string"
    description: ""

  - name: "RecId"
    type: "integer"
    description: ""

  - name: "Longitude"
    type: "string"
    description: ""

  - name: "Latitude"
    type: "string"
    description: ""

  - name: "No"
    type: "string"
    description: ""

  - name: "Street"
    type: "string"
    description: ""

  - name: "Suburb"
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
    foreign-key-id: "country-id"

  - name: "Creator"
    type: "integer"
    description: ""
    foreign-key-id: "employee-id"

  - name: "Created"
    type: "date-time"
    description: ""
---