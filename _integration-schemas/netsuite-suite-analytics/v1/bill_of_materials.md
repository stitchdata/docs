---
tap: "netsuite-suite-analytics"
version: "1"
key: "bill-of-materials"

name: "bill_of_materials"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/bill_of_materials.html"
description: ""

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "available_for_all_assemblies"
    type: "string"
    description: ""

  - name: "available_for_all_locations"
    type: "string"
    description: ""

  - name: "bill_of_materials_extid"
    type: "string"
    description: ""

  - name: "bill_of_materials_id"
    type: "integer"
    netsuite-primary-key: true
    description: ""
    foreign-key-id: "bill-of-materials-id"

  - name: "date_created"
    type: "date-time"
    description: ""

  - name: "exclude_child_subsidiaries"
    type: "string"
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

  - name: "original_assembly_id"
    type: "integer"
    description: ""
    foreign-key-id: "item-id"

  - name: "use_component_yield"
    type: "string"
    description: ""
---