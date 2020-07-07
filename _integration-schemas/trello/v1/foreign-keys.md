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
  - id: "action-id"
    table: "actions"
    attribute: "id"
    all-foreign-keys:
      - table: "actions"
        join-on: "id"

  - id: "board-id"
    table: "boards"
    attribute: "idBoard"
    all-foreign-keys:
      - table: "boards"
        join-on: "id"

      - table: "actions"
        subattribute: "data.board"
        join-on: "id"

      - table: "cards"

      - table: "checklists"
        subattribute: "data.board"
        join-on: "id"

      - table: "cards"
        subattribute: "labels"

      - table: "checklists"

      - table: "lists"

      - table: "users"
        join-on: "boardId" 
        
  - id: "card-id"
    table: "cards"
    attribute: "idCard"
    all-foreign-keys:
      - table: "actions"
        subattribute: "data.card"
        join-on: "id"

      - table: "cards"
        join-on: "id"

      - table: "checklists"

      - table: "checklists"
        subattribute: "data.card"
        join-on: "id" 
        
  - id: "checklist-id"
    table: "checklists"
    attribute: "idCheckList"
    all-foreign-keys:
      - table: "cards"
        subattribute: "idChecklists"
        join-on: "value"

      - table: "checklists"
        join-on: "id"

      - table: "checklists"
        subattribute: "checkItems"

      - table: "checklists"
        subattribute: "data.checklist"
        join-on: "id"
        
  - id: "list-id"
    table: "lists"
    attribute: "idList"
    all-foreign-keys:
      - table: "actions"
        subattribute: "data.card"

      - table: "actions"
        subattribute: "data.list"
        join-on: "id"

      - table: "actions"
        subattribute: "data.listAfter"
        join-on: "id"

      - table: "actions"
        subattribute: "data.listBefore"
        join-on: "id"

      - table: "actions"
        subattribute: "data.old"

      - table: "cards"

      - table: "checklists"

      - table: "checklists"
        subattribute: "data.list"
        join-on: "id"

      - table: "lists"
        join-on: "id"

  - id: "organization-id"
    table: ""
    attribute: "idOrganization"
    all-foreign-keys:
      - table: "actions"
        subattribute: "data.organization"
        join-on: "id"

      - table: "boards"

      - table: "checklists"

      - table: "checklists"
        subattribute: "data.organization"
        join-on: "id"

  - id: "tag-id"
    table: ""
    attribute: ""
    all-foreign-keys:
      - table: "boards"
        subattribute: "idTags"
        join-on: "value"
        
  - id: "user-id"
    table: "users"
    attribute: "idMember"
    all-foreign-keys:
      - table: "actions"
        join-on: "idMemberCreator"

      - table: "actions"
        subattribute: "data"

      - table: "actions"
        subattribute: "data"
        join-on: "idMemberAdded"

      - table: "actions"
        subattribute: "data"
        join-on: "idMemberInviter"

      - table: "actions"
        subattribute: "data.card.idMembers"
        join-on: "value"

      - table: "actions"
        subattribute: "data.member"
        join-on: "id"

      - table: "actions"
        subattribute: "data.old.idMembers"
        join-on: "value"

      - table: "actions"
        subattribute: "member"

      - table: "actions"
        subattribute: "memberCreator"

      - table: "boards"
        subattribute: "memberships"

      - table: "cards"
        subattribute: "idMembers"
        join-on: "value"

      - table: "cards"
        subattribute: "idMembersVoted"
        join-on: "value"

      - table: "checklists"
        subattribute: "checkItems"

      - table: "checklists"
        join-on: "idMemberCreator"

      - table: "checklists"
        subattribute: "memberCreator"
        join-on: "id"

      - table: "checklists"
        subattribute: "memberships"

      - table: "users"                 
---