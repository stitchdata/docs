---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/connect-templates/destination-form-property/
## FOR INSTRUCTIONS & REFERENCE INFO


# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-form"
form-type: "source"
key: "source-form-properties-shopify-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Shopify Source Form Property"
api-type: "platform.shopify"
display-name: "Shopify"

source-type: "saas"
docs-name: "shopify"

description: ""


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

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