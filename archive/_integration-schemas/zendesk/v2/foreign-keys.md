---
tap-reference: "zendesk"

version: "2"

foreign-keys:
  - id: "group-id"
    attribute: "group_id"
    table: "groups"
    all-foreign-keys:
      - table: "groups"
        join-on: "id"
      - table: "group_memberships"
      - table: "organizations"
      - table: "satisfaction_ratings"
      - table: "tickets"
      - table: "users"
        join-on: "default_group_id"

  - id: "group-membership-id"
    attribute: "group_membership_id"
    table: "groups"
    all-foreign-keys:
      - table: "group_memberships"
        join-on: "id"
      - table: ""

  - id: "macro-id"
    attribute: "macro_id"
    table: "macros"
    all-foreign-keys:
      - table: "macros"
        join-on: "id"
      - table: "ticket_audits"
        subtable: "events"

  - id: "organization-id"
    attribute: "organization_id"
    table: "organizations"
    all-foreign-keys:
      - table: "organizations"
        join-on: "id"
      - table: "tickets"
      - table: "users"

  - id: "restriction-id"
    attribute: "restriction_id"
    table: ""
    all-foreign-keys:
      - table: "macros"
        subattribute: "restriction"
        join-on: "id"
      - table: "groups"
        join-on: "id"
      - table: "users"
        join-on: "id"

  - id: "sla-policy-id"
    attribute: "sla_policy_id"
    table: ""
    all-foreign-keys:
      - table: "sla_policies"
        join-on: "id"

  - id: "tag-id"
    attribute: "name"
    table: "tags"
    all-foreign-keys:
      - table: "tags"
        join-on: "name"
      - table: "organizations"
        subtable: "tags"
        join-on: "value"
      - table: "tickets"
        subtable: "tags"
        join-on: "value"
      - table: "users"
        subtable: "tags"
        join-on: "value"

  - id: "ticket-audit-id"
    attribute: "audit_id"
    table: "ticket_audits"
    all-foreign-keys:
      - table: "ticket_audits"
        join-on: "id"
      - table: "ticket_audits"
        subtable: "events"
      - table: "ticket_comments"

  - id: "ticket-field-id"
    attribute: "ticket_field_id"
    table: "ticket_fields"
    all-foreign-keys:
      - table: "ticket_fields"
        join-on: "id"
      - table: "ticket_forms"
        subtable: "ticket_field_ids"
        join-on: "value"
      - table: "tickets"
        subtable: "custom_fields"
        join-on: "id"

  - id: "ticket-form-id"
    attribute: "ticket_form_id"
    table: "ticket_forms"
    all-foreign-keys:
      - table: "ticket_forms"
        join-on: "id"
      - table: "tickets"

  - id: "ticket-id"
    attribute: "ticket_id"
    table: "tickets"
    all-foreign-keys:
      - table: "satisfaction_ratings"
      - table: "tickets"
        join-on: "id"
      - table: "ticket_audits"
      - table: "ticket_comments"
      - table: "ticket_metrics"

  - id: "ticket-metric-id"
    attribute: "ticket_metric_id"
    table: "ticket_metrics"
    all-foreign-keys:
      - table: "ticket_metrics"
        join-on: "id"

  - id: "user-id"
    attribute: "user_id"
    table: "users"
    all-foreign-keys:
      - table: "satisfaction_ratings"
        join-on: "assignee_id"
      - table: "satisfaction_ratings"
        join-on: "requester_id"
      - table: "ticket_audits"
        join-on: "author_id"
      - table: "ticket_comments"
        join-on: "author_id"
      - table: "tickets"
        join-on: "requester_id"
      - table: "tickets"
        subtable: "follower_ids"
        join-on: "value"
      - table: "tickets"
        join-on: "submitter_id"
      - table: "tickets"
        subtable: "collaborator_ids"
        join-on: "value"
      - table: "tickets"
        join-on: "assignee_id"
      - table: "users"
        join-on: "id"
---
