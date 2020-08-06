---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-foreign-keys/
## FOR INSTRUCTIONS & REFERENCE INFO

tap-reference: "zoom"

version: "1"

foreign-keys:
  - id: "user-id"
    table: "users"
    attribute: "id"
    all-foreign-keys:
      - table: "users"
        join-on: "id"

  - id: "meeting-uuid"
    table: "meetings"
    attribute: "uuid"
    all-foreign-keys:
      - table: "meetings"
        join-on: "uuid"
      - table: "meeting_poll_results"  

  - id: "meeting-email"
    table: "meeting_poll_results"
    attribute: "email"
    all-foreign-keys:
      - table: "meeting_poll_results"
        join-on: "email"            
---