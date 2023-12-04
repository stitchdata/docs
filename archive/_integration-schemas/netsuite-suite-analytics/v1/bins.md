---
tap: "netsuite-suite-analytics"
version: "1"
key: "bin"

name: "bins"
doc-link: "https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2020_1/odbc/record/bin.html"
description: |
  The `{{ table.name }}` table contains info about bins, or places in your warehouse where you store inventory items.

replication-method: "Full Table"

attributes:
  - name: "{{ system-column.record-hash }}"
    type: "string"
    primary-key: true
    description: |
      {{ system-column.record-hash-netsuite-suite-analytics }}

      {{ integration.netsuite-primary-keys | flatify }}

  - name: "bin_id"
    type: "integer"
    netsuite-primary-key: true
    description: "The bin ID. {{ integration.netsuite-primary-key-description | flatify }}"
    # foreign-key-id: "bin-id"

  - name: "bin_number"
    type: "integer"
    description: "The bin number."

  - name: "external_id"
    type: "integer"
    description: "The external ID of the bin."

  - name: "is_inactive"
    type: "string"
    description: "Whether the bin is inactive."

  - name: "location_id"
    type: "integer"
    description: "The location of the bin."
    # foreign-key-id: "location-id"

  - name: "memo"
    type: "string"
    description: "Memo about the bin."
---