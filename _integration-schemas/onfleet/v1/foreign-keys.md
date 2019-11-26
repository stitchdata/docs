---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-foreign-keys/
## FOR INSTRUCTIONS & REFERENCE INFO

tap-reference: "onfleet"

version: "1.0"

foreign-keys:
  - id: "administrator-id"
    table: "administrators"
    attribute: ""
    all-foreign-keys:
      - table: "administrators"
        join-on: "id"
      - table: "tasks"
        join-on: "creator"
      - table: "teams"
        subtable: "managers"
        join-on: "value"

  - id: "hub-id"
    table: "hubs"
    attribute: "hub"
    all-foreign-keys:
      - table: "hubs"
        join-on: "id"
      - table: "teams"

  - id: "organization-id"
    table: "organizations"
    attribute: "organization"
    all-foreign-keys:
      - table: "administrators"
      - table: "organizations"
        join-on: "id"
      - table: "organizations"
        subtable: "delegatees"
        join-on: "value"
      - table: "tasks"
      - table: "workers"

  - id: "task-id"
    table: "tasks"
    attribute: ""
    all-foreign-keys:
      - table: "task"
        join-on: "id"
      - table: "teams"
        subtable: "tasks"
        join-on: "value"
      - table: "workers"
        join-on: "activeTask"
      - table: "workers"
        subtable: "tasks"
        join-on: "value"

  - id: "team-id"
    table: "teams"
    attribute: "team"
    all-foreign-keys:
      - table: "hubs"
        subtable: "teams"
        join-on: "value"
      - table: "teams"
        join-on: "id"
      - table: "workers"
        subtable: "teams"
        join-on: "value"

  - id: "worker-id"
    table: "workers"
    attribute: "worker"
    all-foreign-keys:
      - table: "tasks"
      - table: "teams"
        subtable: "workers"
        join-on: "value"
      - table: "workers"
        join-on: "id"
---