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
  - id: "channel-id"
    table: "channels"
    attribute: "id"
    all-foreign-keys:
      - table: "channels"
        join-on: "id"
      - table: "channel_members"
        join-on: "channel_id"
      - table: "channel_id"
        join-on: "channel_id" 
      - table: "threads"
        join-on: "channel_id"
      - table: "messages"
        join-on: "channel-id"
      - table: "remote_files"
        subattribute: "channels"
        join-on: "value"       

  - id: "user-id"
    table: "users"
    attribute: "id"
    all-foreign-keys:
      - table: "users"
        join-on: "id"
      - table: "channel_members"
        join-on: "user_id"
      - table: "channels"
        subattribute: "members"
        join-on: "value"
      - table: "files"
        join-on: "user"
      - table: "messages"
        subattribute: "reactions.user"
        join-on: "value"
      - table: "messages"
        join-on: "user" 
      - table: "remote_files"
        join-on: "user"
      - table: "threads"
        join-on: "user"
      - table: "threads"
        subattribute: "reply_users"
        join-on: "value"
      - table: "user_groups"
        subattribute: "members"
        join-on: "value"
      - table: "channels"
        join-on: "creator"    

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

  - id: "team-id"
    table: "teams"
    attribute: "id"
    all-foreign-keys:
      - table: "teams"
        join-on: "id"
      - table: "threads"
        join-on: "team"  
      - table: "users"
        join-on: "team_id" 
      - table: "channels"
        subattribute: "pending_connected_team_ids"
        join-on: "value"    
---