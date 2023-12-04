---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-foreign-keys/
## FOR INSTRUCTIONS & REFERENCE INFO

tap-reference: "zendesk-chat"

version: "1"

foreign-keys:
  - id: "account-id"
    table: "account"
    attribute: "account-key"
    all-foreign-keys:
      - table: "account"
        join-on: "id"

  - id: "agent-id"
    table: "agents"
    attribute: "id"
    all-foreign-keys:
      - table: "agents"
        join-on: "id"
      - table: "chats"
        subattribute: "agent_ids"
        join-on: "value"
      - table: "chats"
        subtattribute: "conversions.attribution"
        join-on: "agent_id"
      - table: "chats"
        subtattribute: "count"
        join-on: "agent"
      - table: "chats"
        subtattribute: "history.conversion.attribution"
        join-on: "agent_id"      
        
  - id: "ban-id"
    table: "bans"
    attribute: "id"
    all-foreign-keys:
      - table: "bans"
        join-on: "id"
        

  - id: "chat-id"
    table: "chats"
    attribute: "id"
    all-foreign-keys:
      - table: "chats"
        join-on: "id"
        
  - id: "department-id"
    table: "departments"
    attribute: "id"
    all-foreign-keys:
      - table: "departments"
        join-on: "id"
      - table: "shortcuts"
        subattribute: "departments"
        join-on: "id"
      - table: "chats"
        join-on: "department_id" 
      - table: "chats"
        subtattribute: "history.conversion.attribution"
        join-on: "department_id"
      - table: "chats"
        subtattribute: "history"
        join-on: "department_id"
      - table: "chats"
        subtattribute: "history"
        join-on: "prev_department_id"
      - table: "agents"
        subtattribute: "departments"
        join-on: "value"       
        
  - id: "goal-id"
    table: "goals"
    attribute: "id"
    all-foreign-keys:
      - table: "goals"
        join-on: "id"
      - table: "chats"
        subattribute: "conversions"
        join-on: "goal_id"
      - table: "chats"
        subattribute: "history.conversion"
        join-on: "goal_id"
      - table: "account"
        subattribute: "plan"
        join-on: "goals"    
        
  - id: "shortcut-id"
    table: "shortcuts"
    attribute: "name"
    all-foreign-keys:
      - table: "shortcuts"
        join-on: "id"
        
  - id: "trigger-id"
    table: "triggers"
    attribute: "id"
    all-foreign-keys:
      - table: "triggers"
        join-on: "id"                                          
---