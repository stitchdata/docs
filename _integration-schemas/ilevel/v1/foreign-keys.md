---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-foreign-keys/
## FOR INSTRUCTIONS & REFERENCE INFO

tap-reference: "ilevel"

version: "1"

foreign-keys:
  - id: "asset-id"
    table: "assets"
    attribute: "asset_id"
    all-foreign-keys:
      - table: "asset_to_asset_relations"
        join-on: "from_id"
      - table: "asset_to_asset_relations"
        join-on: "to_id"
      - table: "assets"
        join-on: "id"
      - table: "data_items"
      - table: "fund_to_asset_relations"
        join-on: "to_id"
      - table: "securities"

  - id: "data-item-id"
    table: "data_items"
    attribute: "data_item_id"
    all-foreign-keys:
      - table: "data_items"
        join-on: "id"
      - table: "periodic_data_calculated"
      - table: "periodic_data_standardized"

  - id: "fund-id"
    table: "funds"
    attribute: "fund_id"
    all-foreign-keys:
      - table: "assets"
        join-on: "lead_fund_id"
      - table: "fund_to_asset_relations"
        join-on: "from_id"
      - table: "fund_to_fund_relations"
        join-on: "from_id"
      - table: "fund_to_fund_relations"
        join-on: "to_id"
      - table: "funds"
        join-on: "id"

  - id: "investment-id"
    table: "investments"
    attribute: "id"
    all-foreign-keys:
      - table: "investment_transactions"
        subattribute: "investment"
      - table: "investments"

  - id: "scenario-id"
    table: "scenarios"
    attribute: "id"
    all-foreign-keys:
      - table: "investment_transactions"
        subattribute: "scenario"
      - table: "periodic_data_calculated"
      - table: "periodic_data_standardized"
      - table: "scenarios"

  - id: "security"
    table: "securities"
    attribute: "id"
    all-foreign-keys:
      - table: "investment_transactions"
        subattribute: "security"
      - table: "investments"
      - table: "securities"
---