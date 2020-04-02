---
tap: "covid-19"
version: "1"
key: ""

name: "c19_trk_us_daily"
doc-link: "https://github.com/COVID19Tracking"
singer-schema: "https://github.com/singer-io/tap-covid-19/blob/master/tap_covid_19/schemas/c19_trk_us_daily.json"
description: |
  The `{{ table.name }}` table contains statistics for the United States, aggregated by day.

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

  - name: "date"
    type: "date"
    description: "The date."

  - name: "date_checked"
    type: "date-time"
    description: ""

  - name: "death"
    type: "integer"
    description: "The number of deaths recorded for the day."

  - name: "death_increase"
    type: "integer"
    description: "The increase in recorded deaths from the previous day."

  - name: "git_file_name"
    type: "string"
    description: "The name of the source git file."

  - name: "git_html_url"
    type: "string"
    description: "The URL of the source git html."

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

  - name: "hospitalized"
    type: "integer"
    description: "The number of recorded hospitalized cases for the day."

  - name: "hospitalized_increase"
    type: "integer"
    description: "The increase in recorded hospitalizations from the previous day."

  - name: "negative"
    type: "integer"
    description: "The number of negative tests recorded for the day."

  - name: "negative_increase"
    type: "integer"
    description: "The increase in recorded negative tests from the previous day."

  - name: "pending"
    type: "integer"
    description: "The number of pending tests for the day."

  - name: "pos_neg"
    type: "integer"
    description: "The sum of `positive` + `negative`."

  - name: "positive"
    type: "integer"
    description: "The number of recorded positive tests for the day."

  - name: "positive_increase"
    type: "integer"
    description: "The increase in recorded positive tests from the previous day."

  - name: "states"
    type: "integer"
    description: "The number of states included in the day's statistics."

  - name: "total"
    type: "integer"
    description: "The sum of `positive + negative + pending`."

  - name: "total_test_results"
    type: "integer"
    description: "The total number of test results recorded for the day."

  - name: "total_test_results_increase"
    type: "integer"
    description: "The increase in test results from the previous day."
---