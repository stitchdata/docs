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
      - table: "opportunities"
      - table: "prospects"
      - table: "sequence_states"
      - table: "tasks"

  - id: "call-disposition-id"
    table: "call_dispositions"
    attribute: "callDispositionId"
    all-foreign-keys:
      - table: "call_dispositions"
        join-on: "id"
      - table: "calls"

  - id: "call-purpose-id"
    table: "call_purposes"
    attribute: "callPurposeId"
    all-foreign-keys:
      - table: "call_purposes"
        join-on: "id"
      - table: "calls"
  
  - id: "call-id"
    table: "calls"
    attribute: "callId"
    all-foreign-keys:
      - table: "calls"
        join-on: "id"
      - table: "tasks"

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
      - table: "users"
        subattribute: "duties"
  
  - id: "event-id"
    table: "events"
    attribute: "id"
    all-foreign-keys:
      - table: "event"
        join-on: "id"
  
  - id: "mailbox-id"
    table: "mailboxes"
    attribute: "mailboxId"
    all-foreign-keys:
      - table: "mailboxes"
        join-on: "id"
      - table: "mailings"
      - table: "users"
  
  - id: "mailing-id"
    table: "mailings"
    attribute: "mailingId"
    all-foreign-keys:
      - table: "events"
      - table: "mailings"
        join-on: "id"
      - table: "tasks"
  
  - id: "opportunity-id"
    table: "opportunities"
    attribute: "opportunityId"
    all-foreign-keys:
      - table: "calls"
      - table: "mailings"
      - table: "opportunities"
        join-on: "id"
      - table: "tasks"

  - id: "persona-id"
    table: "personas"
    attribute: "personaId"
    all-foreign-keys:
      - table: "personas"
        join-on: "id"
      - table: "prospects"
        
  - id: "prospect-id"
    table: "prospects"
    attribute: "prospectId"
    all-foreign-keys:
      - table: "calls"
      - table: "events"
      - table: "mailings"
      - table: "prospects"
        join-on: "id"
      - table: "sequence_states"
      - table: "tasks"

  - id: "sequence-id"
    table: "sequences"
    attribute: "sequenceId"
    all-foreign-keys:
      - table: "calls"
      - table: "mailings"
      - table: "sequence_states"
      - table: "sequence_steps"
      - table: "tasks"

  - id: "sequence-state-id"
    table: "sequence_states"
    attribute: "sequenceStateId"
    all-foreign-keys:
      - table: "calls"
      - table: "mailings"
      - table: "sequence_states"
      - table: "tasks"

  - id: "sequence-step-id"
    table: "sequence_steps"
    attribute: "sequenceStepId"
    all-foreign-keys:
      - table: "calls"
      - table: "mailings"
      - table: "sequence_steps"
      - table: "tasks"
        
  - id: "stage-id"
    table: "stages"
    attribute: "opportunityStageId"
    all-foreign-keys:
      - table: "opportunities"
      - table: "prospects"
        join-on: "stageId"
      - table: "stages"
        join-on: "id"

  - id: "task-id"
    table: "tasks"
    attribute: "id"
    all-foreign-keys:
      - table: "calls"
      - table: "mailings"
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
    attribute: "creatorId"
    all-foreign-keys:
      - table: "accounts"
      - table: "accounts"
        join-on: "ownerId"
      - table: "accounts"
        join-on: "updaterId"
      - table: "call_dispositions"
      - table: "call_purposes"
      - table: "calls"
        join-on: "userId"
      - table: "content_categories"
      - table: "events"
      - table: "mailboxes"
      - table: "mailboxes"
        join-on: "updaterId"
      - table: "mailboxes"
        join-on: "userId"
      - table: "opportunities"
      - table: "opportunities"
        join-on: "ownerId"
      - table: "prospects"
      - table: "prospects"
        join-on: "updaterId"
      - table: "sequence_states"
      - table: "sequence_steps"
      - table: "sequence_steps"
        join-on: "updaterId"
      - table: "sequence_templates"
      - table: "sequence_templates"
        join-on: "updaterId"
      - table: "sequences"
      - table: "sequences"
        join-on: "ownerId"
      - table: "sequences"
        join-on: "updaterId"
      - table: "stages"
      - table: "stages"
        join-on: "updaterId"
      - table: "tasks"
      - table: "tasks"
        join-on: "completerId"
      - table: "users"
      - table: "users"
        join-on: "id"
      - table: "users"
        join-on: "updaterId"
---