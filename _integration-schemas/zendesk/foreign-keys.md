---
tap-reference: "zendesk"

version: "1.0"

foreign-keys:
  - attribute: "group_id"
    table: "groups"
    join-on: "id"

  - attribute: "default_group_id"
    table: "groups"
    join-on: "id"

  - attribute: "user_id"
    table: "users"
    join-on: "id"

  - attribute: "macro_id"
    table: "macros"
    join-on: "id"

  - attribute: "author_id"
    table: "users"
    join-on: "id"

  - attribute: "ticket_id"
    table: "tickets"
    join-on: "id"

  - attribute: "requester_id"
    table: "users"
    join-on: "id"

  - attribute: "organization_id"
    table: "organizations"
    join-on: "id"

  - attribute: "submitter_id"
    table: "users"
    join-on: "id"

  - attribute: "assignee_id"
    table: "users"
    join-on: "id"

  - attribute: ""
    table: "tags"
    join-on: "name"

  - attribute: ""
    table: "ticket_fields"
    join-on: "id"
---