---
tap: "covid-19"
version: "1"
key: ""

name: "neherlab_population"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-covid-19/blob/master/tap_covid_19/schemas/neherlab_population.json"
description: |
  The `{{ table.name }}` table contains [Neherlab Scenarios Data](https://github.com/neherlab/covid19_scenarios){:target="new"} from [Neherlab Biozentrum, Center for Computational Biology](https://neherlab.org/){:target="new"}.

  **Note**: The source file for this table is a single file that updates on a daily basis. When Stitch replicates this table, it will replicate the entire contents of the file, but only if the file has been modified since the integration's last replication job.

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

  - name: "git_repository"
    type: "string"
    description: "The git repository."

  - name: "git_sha"
    type: "string"
    description: "The SHA of the file in git."

  - name: "git_url"
    type: "string"
    description: "The git URL."

  - name: "hemisphere"
    type: "string"
    description: ""

  - name: "hospital_beds"
    type: "integer"
    description: ""

  - name: "icu_beds"
    type: "integer"
    description: ""

  - name: "imports_per_day"
    type: "number"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "population"
    type: "string"
    description: ""

  - name: "suspected_cases_mar_1st"
    type: "integer"
    description: ""
---