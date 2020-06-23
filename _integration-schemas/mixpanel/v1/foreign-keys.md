---
tap-reference: "mixpanel"

version: "1"

foreign-keys:
  - id: "cohort-id"
    table: "cohorts"
    attribute: "cohort_id"
    all-foreign-keys:
      - table: "cohort_members"
      - table: "cohorts"

  - id: "project-id"
    table: ""
    attribute: "project_id"
    all-foreign-keys:
      - table: "annotations"
      - table: "cohorts"
---