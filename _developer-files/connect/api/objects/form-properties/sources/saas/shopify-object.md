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
#  CLIENT CREDENTIALS PROPERTIES     #
# -------------------------- #

client-credentials-link: "https://shopify.dev/docs/apps/build/authentication-authorization/access-tokens/client-credentials-grant"

client-credentials-description: "Client Credentials authentication uses a custom app created in your {{ form-property.display-name }} Developer Dashboard."

client-credentials-attributes:
  - name: "client_id"
    type: "string"
    required: true
    credential: true
    description: |
      The Client ID for your {{ form-property.display-name }} custom app.

      You'll find this in your custom app's **API credentials** section in the {{ form-property.display-name }} Developer Dashboard.
    value: "<CLIENT_ID>"

  - name: "client_secret"
    type: "string"
    required: true
    credential: true
    description: |
      The Client Secret for your {{ form-property.display-name }} custom app.

      You'll find this in your custom app's **API credentials** section in the {{ form-property.display-name }} Developer Dashboard. Store this securely—it's only visible once after initial creation.
    value: "<CLIENT_SECRET>"
---