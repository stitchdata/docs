---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/connect-templates/source-form-property/
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
#       FORM PROPERTIES      #
# -------------------------- #

uses-start-date: true

object-attributes:
  # - name: "date_window_size"
  #   type: "string"
  #   required: false
  #   description: ""
  #   value: ""

  # - name: "results_per_page"
  #   type: "string"
  #   required: "false"
  #   description: "The amount of results to load per page."
  #   value: "175"

  - name: "shop"
    type: "string"
    required: true
    description: |
      The name of the {{ form-property.display-name }} shop.

      For example: If the shop URL was `stitch-data.shopify.com`, this value would be `stitch-data`.
    value: "stitch-data"


# -------------------------- #
#       OAUTH PROPERTIES     #
# -------------------------- #

oauth-link: "https://shopify.dev/tutorials/authenticate-with-oauth#the-oauth-flow"

oauth-description: ""

oauth-properties:
  - name: "api_key"
    type: "string"
    required: true
    credential: true
    description: |
      The API key for your {{ form-property.display-name }} shop, generated via an OAuth handshake.
    value: "<API_KEY>"
---