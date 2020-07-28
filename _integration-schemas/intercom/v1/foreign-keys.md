---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-foreign-keys/
## FOR INSTRUCTIONS & REFERENCE INFO

tap-reference: "intercom"

version: "1"

foreign-keys:
  - id: "admin-id"
    table: "admins"
    attribute: "id"
    all-foreign-keys:
      - table: "admins"
        join-on: "id"
      - table: "teams"
        subattribute: "admin_ids"
        join-on: "id"  
  
  - id: "team-id"
    table: "teams"
    attribute: "id"
    all-foreign-keys:
      - table: "teams"
        join-on: "id"
      - table: "admins"
        join-on: "team_ids" 

  - id: "company-id"
    table: "companies"
    attribute: "id"
    all-foreign-keys:
      - table: "companies"
        join-on: "id"
      - table: "leads"
        subattribute: "companies"
        join-on: "id"  
      - table: "users"
        subattribute: "companies"
        join-on: "id"  

  - id: "segment-id"
    table: "segment"
    attribute: "id"
    all-foreign-keys:
      - table: "segment"
        join-on: "id"
      - table: "companies"
        subattribute: "segments"
        join-on: "id"
      - table: "leads"
        subattribute: "segments"
        join-on: "id"
      - table: "users"
        subattribute: "segments"
        join-on: "id"  

  - id: "tag-id"
    table: "tags"
    attribute: "id"
    all-foreign-keys:
      - table: "tags"
        join-on: "id"
      - table: "companies"
        subattribute: "tags"
        join-on: "id"
      - table: "conversations"
        subattribute: "tags"
        join-on: "id"
      - table: "leads"
        subattribute: "tags"
        join-on: "id" 
      - table: "users"
        subattribute: "tags"
        join-on: "id"  

  - id: "attribute-name"
    table: "company_attributes"
    attribute: "name"
    all-foreign-keys:
      - table: "company_attributes"
        join-on: "name"

  - id: "company-segment"
    table: "company_segments"
    attribute: "id"
    all-foreign-keys:
      - table: "company_segments"
        join-on: "id"

  - id: "part-id"
    table: "conversation_parts"
    attribute: "id"
    all-foreign-keys:
      - table: "conversation_parts"
        join-on: "id"
  
  - id: "conversation-id"
    table: "conversations"
    attribute: "id"
    all-foreign-keys:
      - table: "conversations"
        join-on: "id"
      - table: "conversation_parts"
        join-on: "conversation_id"

  - id: "author-id"
    table: "authors"
    attribute: "id"
    all-foreign-keys:
      - table: "conversation_parts"
        subattribute: "author"
        join-on: "id"
      - table: "conversations"
        subattribute: "conversation_message.author"
        join-on: "id"  

  - id: "assignee-id"
    table: "assignees"
    attribute: "id"
    all-foreign-keys:
      - table: "conversations"
        subattribute: "assignee"
        join-on: "id"

  - id: "customer-id"
    table: "customers"
    attribute: "id"
    all-foreign-keys:
      - table: "customers"
        join-on: "id"
      - table: "conversations"
        subattribute: "customers"
        join-on: "id"

  - id: "user-id"
    table: "users"
    attribute: "id"
    all-foreign-keys:
      - table: "users"
        join-on: "id"
      - table: "conversations"
        subattribute: "user"
        join-on: "id"  

  - id: "customer-attribute-name"
    table: "customer_attributes"
    attribute: "name"
    all-foreign-keys:
      - table: "customer_attributes"
        join-on: "name"      
---