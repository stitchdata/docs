---
tap: "covid-19"
version: "1"
key: ""

name: "italy_national_daily"
doc-link: "https://github.com/pcm-dpc/COVID-19#andamento-nazionale"
singer-schema: "https://github.com/singer-io/tap-covid-19/blob/master/tap_covid_19/schemas/italy_national_daily.json"
description: |
  The `{{ table.name }}` table contains statistics for Italy, segmented by day.

replication-method: "Key-based Incremental"

attributes:
  - name: "git_path"
    type: "string"
    primary-key: true
    description: "The path to the file in git."

  - name: "row_number"
    type: "integer"
    primary-key: true
    description: "The number of the row in the source CSV."

  - name: "git_last_modified"
    type: "date-time"
    replication-key: true
    description: "The date the git file was last modified."

  - name: "country"
    type: "string"
    description: "The country code."

  - name: "date"
    type: "date"
    description: "The date."

  - name: "date_of_notification"
    type: "date-time"
    description: "The date of the record."

  - name: "datetime"
    type: "date-time"
    description: "The datetime of the record."

  - name: "deaths"
    type: "integer"
    description: "The number of recorded deaths."

  - name: "discharged_recovered"
    type: "integer"
    description: "The number of recovered patients."

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

  - name: "home_isolation"
    type: "integer"
    description: "The number of people in home isolation."

  - name: "hospitalized_with_symptoms"
    type: "integer"
    description: "The number of people hospitalized with symptoms."

  - name: "intensive_care"
    type: "integer"
    description: "The number of people hospitalized in intensive care."

  - name: "new_currently_positive"
    type: "integer"
    description: "The new amount of current positive cases, calculated as the current day's `total_currently_positive` - previous day's `total_currently_positive`"

  - name: "note_en"
    type: "string"
    description: "Notes in English."

  - name: "note_it"
    type: "string"
    description: "Notes in Italian."

  - name: "tested"
    type: "integer"
    description: "The number of tested cases."

  - name: "total_cases"
    type: "integer"
    description: "The total number of cases."

  - name: "total_currently_positive"
    type: "integer"
    description: "The total number of currently positive cases."

  - name: "total_hospitalized"
    type: "integer"
    description: "The total number of hospitalized cases."
---