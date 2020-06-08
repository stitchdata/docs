---
tap: "netsuite-suite-analytics"
version: "1"
key: "bom-revision"

name: "bom_revisions"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/bomrevision.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "bill_of_materials_id"
    type: "integer"
    description: ""
    foreign-key-id: "bill-of-materials-id"

  - name: "bom_revision_extid"
    type: "string"
    description: ""

  - name: "bom_revision_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "bom-revision-id"

  - name: "date_created"
    type: "date-time"
    description: ""

  - name: "date_effective"
    type: "date-time"
    description: ""

  - name: "date_obsolete"
    type: "date-time"
    description: ""

  - name: "form_template_component_id"
    type: "string"
    description: ""

  - name: "form_template_id"
    type: "integer"
    description: ""

  - name: "is_inactive"
    type: "string"
    description: ""

  - name: "memo"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""
---