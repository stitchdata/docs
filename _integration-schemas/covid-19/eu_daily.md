---
tap: "covid-19"
version: "1"
key: ""

name: "eu_daily"
doc-link: "https://github.com/covid19-eu-zh/covid19-eu-data"
singer-schema: "https://github.com/singer-io/tap-covid-19/blob/master/tap_covid_19/schemas/eu_daily.json"
description: |
  The `{{ table.name }}` table contains statistics for the European Union, aggregated by day. This data is sourced from the [covid19-eu-data](https://github.com/covid19-eu-zh/covid19-eu-data){:target="new"} GitHub repository.

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
    type: "number"
    description: "The number of cases by the specified `datetime`."

  - name: "cases_100k_pop"
    type: "number"
    description: |
      The number of cases per 100k population. When looking at this value, note that:

      - **Germany** did not track this in the beginning, thus there may be missing values.

  - name: "cases_lower"
    type: "integer"
    description: ""

  - name: "cases_upper"
    type: "integer"
    description: ""

  - name: "country"
    type: "string"
    description: "The country code."

  - name: "date"
    type: "date"
    description: "The date."

  - name: "datetime"
    type: "date-time"
    description: "The local datetime of the record."

  - name: "deaths"
    type: "number"
    description: |
      The number of deaths. When looking at this value, note that:

      - **Austria** started tracking this on 2020-03-13
      - **Germany** did not track this in the beginning, thus there may be missing values.

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
    type: "number"
    description: "The number of hospitalized patients."

  - name: "intensive_care"
    type: "integer"
    description: "The number of patients in intensive care."

  - name: "lau"
    type: "string"
    description: |
      - **Netherlands**: LAU (city).

  - name: "nuts_1"
    type: "string"
    description: "**Applicable to Germany**. NUTS 1 (states) in Germany."

  - name: "nuts_2"
    type: "string"
    description: |
      - **Austria**: NUTS 2 administrative divisions (states) in Austria.
      - **France**: Local provinces or oversea authorities in France. Oversea and Metropolis are also added as conditional sum.
      - **Italy**: NUTS 2 (regions).
      - **Poland**: NUTS 2 (provinces) in PL or sum as the total.
      - **Switzerland**: NUTS 2 (regions).

  - name: "nuts_3"
    type: "string"
    description: |
      - **Czechia**: NUTS 3 (regions, Kraje) in Czechia (Czech Republic).
      - **England, Scotland, Wales**: Local authorities in the city, town, borough, etc.
      - **Italy**: NUTS 3 (provinces).
      - **Norway**: NUTS 3 (counties).
      - **Sweden**: NUTS 3 (counties) in Sweden.

  - name: "percent"
    type: "number"
    description: "The percent of cases by the specified `datetime`."

  - name: "population"
    type: "number"
    description: "The population of the city."

  - name: "quarantine"
    type: "integer"
    description: "The number of quarantined patients."

  - name: "recovered"
    type: "integer"
    description: |
      The number of recovered patients. When looking at this value, note that:

      - **Austria** started tracking this on 2020-03-13.

  - name: "tests"
    type: "integer"
    description: ""
---