---
tap-reference: "harvest-forecast"

version: "1.0"

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
    attribute: "person_id"
    table: "people"
    all-foreign-keys:
      - table: "assignments"
      - table: "assignments"
        join-on: "updated_by_id"
      - table: "clients"
        join-on: "updated_by_id"
      - table: "milestones"
        join-on: "updated_by_id"
      - table: "people"
        join-on: "id"
      - table: "people"
        join-on: "updated_by_id"
      - table: "projects"
        join-on: "updated_by_id"

  - id: "project-id"
    attribute: "project_id"
    table: "projects"
    all-foreign-keys:
      - table: "assignments"
      - table: "milestones"
      - table: "projects"
        join-on: "id"
---