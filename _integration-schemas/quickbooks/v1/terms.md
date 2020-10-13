---
tap: "quickbooks"
version: "1"
key: "term"

name: "terms"
doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/term"
singer-schema: "https://github.com/singer-io/tap-quickbooks/blob/master/tap_quickbooks/schemas/terms.json"
description: |
  The `{{ table.name }}` table contains info about the sale terms defined in your {{ integration.display_name }} instance. **Note**: Both active and inactive terms are included in the data for this table.

replication-method: "Key-based Incremental"

replication-key:
  name: "Metadata.LastUpdatedTime"

api-method:
  name: "Query a term"
  doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/term#query-a-term"

attributes:
  - name: "Id"
    type: "string"
    primary-key: true
    description: "The term ID."
    foreign-key-id: "term-id"

  - name: "Active"
    type: "boolean"
    description: ""

  - name: "DayOfMonthDue"
    type: "integer"
    description: ""

  - name: "DiscountDays"
    type: "integer"
    description: ""

  - name: "DiscountDayOfMonth"
    type: "integer"
    description: ""

  - name: "DiscountPercent"
    type: "number"
    description: ""

  - name: "domain"
    type: "string"
    description: ""

  - name: "DueDays"
    type: "integer"
    description: ""

  - name: "DueNextMonthDays"
    type: "integer"
    description: ""

  - name: "MetaData"
    type: "object"
    description: ""
    subattributes:
      - name: "CreateTime"
        type: "date-time"
        description: ""

      - name: "LastUpdatedTime"
        type: "date-time"
        description: ""

  - name: "Name"
    type: "string"
    description: ""

  - name: "SyncToken"
    type: "string"
    description: ""

  - name: "Type"
    type: "string"
    description: ""
---