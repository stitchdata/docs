---
tap: "netsuite"
version: "1.0"

name: "RevRecTemplate"
doc-link: "https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2017_2/schema/record/revrectemplate.html"
# singer-schema: "https://github.com/singer-io/tap-netsuite/blob/master/tap_netsuite/schemas/RevRecTemplate.json"
description: |
  The `{{ table.name }}` table contains info about the revenue recognition templates in your {{ integration.display_name }} account. A revenue recognition template indicates how revenue from associated items should be posted.

  {{ integration.permission-for-table | flatify }}

## Refer to _data/extraction/netsuite/netsuite-permissions.yml for permissions for this table/object.
key: "rev-rec-template"

replication-method: "Full Table"

attributes:
  - name: "internalId"
    type: "string"
    primary-key: true
    description: ""
    # foreign-key-id: "revenue-recognition-template-id"

  - name: "amortizationPeriod"
    type: "integer, string"
    description: ""

  - name: "amortizationType"
    type: "varies"
    description: ""

  - name: "externalId"
    type: "string"
    description: ""

  - name: "initialAmount"
    type: "number, string"
    description: ""

  - name: "isInactive"
    type: "boolean, string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "nullFieldList"
    type: "varies"
    description: ""

  - name: "periodOffset"
    type: "integer, string"
    description: ""

  - name: "recogIntervalSrc"
    type: "varies"
    description: ""

  - name: "recurrenceList"
    type: "varies"
    description: ""

  - name: "recurrenceType"
    type: "varies"
    description: ""

  - name: "revRecOffset"
    type: "integer, string"
    description: ""
---