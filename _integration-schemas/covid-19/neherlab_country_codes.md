---
tap: "covid-19"
version: "1"
key: ""

name: "neherlab_country_codes"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-covid-19/blob/master/tap_covid_19/schemas/neherlab_country_codes.json"
description: |
  The `{{ table.name }}` table contains [Neherlab Scenarios Data](https://github.com/neherlab/covid19_scenarios){:target="new"} from [Neherlab Biozentrum, Center for Computational Biology](https://neherlab.org/){:target="new"}.

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

  - name: "alpha_2"
    type: "string"
    description: ""

  - name: "alpha_3"
    type: "string"
    description: ""

  - name: "country_code"
    type: "string"
    description: ""

  - name: "git_file_name"
    type: "string"
    description: "The name of the source git file."

  - name: "git_html_url"
    type: "string"
    description: "The URL of the source git html."

  - name: "git_path"
    type: "string"
    description: "The path to the file in git."

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

  - name: "intermediate_region"
    type: "string"
    description: ""

  - name: "intermediate_region_code"
    type: "string"
    description: ""

  - name: "iso_3166_2"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "region"
    type: "string"
    description: ""

  - name: "region_code"
    type: "string"
    description: ""

  - name: "sub_region"
    type: "string"
    description: ""

  - name: "sub_region_code"
    type: "string"
    description: ""
---