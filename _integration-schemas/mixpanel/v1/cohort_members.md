---
tap: "mixpanel"
version: "1"
key: "cohort-member"

name: "cohort_members"
doc-link: "https://developer.mixpanel.com/docs/data-export-api#section-engage"
singer-schema: "https://github.com/singer-io/tap-mixpanel/blob/master/tap_mixpanel/schemas/cohort_members.json"
description: |
  The `{{ table.name }}` table contains info about the cohorts user profiles belong to.

replication-method: "Full Table"

api-method:
  name: "Engage, fiiter by cohort ID"
  doc-link: "https://mixpanel.com/api/2.0/cohorts/list"

attributes:
  - name: "cohort_id"
    type: "integer"
    primary-key: true
    description: "The cohort ID."
    foreign-key-id: "cohort-id"

  - name: "distinct_id"
    type: "string"
    primary-key: true
    description: "The individual profile ID."
---