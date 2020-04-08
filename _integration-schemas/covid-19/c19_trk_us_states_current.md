---
tap: "covid-19"
version: "1"
key: ""

name: "c19_trk_us_states_current"
doc-link: "https://covidtracking.com/api#apistates---states-current-values"
singer-schema: "https://github.com/singer-io/tap-covid-19/blob/master/tap_covid_19/schemas/c19_trk_us_states_current.json"
description: |
  The `{{ table.name }}` table contains current statistics for states in the United States.

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

  - name: "check_time_et"
    type: "string"
    description: ""

  - name: "commercial_score"
    type: "integer"
    description: "`+1` for reporting all commercial tests."

  - name: "date_checked"
    type: "date-time"
    description: "The date and time when the data was last checked."

  - name: "date_modified"
    type: "date-time"
    description: "The date the record was last modified."

  - name: "death"
    type: "integer"
    description: "The cumulative number of deaths recorded for the state."

  - name: "fips"
    type: "string"
    description: "Federal Information Processing Standard state code."

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

  - name: "grade"
    type: "string"
    description: |
      The letter grade, based on `score`. Refer to the [COVID documentation](https://covidtracking.com/about-data#data-quality-grade){:target="new"} for more info about how grades are caluclated.

  - name: "hospitalized"
    type: "integer"
    description: "The total cumulative number of people hospitalized."

  - name: "last_update_et"
    type: "string"
    description: ""

  - name: "negative"
    type: "integer"
    description: "The total cumulative number of negative tests."

  - name: "negative_regular_score"
    type: "integer"
    description: "+1 for reporting negatives reliably."

  - name: "notes"
    type: "string"
    description: ""

  - name: "pending"
    type: "integer"
    description: "The number of pending tests for the day."

  - name: "positive"
    type: "integer"
    description: "The total cumulative number of positive tests."

  - name: "positive_score"
    type: "integer"
    description: "+1 for reporting positives reliably."

  - name: "score"
    type: "integer"
    description: |
      The data quality grade for the state. Possible values are:

      - `4` - Corresponds to a `grade` of `A`
      - `3` - Corresponds to a `grade` of `B`
      - `2` - Corresponds to a `grade` of `C`
      - `1` - Corresponds to a `grade` of `D`
      
      Refer to the [COVID documentation](https://covidtracking.com/about-data#data-quality-grade){:target="new"} for more info about how scores are caluclated.

  - name: "state"
    type: "string"
    description: "The state or territory postal code abbreviation."

  - name: "total"
    type: "integer"
    description: "**Deprecated**. Equal to `positive + negative + pending`. **Note**: `pending` has been an unstable value and should not count in any totals."

  - name: "total_test_results"
    type: "integer"
    description: "The total number of test results, calculated as `positive + negative`."
---