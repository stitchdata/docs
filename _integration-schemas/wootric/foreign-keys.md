---
tap-reference: "wootric"

version: "1"

foreign-keys: 
  - id: "wootric-id"
    attribute: ""
    table: "declines"
    all-foreign-keys:
      - table: "declines"
        join-on: "id"

  - id: "end-user-id"
    attribute: "end_user_id"
    table: "end_users"
    all-foreign-keys:
      - table: "declines"
      - table: "end_users"
        join-on: "id"
      - table: "responses"

  - id: "survey-id"
    attribute: "survey_id"
    table: "responses"
    all-foreign-keys:
      - table: "declines"
      - table: "responses"
---