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
    attribute: "admin_id"
    all-foreign-keys:
      - table: "admins"
        join-on: "id"
      - table: "company_attributes"
      - table: "contact_attributes"
      - table: "contacts"
        join-on: "owner_id"
      - table: "conversation_parts"
        join-on: "assigned_to"
      - table: "conversations"
        subattribute: "conversation_rating.teammate"
        join-on: "id"
      - table: "conversations"
        subattribute: "tags.applied_by"
        join-on: "id"
      - table: "teams"
        subattribute: "admin_ids"
        join-on: "id"
      - table: "conversations"
        subattribute: "teammates.admins"
        join-on: "id"  

  - id: "company-id"
    table: "companies"
    attribute: "id"
    all-foreign-keys:
      - table: "companies"
        join-on: "id"

      - table: "contacts"
        subattribute: "companies.data"
        join-on: "id"

  - id: "company-segment-id"
    table: "company_segments"
    attribute: "id"
    all-foreign-keys:
      - table: "company_segments"
        join-on: "id"

  - id: "conversation-id"
    table: "conversations"
    attribute: "id"
    all-foreign-keys:
      - table: "conversations"
        join-on: "id"
      - table: "conversation_parts"
        join-on: "conversation_id"

  - id: "contact-id"
    table: "contacts"
    attribute: "id"
    all-foreign-keys:
      - table: "contacts"
      - table: "conversations"
        subattribute: "conversation_rating.customer"
      - table: "conversations"
        subattribute: "customers"
      - table: "conversations"
        subattribute: "contacts"
        join-on: "id"  

  - id: "segment-id"
    table: "segment"
    attribute: "id"
    all-foreign-keys:
      - table: "companies"
        subattribute: "segments"
        join-on: "id"
      - table: "segment"
        join-on: "id"  

  - id: "tag-id"
    table: "tags"
    attribute: "id"
    all-foreign-keys:
      - table: "contacts"
        subattribute: "tags.data"
        join-on: "id"
      - table: "conversations"
        subattribute: "tags"
        join-on: "id"
      - table: "companies"
        subattribute: "tags"
        join-on: "id"
      - table: "tags"
        join-on: "id"

  - id: "team-id"
    table: "teams"
    attribute: "id"
    all-foreign-keys:
      - table: "admins"
        subattribute: "team_ids"
        join-on: "value"
      - table: "teams"
        join-on: "id"
---