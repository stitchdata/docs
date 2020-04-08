---
tap: "covid-19"
version: "1"
key: ""

name: "c19_trk_us_states_kff_hospital_beds"
doc-link: "https://www.kff.org/other/state-indicator/beds-by-ownership/?currentTimeframe=0&sortModel=%7B%22colId%22:%22Location%22,%22sort%22:%22asc%22%7D"
singer-schema: "https://github.com/singer-io/tap-covid-19/blob/master/tap_covid_19/schemas/c19_trk_us_states_kff_hospital_beds.json"
description: |
  The `{{ table.name }}` table contains statistics about hospital beds per 1,000 population, segmented by hospital ownership type.

  **Note**: The source file for this table is a single file that updates on a daily basis. When Stitch replicates this table, it will replicate the entire contents of the file, but only if the file has been modified since the integration's last replication job.

replication-method: "Key-based Incremental"

attributes:
  - name: "__sdc_row_number"
    type: "integer"
    primary-key: true
    description: "The number of the row in the source CSV."

  - name: "git_last_modified"
    type: "date-time"
    replication-key: true
    description: "The date the git file was last modified."

  - name: "for_profit"
    type: "number"
    description: "The number of hospital beds for for-profit hospitals."

  - name: "git_file_name"
    type: "string"
    description: "The name of the source git file."

  - name: "git_html_url"
    type: "string"
    description: "The URL of the source git html."

  - name: "git_last_modified"
    type: "date-time"
    description: "The date the git file was last modified."

  - name: "git_owner"
    type: "string"
    description: "The owner of the file in git."

  - name: "git_path"
    type: "string"
    description: "The path to the file in git."

  - name: "git_repository"
    type: "string"
    description: "The git repository."

  - name: "git_sha"
    type: "string"
    description: "The SHA of the file in git."

  - name: "git_url"
    type: "string"
    description: "The git URL."

  - name: "non_profit"
    type: "number"
    description: "The number of hospital beds for non-profit hospitals."

  - name: "state"
    type: "string"
    description: "The state or territory postal code abbreviation."

  - name: "state_local_government"
    type: "number"
    description: "The number of hospital beds for state/local government hospitals."

  - name: "state_name"
    type: "string"
    description: "The full name of the state or territory."

  - name: "total"
    type: "number"
    description: "The total number of hospital beds, calculated by `for_profit + non_profit + state_local_government`."
---