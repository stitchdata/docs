---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-foreign-keys/
## FOR INSTRUCTIONS & REFERENCE INFO

tap-reference: "sailthru"

version: "1"

foreign-keys:
  - id: "list-id"
    table: "lists"
    attribute: "list_id"
    all-foreign-keys:
      - table: "lists"
        join-on: "list_id"
      - table: "ad_targeter_plans"
        join-on: "list"
      - table: "blast_save_list"
        join-on: "lists"
      - table: "users"
        subattribute: "users.lists"
        join-on: "value"
      - table: "blasts"
        join-on: "list"
      - table: "blast_repeats"    

  - id: "blast-id"
    table: "blasts"
    attribute: "blast_id"
    all-foreign-keys:
      - table: "blasts"
        join-on: "blast_id"
      - table: "blast_query"
        join-on: "blast_id"  
        
  - id: ""
    table: ""
    attribute: ""
    all-foreign-keys:
      - table: ""
        join-on: ""
        
  - id: ""
    table: ""
    attribute: ""
    all-foreign-keys:
      - table: ""
        join-on: ""
        
  - id: ""
    table: ""
    attribute: ""
    all-foreign-keys:
      - table: ""
        join-on: ""
        
  - id: ""
    table: ""
    attribute: ""
    all-foreign-keys:
      - table: ""
        join-on: ""                              
---