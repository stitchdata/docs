---
tap: "impact"
version: "1"
key: "report"

name: "reports"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-impact/blob/master/tap_impact/schemas/reports.json"
description: |
  The `{{ table.name }}` table contains info about the reports in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
  name: "List reports"
  doc-link: "https://developer.impact.com/default#operations-Reports-ListReports"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: ""
    foreign-key-id: "report-id"

  - name: "description"
    type: "string"
    description: ""

  - name: "meta_data_uri"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "run_uri"
    type: "string"
    description: ""
---