---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-structure"
key: "import-api-access-token-object"

# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Import API access token"
description: "{{ site.data.connect.data-structures.import-api-access-token.description | flatify }}"


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

object-attributes:
  - name: "access_token"
    type: "string"
    description: |
      An Import API access token. This token is valid only for the Import API source it is created for.
    value: |
      <IMPORT_API_ACCESS_TOKEN>

examples:
  - code: |
      {
        "access_token": "<IMPORT_API_ACCESS_TOKEN>"
      }
---