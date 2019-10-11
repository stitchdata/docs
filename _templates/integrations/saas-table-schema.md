---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/integration-templates/saas-table-schema/
## FOR INSTRUCTIONS & REFERENCE INFO


tap: "integration_name"
# version: 

key: ""
name: "table_name"
doc-link: 
singer-schema: 
description: |
  ## description of the table

replication-method: "Key-based Incremental / Full Table"

## Used when the Replication Key is *not* an actual column,
## but an API query parameter, etc.
replication-key:
  name: ""

api-method:
  name: ""
  doc-link: ""

attributes:
  # The output from running the json_to_yaml.rb script should go here.
  # It needs to be indented two spaces from the left, like this:

# - name: "id"
#   type: "string"
#   description: "I'm an ID!" 
---