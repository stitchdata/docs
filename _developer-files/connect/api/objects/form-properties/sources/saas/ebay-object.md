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
key: "source-form-properties-ebay-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "eBay Source Form Property"
api-type: "platform.ebay"
display-name: "eBay"

source-type: "saas"
docs-name: "ebay" # This should be whatever integration.name is. Ex: LinkedIn Ads is linkedin-ads


# -------------------------- #
#       OAUTH PROPERTIES     #
# -------------------------- #

oauth-link: "https://developer.ebay.com/api-docs/static/oauth-trad-apis.html"

oauth-description: ""

oauth-attributes:
  - name: "client_id"
    type: "string"
    required: true
    credential: true
    description: |
      This is your App ID in your {{ form-property.display-name }} seller account.
    value: "<CLIENT_ID>"

  - name: "client_secret"
    type: "string"
    required: true
    credential: true
    description: |
      This is your Cert ID in your {{ form-property.display-name }} seller account.
    value: "<CLIENT_SECRET>"

  - name: "refresh_token"
    type: "string"
    required: true
    credential: true
    description: |
      A long-lived token, used to generate new {{ form-property.display-name }} access tokens when old ones expire.
    value: "<REFRESH_TOKEN>"

  - name: "scope"
    type: "string"
    required: true
    credential: true
    description: |
      This allows Stitch to have certain access privileges to your {{ form-property.display-name }} sales data.
    value: "<SCOPE>"
---     
---