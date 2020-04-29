---
tap: "covid-19"
version: "1"
key: ""

name: "italy_provincial_daily"
doc-link: "https://github.com/pcm-dpc/COVID-19#dati-per-provincia"
singer-schema: "https://github.com/singer-io/tap-covid-19/blob/master/tap_covid_19/schemas/italy_provincial_daily.json"
description: |
  The `{{ table.name }}` table contains statistics for Italian provinces, segmented by day.

replication-method: "Key-based Incremental"

attributes:
  - name: "git_path"
    type: "string"
    primary-key: true
    description: "The path to the file in git."

  - name: "__sdc_row_number"
    type: "integer"
    primary-key: true
    description: "The number of the row in the source CSV."

  - name: "git_last_modified"
    type: "date-time"
    replication-key: true
    description: "The date the git file was last modified."

  - name: "country"
    type: "string"
    description: "The country reference code."

  - name: "date"
    type: "date"
    description: "The date."

  - name: "date_of_notification"
    type: "date-time"
    description: ""

  - name: "datetime"
    type: "date-time"
    description: ""

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

  - name: "lat"
    type: "number"
    description: "The latitude of the province."

  - name: "long"
    type: "number"
    description: "The longitude of the province."

  - name: "note_en"
    type: "string"
    description: "Notes in English."

  - name: "note_it"
    type: "string"
    description: "Notes in Italian."

  - name: "province"
    type: "string"
    description: "The full name of the province."

  - name: "province_abbr"
    type: "string"
    description: "The abbreviation of the province's name."

  - name: "province_code"
    type: "string"
    description: "The code of the region."

  - name: "region"
    type: "string"
    description: "The full name of the region."

  - name: "region_code"
    type: "string"
    description: "The code of the region."

  - name: "total_cases"
    type: "integer"
    description: "The total number of positive cases for the province."
---