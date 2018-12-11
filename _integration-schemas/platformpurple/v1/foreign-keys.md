---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-foreign-keys/
## FOR INSTRUCTIONS & REFERENCE INFO

tap-reference: "platformpurple"

version: "1.0"

foreign-keys:
  - id: "product-id"
    table: "products"
    attribute: "productID"
    all-foreign-keys:
      - table: "products"
      - table: "events"
      - table: "transactions"   
---