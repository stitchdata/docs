---
tap-reference: "sendgrid-core"

version: "1.0"

foreign-keys:
  - id: "campaign-id"
    attribute: "id"
    table: "campaigns"
    all-foreign-keys:
      - table: "campaigns"

  - id: "contact-id"
    attribute: "id"
    table: "contacts"
    all-foreign-keys:
      - table: "contacts"

  - id: "email-id"
    attribute: "email"
    table: ""
    all-foreign-keys:
      - table: "blocks"
      - table: "bounces"
      - table: "contacts"
      - table: "group_members"
      - table: "invalids"
      - table: "lists_members"
      - table: "segments_members"
      - table: "spam_reports"

  - id: "list-id"
    attribute: "list_id"
    table: "lists_all"
    all-foreign-keys:
      - table: "lists_all"
      - table: "campaigns"
        subtable: "list_ids"

  - id: "list-member-id"
    attribute: "id"
    table: "lists_members"
    all-foreign-keys:
      - table: "lists_members"

  - id: "segment-id"
    attribute: "segment_id"
    table: "segments"
    all-foreign-keys:
      - table: "segments_all"
        join-on: "id"
      - table: "campaigns"
        subtable: "segment_ids"
      - table: "segments_members"

  - id: "segment-member-id"
    attribute: "id"
    table: "segments_members"
    all-foreign-keys:
      - table: "segments_members"

  - id: "suppression-group-id"
    attribute: "suppression_group_id"
    table: "groups_all"
    all-foreign-keys:
      - table: "campaigns"
      - table: "global_suppressions"
        join-on: "id"
      - table: "group_members"
        join-on: "group_id"

  - id: "template-id"
    attribute: "id"
    table: "templates_all"
    all-foreign-keys:
      - table: "templates_all"
---