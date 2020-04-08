---
tap: "covid-19"
version: "1"
key: ""

name: "jh_csse_daily"
doc-link: "https://github.com/CSSEGISandData/COVID-19"
singer-schema: "https://github.com/singer-io/tap-covid-19/blob/master/tap_covid_19/schemas/jh_csse_daily.json"
description: |
  The `{{ table.name }}` table contains data collected by [Johns Hopkins CSSE](https://github.com/CSSEGISandData/COVID-19){:target="new"}.

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

  - name: "active"
    type: "integer"
    description: ""

  - name: "admin_area"
    type: "string"
    description: ""

  - name: "combined_key"
    type: "string"
    description: ""

  - name: "confirmed"
    type: "integer"
    description: ""

  - name: "country_region"
    type: "string"
    description: ""

  - name: "country_region_cleansed"
    type: "string"
    description: ""

  - name: "date"
    type: "date"
    description: "The date."

  - name: "datetime"
    type: "date-time"
    description: "The datetime of the record."

  - name: "deaths"
    type: "integer"
    description: ""

  - name: "fips"
    type: "string"
    description: "The Federal Information Processing Standard state code."

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

  - name: "is_a_cruise"
    type: "boolean"
    description: ""

  - name: "last_update"
    type: "date-time"
    description: ""

  - name: "latitude"
    type: "number"
    description: ""

  - name: "longitude"
    type: "number"
    description: ""

  - name: "province_state"
    type: "string"
    description: ""

  - name: "province_state_cleansed"
    type: "string"
    description: ""

  - name: "recovered"
    type: "integer"
    description: ""
---