---
tap-reference: "urban-airship"

version: "1"

foreign-keys: 
  - id: "channel-id"
    attribute: "channel_id"
    table: "channels"
    all-foreign-keys:
      - table: "channels"
      - table: "named_users"
        subtable: "channels"
        join-on: "value"

  - id: "list-name"
    attribute: "name"
    table: "lists"
    all-foreign-keys:
      - table: "lists"
      
  - id: "named-user-id"
    attribute: "named_user_id"
    table: "named_users"
    all-foreign-keys:
      - table: "channels"
      - table: "named_users"
   
  - id: "segment-id"
    attribute: "segment_id"
    table: "segments"
    all-foreign-keys:
      - table: "segments"
        join-on: "id"
---