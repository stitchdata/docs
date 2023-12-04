---
tap-reference: "harvest-forecast"

version: "1"

foreign-keys:
  - id: "assignment-id"
    attribute: ""
    table: "assignments"
    all-foreign-keys:
      - table: "assignments"
        join-on: "id"

  - id: "client-id"
    attribute: "client_id"
    table: "clients"
    all-foreign-keys:
      - table: "clients"
        join-on: "id"
      - table: "projects"

  - id: "milestone-id"
    attribute: ""
    table: "milestones"
    all-foreign-keys:
      - table: "milestones"
        join-on: "id"

  - id: "person-id"
    attribute: "updated_by_id"
    table: "people"
    all-foreign-keys:
      - table: "assignments"
        join-on: "person_id"
      - table: "assignments"
      - table: "clients"
      - table: "milestones"
      - table: "people"
        join-on: "id"
      - table: "people"
      - table: "projects"
      - table: "placeholders"
      - table: "roles"

  - id: "project-id"
    attribute: "project_id"
    table: "projects"
    all-foreign-keys:
      - table: "assignments"
      - table: "milestones"
      - table: "projects"
        join-on: "id"

  - id: "placeholder-id"
    attribute: "placeholder_id"
    table: "placeholders"
    all-foreign-keys:
      - table: "assignments"
      - table: "placeholders"
        join-on: "id"
      - table: "roles"
        subattribute: "placeholder_ids"
        join-on: "value"

  - id: "role-id"
    attribute: "value"
    table: "roles"
    all-foreign-keys:
      - table: "people"
        subattribute: "roles"

      - table: "placeholders"
        subattribute: "roles"

      - table: "roles"
        join-on: "id"
---