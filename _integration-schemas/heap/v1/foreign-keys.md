---
tap-reference: "heap"
version: "1"

foreign-keys:
  - id: "event-id"
    attribute: "event_id"
    table: "events"
    all-foreign-keys:
      - table: "[event_type]"
      - table: "pageviews"
      - table: "sessions"

  - id: "session-id"
    attribute: "session_id"
    table: "sessions"
    all-foreign-keys:
      - table: "[event_type]"
      - table: "pageviews"
      - table: "sessions"

  - id: "user-id"
    attribute: "user_id"
    table: "users"
    all-foreign-keys:
      - table: "[event_type]"
      - table: "pageviews"
      - table: "sessions"
      - table: "user_migrations"
        join-on: "to_user_id"
      - table: "users"
---