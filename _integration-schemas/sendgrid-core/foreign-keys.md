---
tap-reference: "sendgrid-core"

# version: "1.0"

foreign-keys:
  - attribute: "list_id"
    table: "lists_all"
    join-on: "id"

  - attribute: "segment_id"
    table: "segments_all"
    join-on: "id"

  - attribute: "suppression_group_id"
    table: "groups_all"
    join-on: "id"

  - attribute: "group_id"
    table: "groups_all"
    join-on: "id"

  - attribute: ""
    table: "campaigns"
    join-on: "id"
---