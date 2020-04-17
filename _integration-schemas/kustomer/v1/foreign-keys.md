---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-foreign-keys/
## FOR INSTRUCTIONS & REFERENCE INFO

tap-reference: "integration"

version: "1"

foreign-keys:
  - id: "user-id"
    table: "users"
    attribute: "id"
    all-foreign-keys:
      - table: "users"
        join-on: "id"

  - id: "team-id"
    table: "teams"
    attribute: "id"
    all-foreign-keys:
      - table: "teams"
        join-on: "id" 

  - id: "tag-id"
    table: "tags"
    attribute: "id"
    all-foreign-keys:
      - table: "tags"
        join-on: "id"

  - id: "shortcut-id"
    table: "shortcuts"
    attribute: "id"
    all-foreign-keys:
      - table: "shortcuts"
        join-on: "id"

  - id: "note-id"
    table: "notes"
    attribute: "id"
    all-foreign-keys:
      - table: "notes"
        join-on: "id"
        
  - id: "kobject-id"
    table: "kobjects"
    attribute: "id"
    all-foreign-keys:
      - table: "kobjects"
        join-on: "id"
        
  - id: "customer-id"
    table: "customers"
    attribute: "id"
    all-foreign-keys:
      - table: "customers"
        join-on: "id"
        
  - id: "conversation-id"
    table: "conversations"
    attribute: "id"
    all-foreign-keys:
      - table: "conversations"
        join-on: "id"                                          
---