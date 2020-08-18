---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-foreign-keys/
## FOR INSTRUCTIONS & REFERENCE INFO

tap-reference: "slack"

version: "1"

foreign-keys:
  - id: "conversation-id"
    table: "channels"
    attribute: "id"
    all-foreign-keys:
      - table: "channels"
        join-on: "conversation-id"
      - table: "channel_members"
        join-on: "channel_id"
      - table: "channel_id"
        join-on: "channel_id" 
      - table: "threads"
        join-on: "channel_id"     

  - id: "user-id"
    table: "users"
    attribute: "id"
    all-foreign-keys:
      - table: "users"
        join-on: "id"
      - table: "channel_members"
        join-on: "user_id"  

  - id: "timestamp"
    table: "messages"
    attribute: "ts"
    all-foreign-keys:
      - table: "messages"
        join-on: "ts"
      - table: "threads"
        join-on: "ts"  

  - id: "thread-timestamp"
    table: "threads"
    attribute: "thread_ts"
    all-foreign-keys:
      - table: "threads"
        join-on: "thread_ts"

  - id: "group-id"
    table: "user_groups"
    attribute: "id"
    all-foreign-keys:
      - table: "user_groups"
        join-on: "id"

  - id: "file-id"
    table: "files"
    attribute: "id"
    all-foreign-keys:
      - table: "files"
        join-on: "id"

  - id: "remote-file-id"
    table: "remote_files"
    attribute: "id"
    all-foreign-keys:
      - table: "remote_files"
        join-on: "id"
---