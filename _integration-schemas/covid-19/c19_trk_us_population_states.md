---
tap: "covid-19"
version: "1"
key: ""

name: "c19_trk_us_population_states"
doc-link: "https://github.com/COVID19Tracking"
singer-schema: "https://github.com/singer-io/tap-covid-19/blob/master/tap_covid_19/schemas/c19_trk_us_population_states.json"
description: |
  The `{{ table.name }}` table contains population statistics for states in the United States.

  **Note**: The source file for this table is a single file that updates on a daily basis. When Stitch replicates this table, it will replicate the entire contents of the file, but only if the file has been modified since the integration's last replication job.

replication-method: "Key-based Incremental"

attributes:
  - name: "row_number"
    type: "integer"
    primary-key: true
    description: "The number of the row in the source CSV."

  - name: "git_last_modified"
    type: "date-time"
    replication-key: true
    description: "The date the git file was last modified."

  - name: "geo_id"
    type: "string"
    description: ""

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

  - name: "pop_density"
    type: "number"
    description: "The population density for the state."

  - name: "population"
    type: "integer"
    description: "The total population for the state."

  - name: "state"
    type: "string"
    description: "The abbreviated state code for the state. For example: `NY`"

  - name: "state_name"
    type: "string"
    description: "The name of the state. For example: `New York`"
---