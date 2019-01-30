---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-foreign-keys/
## FOR INSTRUCTIONS & REFERENCE INFO

tap-reference: "toggl"

version: "1.0"

foreign-keys:
  - id: "workspace-id"
    table: "a_workspaces"
    attribute: "wid"
    all-foreign-keys:
      - table: "a_workspaces"
        join-on: "id"
      - table: "clients"
      - table: "groups"
      - table: "projects"
      - table: "tags"
      - table: "tasks"
      - table: "users"
        join-on: "default_wid"
      - table: "workspace_users"


  - id: "client-id"
    table: "clients"
    attribute: "cid"
    all-foreign-keys:
      - table: "clients"
        join-on: "id"
      - table: "projects"

  - id: "group-id"
    table: "groups"
    attribute: ""
    all-foreign-keys:
      - table: "groups"
        join-on: "id"
  
  - id: "project-id"
    table: "projects"
    attribute: ""
    all-foreign-keys:
      - table: "projects"
        join-on: "id"
      - table: "tasks"
      - table: "time_entries"

  - id: "tag-id"
    table: "tags"
    attribute: ""
    all-foreign-keys:
      - table: "tags"
        join-on: "id"

  - id: "task-id"
    table: "tasks"
    attribute: "tid"
    all-foreign-keys:
      - table: "tasks"
        join-on: "id"
      - table: "time_entries"

  - id: "user-id"
    table: "users"
    attribute: "uid"
    all-foreign-keys:
      - table: "tasks"
      - table: "time_entries"
      - table: "users"
        join-on: "id"
---