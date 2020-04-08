---
tap: "covid-19"
version: "1"
key: ""

name: "c19_trk_us_states_info"
doc-link: "https://covidtracking.com/api#apistatesinfo---states-information"
singer-schema: "https://github.com/singer-io/tap-covid-19/blob/master/tap_covid_19/schemas/c19_trk_us_states_info.json"
description: |
  The `{{ table.name }}` table contains information about states in the United States.

  **Note**: The source file for this table is a single file that updates on a daily basis. When Stitch replicates this table, it will replicate the entire contents of the file, but only if the file has been modified since the integration's last replication job.

replication-method: "Key-based Incremental"

attributes:
  - name: "_sdc_row_number"
    type: "integer"
    primary-key: true
    description: "The number of the row in the source CSV."

  - name: "git_last_modified"
    type: "date-time"
    replication-key: true
    description: "The date the git file was last modified."

  - name: "covid19_site"
    type: "string"
    description: "The webpage dedicated to making results available to the public."

  - name: "covid19_site_old"
    type: "string"
    description: ""

  - name: "covid19_site_secondary"
    type: "string"
    description: "An informational webpage."

  - name: "fips"
    type: "string"
    description: "The Federal Information Processing Standard state code."

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

  - name: "name"
    type: "string"
    description: "The full state or territory name."

  - name: "notes"
    type: "string"
    description: "Notes about the information available and how it's collected or recorded."

  - name: "pui"
    type: "string"
    description: "Person Under Investigation; it is meant to capture positive, negative, and pending test results."

  - name: "pum"
    type: "string"
    description: "Person Under Monitoring. **Note**: The source doesn't track these numbers as they are reported less consistently across states."

  - name: "state"
    type: "string"
    description: "The state or territory postal code abbreviation."

  - name: "twitter"
    type: "string"
    description: "Twitter for the state's health department."
---