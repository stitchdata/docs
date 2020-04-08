---
tap: "covid-19"
version: "1"
key: ""

name: "eu_ecdc_daily"
doc-link: "https://github.com/covid19-eu-zh/covid19-eu-data"
singer-schema: "https://github.com/singer-io/tap-covid-19/blob/master/tap_covid_19/schemas/eu_ecdc_daily.json"
description: |
  The `{{ table.name }}` table contains statistics reported to the European Centre for Disease Prevention and Control, segmented by day.

replication-method: "Key-based Incremental"

attributes:
  - name: "git_path"
    type: "string"
    primary-key: true
    description: "The path to the file in git."

  - name: "_sdc_row_number"
    type: "integer"
    primary-key: true
    description: "The number of the row in the source CSV."

  - name: "git_last_modified"
    type: "date-time"
    replication-key: true
    description: "The date the git file was last modified."

  - name: "cases"
    type: "number"
    description: "The number of cases."

  - name: "country"
    type: "string"
    description: "The country code."

  - name: "date"
    type: "date"
    description: "The date."

  - name: "datetime"
    type: "date-time"
    description: "The local datetime of the record."

  - name: "deaths"
    type: "number"
    description: "The number of deaths."

  - name: "git_file_name"
    type: "string"
    description: "The name of the source git file."

  - name: "git_html_url"
    type: "string"
    description: "The URL of the source git html."

  - name: "git_owner"
    type: "string"
    description: "The owner of the file in git."

  - name: "git_repository"
    type: "string"
    description: "The git repository."

  - name: "git_sha"
    type: "string"
    description: "The SHA of the file in git."

  - name: "git_url"
    type: "string"
    description: "The git URL."
---