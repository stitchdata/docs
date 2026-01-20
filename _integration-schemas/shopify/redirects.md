---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-table-schema/
## FOR INSTRUCTIONS & REFERENCE INFO


tap: "shopify"
version: "1"

key: "id"
name: "redirects"
doc-link: https://shopify.dev/api/admin-rest/2021-10/resources/redirect
singer-schema: https://github.com/singer-io/tap-shopify/blob/master/tap_shopify/schemas/redirects.json
description: |
  The `{{ table.name }}` table contains info about URL redirects.

replication-method: "Full Table"

api-method:
  name: "Retrieves a list of URL redirects"
  doc-link: "https://shopify.dev/api/admin-rest/2021-10/resources/redirect#[get]/admin/api/2021-10/redirects.json"

attributes:
  - name: "id"
    type: "integer"
    description: "The redirect ID." 
  - name: "path"
    type: "string"
    description: "The source path that is redirected." 
  - name: "target"
    type: "string"
    description: "The target location of the redirect (path or full URL)." 
---