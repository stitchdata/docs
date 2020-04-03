---
tap: "covid-19"
version: "1"
key: ""

name: "neherlab_case_counts"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-covid-19/blob/master/tap_covid_19/schemas/neherlab_case_counts.json"
description: |
  The `{{ table.name }}` table contains [Neherlab Scenarios Data](https://github.com/neherlab/covid19_scenarios){:target="new"} from [Neherlab Biozentrum, Center for Computational Biology](https://neherlab.org/){:target="new"}.

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

  - name: "cases"
    type: "integer"
    description: ""

  - name: "date"
    type: "date"
    description: "The date."

  - name: "datetime"
    type: "date-time"
    description: ""

  - name: "deaths"
    type: "integer"
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

  - name: "hospitalized"
    type: "integer"
    description: "The number of recorded hospitalized cases for the day."

  - name: "icu"
    type: "integer"
    description: ""

  - name: "location"
    type: "string"
    description: ""

  - name: "recovered"
    type: "integer"
    description: ""
---