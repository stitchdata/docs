---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-foreign-keys/
## FOR INSTRUCTIONS & REFERENCE INFO

tap-reference: "ms-teams"

version: "1"

foreign-keys:
  - id: "channel-id"
    table: "channels"
    attribute: "id"
    all-foreign-keys:
      - table: "channels"
        join-on: "id"
      - table: "channel"
        join-on: "id"  
      - table: "channel_members"
        join-on: "channel_id" 
      - table: "channel_tabs"
        join-on: "channel_id"
      - table: "channel_messages"
        subattribute: "channel_identity"
        join-on: "channel_id"   
      - table: "channel_message_replies"
        subattribute: "channel_identity"
        join-on: "channel_id"

  - id: "conversation-members-id"
    table: "channel_members"
    attribute: "id"
    all-foreign-keys:
      - table: "channel_members"
        join-on: "id"

  - id: "conversation-id"
    table: "conversations"
    attribute: "id"
    all-foreign-keys:
      - table: "conversation"
        join-on: "id"
      - table: "conversation_threads" 
        join-on: "conversation_id" 
      - table: "conversation_posts"
        join-on: "conversation_id" 

  - id: "drive-id"
    table: "team_drives"
    attribute: "id"
    all-foreign-keys:
      - table: "team_drives"
        join-on: "id" 

  - id: "group-id"
    table: "groups"
    attribute: "id"
    all-foreign-keys:
      - table: "groups"
        join-on: "id"
      - table: "group_owners"
        join-on: "group_id"
      - table: "channel_tabs"
        join-on: "group_id"
      - table: "conversations"
        join-on: "group_id"   
      - table: "conversation_threads"
        join-on: "group_id" 
      - table: "team_drives"
        subattribute: "owner.group"
        join-on: "id"   
  - id: "member-id"
    table: "group_members"
    attribute: "id"
    all-foreign-keys:
      - table: "group_members"
        join-on: "id"

  - id: "message-id"
    table: "channel_messages"
    attribute: "id"
    all-foreign-keys:
      - table: "channel_messages"
        join-on: "id"

  - id: "owner-id"
    table: "group_owners"
    attribute: "id"
    all-foreign-keys:
      - table: "group_owners"
        join-on: "id"

  - id: "post-id"
    table: "conversation_posts"
    attribute: "id"
    all-foreign-keys:
      - table: "conversation_posts"
        join-on: "id"  

  - id: "reply-id"
    table: "channel_message_replies"
    attribute: "id"
    all-foreign-keys:
      - table: "channel_messages_replies"
        join-on: "id"

  - id: "tab-id"
    table: "channel_tabs"
    attribute: "id"
    all-foreign-keys:
      - table: "channel_tabs"
        join-on: "id"

  - id: "thread-id"
    table: "conversation_threads"
    attribute: "id"
    all-foreign-keys:
      - table: "conversation_threads"
        join-on: "id"
      - table: "conversation_posts"
        join-on: "thread_id"

  - id: "user-id"
    table: "users"
    attribute: "user.id"
    all-foreign-keys:
      - table: "users"
        join-on: "id"
      - table: "channel_members"
        join-on: "user_id"
      - table: "channel_message_replies"
        subattribute: "from"
      - table: "channel_message_replies"
        subattribute: "mentions.mentioned"
      - table: "channel_message_replies"
        subattribute: "reactions.user"
      - table: "channel_messages"
        subattribute: "from"
      - table: "channel_messages"
        subattribute: "mentions.mentioned"
      - table: "channel_messages"
        subattribute: "reactions.user"  
---