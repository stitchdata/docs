---
tap-reference: "asana"

version: "1"

foreign-keys:
  - id: "project-id"
    attribute: "id"
    table: "projects"
    all-foreign-keys:
      - table: "projects"
      - table: "tasks"
        subtable: "projects"

  - id: "tag-id"
    attribute: "id"
    table: "tags"
    all-foreign-keys:
      - table: "tags"

  - id: "task-id"
    attribute: "id"
    table: "tasks"
    all-foreign-keys:
      - table: "tasks"

  - id: "user-id"
    attribute: "id"
    table: "users"
    all-foreign-keys:
      - table: "projects"
        subtable: "followers"
      - table: "projects"
        subtable: "members"
      - table: "projects"
        subtable: "owner"
      - table: "tags"
        subtable: "followers"
      - table: "tasks"
        subtable: "assignees"
      - table: "tasks"
        subtable: "followers"
      - table: "users"

  - id: "workspace-id"
    attribute: "id"
    table: "workspace"
    all-foreign-keys:
      - table: "projects"
        subtable: "workspace"
      - table: "tags"
        subtable: "workspace"
      - table: "tasks"
        subtable: "workspace"
      - table: "users"
        subtable: "workspace"
      - table: "workspace"
---