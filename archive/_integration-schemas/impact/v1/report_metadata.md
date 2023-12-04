---
tap: "impact"
version: "1"
key: "report-metadata"

name: "report_metadata"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-impact/blob/master/tap_impact/schemas/report_metadata.json"
description: |
  The `{{ table.name }}` table contains info about metadata associated with reports.

replication-method: "Full Table"

api-method:
  name: "Get report metadata"
  doc-link: "https://developer.impact.com/default/documentation/Rest-Adv-v8#operations-Reports-GetReportMetadata"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: ""
    foreign-key-id: "report-id"

  - name: "attributes"
    type: "array"
    description: ""
    subattributes:
      - name: "name"
        type: "string"
        description: ""

      - name: "data_type"
        type: "string"
        description: ""

      - name: "description"
        type: "string"
        description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "filters"
    type: "array"
    description: ""
    subattributes:
      - name: "name"
        type: "string"
        description: ""

      - name: "data_type"
        type: "string"
        description: ""

      - name: "format"
        type: "string"
        description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "run_uri"
    type: "string"
    description: ""

  - name: "uri"
    type: "string"
    description: ""
---