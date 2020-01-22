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
description: |
  {{ site.data.connect.data-structures.import-api-access-token.description | flatify }}

  **Note**: The API will only return the Import API access token once, immediately after a successful request to the [Generate Import API access token]({{ site.data.connect.core-objects.sources.create-iapi-token.anchor }}) endpoint.


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

object-attributes:
  - name: "id"
    type: "integer"
    description: "The unique identifier for this Import API access token."
    value: |
      828792559

  - name: "access_token"
    type: "string"
    description: "An Import API access token. This token is valid only for the Import API source it is created for."
    value: |
      <IMPORT_API_ACCESS_TOKEN>

examples:
  - code: |
      {
        "id": 828792559,
        "access_token": "<IMPORT_API_ACCESS_TOKEN>"
      }
---