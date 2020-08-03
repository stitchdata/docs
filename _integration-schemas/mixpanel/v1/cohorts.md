---
tap: "mixpanel"
version: "1"
key: "cohort"

name: "cohorts"
doc-link: "https://developer.mixpanel.com/docs/cohorts#section-list-cohorts"
singer-schema: "https://github.com/singer-io/tap-mixpanel/blob/master/tap_mixpanel/schemas/cohorts.json"
description: |
  The `{{ table.name }}` table contains info about the cohorts in a {{ integration.display_name }} project.

replication-method: "Full Table"

api-method:
  name: "List cohorts"
  doc-link: "https://developer.mixpanel.com/docs/cohorts#section-list-cohorts"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The cohort ID."
    foreign-key-id: "cohort-id"

  - name: "count"
    type: "integer"
    description: "The number of users in the cohort."

  - name: "created"
    type: "date-time"
    description: "The time the cohort was created, in `yyy-mm-dd hh:mm:ss` format."

  - name: "description"
    type: "string"
    description: "The description of the cohort."

  - name: "is_visible"
    type: "integer"
    description: "If `1`, the cohort is visible. If `0`, the cohort is hidden."

  - name: "name"
    type: "string"
    description: "The name of the cohort."

  - name: "project_id"
    type: "integer"
    description: "The project ID."
    foreign-key-id: "project-id"
---