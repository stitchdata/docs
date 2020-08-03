---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-foreign-keys/
## FOR INSTRUCTIONS & REFERENCE INFO

tap-reference: "ujet"

version: "1"

foreign-keys:
  - id: "agent-id"
    table: "agents"
    attribute: "agent_id"
    all-foreign-keys:
      - table: "agents"
        join-on: "id"
      - table: "agent_activity_logs"
      - table: "calls"
      - table: "calls"
        subattribute: "transfers.from_agent"
        join-on: "id"
      - table: "calls"
        subattribute: "transfers.to_agent"
        join-on: "id"
      - table: "chats"
        subattribute: "transfers.from_agent"
        join-on: "id"
      - table: "chats"
        subattribute: "transfers.to_agent"
        join-on: "id"
      - table: "menus"
        subattribute: "agent_assignments.assignees"
        join-on: "id"
      - table: "menus"
        subattribute: "team_assignments.assignees"
        join-on: "id"
      - table: "trees"
        subattribute: "assignees"
        join-on: "id"

  - id: "call-id"
    table: "calls"
    attribute: "call_id"
    all-foreign-keys:
      - table: "agent_activity_logs"
      - table: "calls"
        join-on: "id"
      - table: "calls"
        subattribute: "participants"

  - id: "chat-id"
    table: "chats"
    attribute: "chat_id"
    all-foreign-keys:
      - table: "agent_activity_logs"
      - table: "chats"
        join-on: "id"
      - table: "chats"
        subattribute: "participants"

  - id: "team-id"
    table: "teams"
    attribute: "team_id"
    all-foreign-keys:
      - table: "agents"
        subattribute: "teams"
        join-on: "id"
      - table: "menus"
        subattribute: "team_assignments.team"
        join-on: "id"
      - table: "teams"
        join-on: "id"
---