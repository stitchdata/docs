---
tap: "covid-19"
version: "1"
key: ""

name: "nytimes_us_states"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-covid-19/blob/master/tap_covid_19/schemas/nytimes_us_states.json"
description: |
  The `{{ table.name }}` table contains data collected by [Johns Hopkins CSSE](https://github.com/CSSEGISandData/COVID-19){:target="new"}.

  **Note**: The source file for this table is a single file that updates on a daily basis. When Stitch replicates this table, it will replicate the entire contents of the file, but only if the file has been modified since the integration's last replication job.

replication-method: "Full Table"

attributes:
  - name: "__sdc_row_number"
    type: "integer"
    primary-key: true
    description: "The number of the row in the source CSV."

  - name: "git_last_modified"
    type: "date-time"
    replication-key: true
    description: "The date the git file was last modified."

  - name: "cases"
    type: "integer"
    description: |
      The number of cases. **Note**: The source considers `confirmed cases as patients who test positive for the coronavirus. A case is confirmed when it is reported by a federal, state, territorial or local government agency.` Additionally, cases are counted on the date they are first announced.

  - name: "date"
    type: "date"
    description: "The date."

  - name: "datetime"
    type: "date-time"
    description: "The datetime for the record."

  - name: "deaths"
    type: "integer"
    description: "The number of deaths."

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

  - name: "state"
    type: "string"
    description: "The full name of the US state."

  - name: "state_code"
    type: "string"
    description: "The state's reference code."
---