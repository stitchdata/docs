---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-foreign-keys/
## FOR INSTRUCTIONS & REFERENCE INFO

tap-reference: "dixa"

version: "1"

foreign-keys:
  - id: "conversation-id"
    table: "conversations"
    attribute: "id"
    all-foreign-keys:
      - table: "conversations"
        join-on: "id"
      - table: "activity_logs"
        join-on: "conversationId"  

  - id: "message-id"
    table: "messages"
    attribute: "id"
    all-foreign-keys:
      - table: "messages"
        join-on: "id"
      - table: "activity_logs"
        subattribute: "attributes"
        join-on: "messageId"             
---