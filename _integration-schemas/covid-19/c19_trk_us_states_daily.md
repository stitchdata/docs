---
tap: "covid-19"
version: "1"
key: ""

name: "c19_trk_us_states_daily"
doc-link: "https://covidtracking.com/api#apistatesdaily---states-historical-data"
singer-schema: "https://github.com/singer-io/tap-covid-19/blob/master/tap_covid_19/schemas/c19_trk_us_states_daily.json"
description: |
  The `{{ table.name }}` table contains historical data for states in the United States, aggregated by day. **Note**: {{ integration.display_name }} updates this data every day at 4PM ET.

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

  - name: "date"
    type: "date"
    description: "The date."

  - name: "date_checked"
    type: "date-time"
    description: ""

  - name: "death"
    type: "integer"
    description: "The total cumulative number of people that have died."

  - name: "death_increase"
    type: "integer"
    description: "The increase in recorded deaths from the previous day."

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

  - name: "hospitalized"
    type: "integer"
    description: "The number of recorded hospitalized cases for the day."

  - name: "hospitalized_increase"
    type: "integer"
    description: "The increase in recorded hospitalizations from the previous day."

  - name: "negative"
    type: "integer"
    description: "The total cumulative negative test results."

  - name: "negative_increase"
    type: "integer"
    description: "The increase in recorded negative tests from the previous day."

  - name: "pending"
    type: "integer"
    description: "The number of tests that have been submitted to a lab but no results have been reported yet."

  - name: "positive"
    type: "integer"
    description: "The number of total cumulative positive test results."

  - name: "positive_increase"
    type: "integer"
    description: "The increase in recorded positive tests from the previous day."

  - name: "state"
    type: "string"
    description: "The state or territory postal code abbreviation."

  - name: "total"
    type: "integer"
    description: "**Deprecated**. Equal to `positive + negative + pending`. **Note**: `pending` has been an unstable value and should not count in any totals."

  - name: "total_test_results"
    type: "integer"
    description: "The total number of test results "

  - name: "total_test_results_increase"
    type: "integer"
    description: "The increase in test results from the previous day."
---