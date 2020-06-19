---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-foreign-keys/
## FOR INSTRUCTIONS & REFERENCE INFO

tap-reference: "trello"

version: "1"

foreign-keys:
  - id: "actions-id"
    table: "actions"
    attribute: "id"
    all-foreign-keys:
      - table: "actions"
        join-on: "id"  

  - id: "boards-id"
    table: "boards"
    attribute: "id"
    all-foreign-keys:
      - table: "boards"
        join-on: "id"
      - table: "actions"
        subattribute: "data.board" 
        join-on: "id"
      - table: "checklists"
        subattribute: "data.board"
        join-on: "id"
      - table: "users"
        join-on: "boardId"  
        
  - id: "cards-id"
    table: "cards"
    attribute: "id"
    all-foreign-keys:
      - table: "cards"
        join-on: "id"
      - table: "checklists"
        subattribute: "data.card"
        join-on: "id" 
        
  - id: "checklists-id"
    table: "checklists"
    attribute: "id"
    all-foreign-keys:
      - table: "checklists"
        join-on: "id"
        
  - id: "lists-id"
    table: "lists"
    attribute: "id"
    all-foreign-keys:
      - table: "lists"
        join-on: "id"
        
  - id: "users-id"
    table: "users"
    attribute: "id"
    all-foreign-keys:
      - table: "users"
        join-on: "id"                              
---