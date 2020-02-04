---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-foreign-keys/
## FOR INSTRUCTIONS & REFERENCE INFO

tap-reference: "google-sheets"

version: "1.0"

foreign-keys:
  - id: "file-id"
    table: "file_metadata"
    attribute: "id"
    all-foreign-keys:
      - table: "file_metadata"
        join-on: "id"
---