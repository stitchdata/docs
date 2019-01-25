---
tap: "netsuite"
# version: "10-15-2015"

name: "netsuite_deleted"
doc-link: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2016_1/schema/search/customerstatussearchbasic.html?mode=package
description: |
  The `{{ table.name }}` table contains info about deleted records.

replication-method: "Full Table"
abstract: true

permissions:
  - name: ""
    level: "View"
    location: ""

attributes:
  - name: "internalId"
    type: "integer"
    primary-key: true
    description: |
      The {{ table.name | remove: "netsuite_" | replace: "_"," " }} record ID.

  - name: "type"
    type: "string"
    primary-key: true
    description: "The type of record that was deleted. For example: `invoice`"

  - name: "deletedDate"
    type: "date-time"
    description: |
      The time the {{ table.name | remove: "netsuite_" | replace: "_"," " }} record was deleted.

  - name: "customRecord"
    type: "boolean"
    description: "Indicates if the deleted record was a custom record."

  - name: "name"
    type: "string"
    description: "The name of the record that was deleted. For example: `Invoice #INV197`"
---


