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

      - table: "files"
        subattribute: "channels"
        join-on: "value"
      - table: "files"
        subattribute: "pinned_to"
        join-on: "value"

      - table: "messages"
        join-on: "channel_id"
      - table: "messages"
        subattribute: "pinned_to"
        join-on: "value"

      - table: "remote_files"
        subattribute: "channels"
        join-on: "value"
      - table: "remote_files"
        subattribute: "pinned_to"
        join-on: "value"

      - table: "threads"    

  - id: "group-id"
    table: "user_groups"
    attribute: "id"
    all-foreign-keys:
      - table: "files"
        subattribute: "groups"
        join-on: "value"

      - table: "remote_files"
        subattribute: "groups"
        join-on: "value"

      - table: "user_groups"
        join-on: "id"
      
      - table: "user_groups"
        join-on: "parent_group"   

  - id: "file-id"
    table: "files"
    attribute: "id"
    all-foreign-keys:
      - table: "files"
        join-on: "id"
      - table: "messages"
        subattribute: "file_ids"
        join-on: "value"

  - id: "team-id"
    table: "teams"
    attribute: "id"
    all-foreign-keys:
      - table: "channels"
        subattribute: "pending_connected_team_ids"
        join-on: "value" 
      - table: "channels"
        subattributes: "shared_team_ids"
        join-on: "value"

      - table: "files"
        join-on: "source_team"
      - table: "files"
        join-on: "user_team"

      - table: "messages"
        subattribute: "bot_profile"
        join-on: "team_id"   
      - table: "messages"
        join-on: "team"
      - table: "messages"
        join-on: "source_team"
      - table: "messages"
        join-on: "user_team" 

      - table: "remote_files"
        join-on: "source_team"
      - table: "remote_files"
        join-on: "user_team"

      - table: "teams"
        join-on: "id"
      - table: "threads"
        join-on: "team"  
      - table: "users"
        join-on: "team_id" 

  - id: "user-id"
    table: "users"
    attribute: "user"
    all-foreign-keys:
      - table: "channel_members"
        join-on: "user_id"
      - table: "channels"
        join-on: "creator"
      - table: "channels"
        subattribute: "members"
        join-on: "value"

      - table: "files"
      - table: "messages"
        subattribute: "reply_users"
        join-on: "value"
      - table: "messages"
        subattribute: "reactions.users"
        join-on: "value"
      - table: "messages"

      - table: "remote_files"

      - table: "threads"
      - table: "threads"
        subattribute: "reply_users"
        join-on: "value"

      - table: "user_groups"
        subattribute: "members"
        join-on: "value"
      - table: "user_groups"
        subattribute: "purpose"
        join-on: "creator"
      - table: "user_groups"
        subattribute: "topic"
        join-on: "creator" 

      - table: "users"
        join-on: "id"          
---