---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/connect-templates/destination-form-property/
## FOR INSTRUCTIONS & REFERENCE INFO


type: "connect"
content-type: "api-form"
form-type: "source"
key: "source-form-properties-shopify-object"

title: "Shopify Source Form Property"
api-type: "shopify"
display-name: "Shopify"

source-type: "saas"
docs-name: "shopify"

description: ""

object-attributes:
  # - name: "date_window_size"
  #   type: "string"
  #   required: false
  #   description: ""
  #   value: ""

  - name: "shop"
    type: "string"
    required: true
    description: |
      The name of the {{ form-property.display-name }} shop.

      For example: If the shop URL was `stitch-data.shopify.com`, this value would be `stitch-data`.
    value: "stitch-data"
---