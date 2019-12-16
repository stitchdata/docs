---
tap-reference: "freshdesk"

version: "1.0"

foreign-keys:
  - id: "agent-id"
    attribute: "agent_id"
    table: "agents"
    all-foreign-keys:
      - table: "agents"
        join-on: "id"
      - table: "groups"
        subtable: "agent_ids"
        join-on: "value"
      - table: "satisfaction_ratings"
      - table: "tickets"
        join-on: "responder_id"
      - table: "time_entries"

  - id: "company-id"
    attribute: "company_id"
    table: "companies"
    all-foreign-keys:
      - table: "companies"
        join-on: "id"
      # - table: "contacts"
      - table: "tickets"

  - id: "contact-id"
    attribute: "contact_id"
    table: "contacts"
    all-foreign-keys:
      - table: "contacts"
        join-on: "id"

  - id: "conversation-id"
    attribute: "conversation_id"
    table: "conversations"
    all-foreign-keys:
      - table: "conversations"
        join-on: "id"

  - id: "group-id"
    attribute: "group_id"
    table: "groups"
    all-foreign-keys:
      - table: "agents"
        subtable: "group_ids"
        join-on: "type"
      - table: "groups"
        join-on: "id"
      - table: "satisfaction_ratings"
      - table: "tickets"
      - table: "time_entries"

  - id: "role-id"
    attribute: "role_id"
    table: "roles"
    all-foreign-keys:
      - table: "agents"
        subtable: "role_ids"
        join-on: "type"
      - table: "roles"
        join-on: "id"

  - id: "satisfaction-rating-id"
    attribute: "satisfaction_rating_id"
    table: "satisfaction_ratings"
    all-foreign-keys:
      - table: "satisfaction_ratings"
        join-on: "id"

  - id: "ticket-id"
    attribute: "ticket_id"
    table: "tickets"
    all-foreign-keys:
      - table: "conversations"
      - table: "tickets"
        join-on: "id"
      - table: "satisfaction_ratings"

  - id: "time-entry-id"
    attribute: "time_entry_id"
    table: "time_entries"
    all-foreign-keys:
      - table: "time_entries"
        join-on: "id"
---