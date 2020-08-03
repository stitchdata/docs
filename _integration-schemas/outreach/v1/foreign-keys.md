---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-foreign-keys/
## FOR INSTRUCTIONS & REFERENCE INFO

tap-reference: "outreach"

version: "1"

foreign-keys:
  - id: "account-id"
    table: "accounts"
    attribute: "id"
    all-foreign-keys:
      - table: "accounts"
        join-on: "id"

  - id: "disposition-id"
    table: "call_dispositions"
    attribute: "id"
    all-foreign-keys:
      - table: "call_dispositions"
        join-on: "id"

  - id: "purpose-id"
    table: "call_purposes"
    attribute: "id"
    all-foreign-keys:
      - table: "call_purposes"
        join-on: "id"
  
  - id: "call-id"
    table: "calls"
    attribute: "id"
    all-foreign-keys:
      - table: "calls"
        join-on: "id"

  - id: "content-id"
    table: "content_categories"
    attribute: "id"
    all-foreign-keys:
      - table: "content_categories"
        join-on: "id"

  - id: "duty-id"
    table: "duties"
    attribute: "id"
    all-foreign-keys:
      - table: "duties"
        join-on: "id"
  
  - id: "event-id"
    table: "events"
    attribute: "id"
    all-foreign-keys:
      - table: "event"
        join-on: "id"
  
  - id: "mailbox-id"
    table: "mailboxes"
    attribute: "id"
    all-foreign-keys:
      - table: "mailboxes"
        join-on: "id"
  
  - id: "mailing-id"
    table: "mailings"
    attribute: "id"
    all-foreign-keys:
      - table: "mailings"
        join-on: "id"
  
  - id: "opportunity-id"
    table: "opportunities"
    attribute: "id"
    all-foreign-keys:
      - table: "opportunities"
        join-on: "id"

  
  - id: "persona-id"
    table: "personas"
    attribute: "id"
    all-foreign-keys:
      - table: "personas"
        join-on: "id"
        
  - id: "prospect-id"
    table: "prospects"
    attribute: "id"
    all-foreign-keys:
      - table: "prospects"
        join-on: "id"
        
  - id: "stage-id"
    table: "stages"
    attribute: "id"
    all-foreign-keys:
      - table: "stages"
        join-on: "id"

  - id: "task-id"
    table: "tasks"
    attribute: "id"
    all-foreign-keys:
      - table: "tasks"
        join-on: "id"
        
  - id: "team-id"
    table: "teams"
    attribute: "id"
    all-foreign-keys:
      - table: "team"
        join-on: "id"
        
  - id: "user-id"
    table: "users"
    attribute: "id"
    all-foreign-keys:
      - table: "users"
        join-on: "id"                                                                              
---