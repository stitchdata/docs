---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-foreign-keys/
## FOR INSTRUCTIONS & REFERENCE INFO

tap-reference: "selligent"

version: "1"

foreign-keys:
  - id: "campaign-id"
    table: "campaign"
    attribute: "asset_id"
    all-foreign-keys:
      - table: "campaign"
        join-on: "asset_id"

  - id: "internal-id"
    table: "internal_datasource"
    attribute: "id"
    all-foreign-keys:
      - table: "internal_datasource"
        join-on: "asset_id"
        
  - id: "owner-id"
    table: "owner"
    attribute: "asset_id"
    all-foreign-keys:
      - table: "owner"
        join-on: "asset_id"
        
  - id: "program-id"
    table: "program"
    attribute: "id"
    all-foreign-keys:
      - table: "program"
        join-on: "id"
        
  - id: "source-id"
    table: "source"
    attribute: "asset_id"
    all-foreign-keys:
      - table: "source"
        join-on: "asset_id"
        
  - id: "transactional-id"
    table: "transactional_mailing"
    attribute: "id"
    all-foreign-keys:
      - table: "transactional_mailing"
        join-on: "id"                              
---