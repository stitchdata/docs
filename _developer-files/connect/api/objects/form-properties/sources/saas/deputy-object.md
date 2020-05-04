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
key: "source-form-properties-deputy-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Deputy Source Form Property"
api-type: "platform.deputy"
display-name: "Deputy"

source-type: "saas"
docs-name: "deputy"


# -------------------------- #
#       FORM PROPERTIES      #
# -------------------------- #

uses-start-date: true

# -------------------------- #
#       OAUTH PROPERTIES     #
# -------------------------- #

oauth-link: "https://www.deputy.com/api-doc/API/Authentication"

oauth-description: ""

oauth-properties:
  - name: "client_id"
    type: "string"
    required: true
    credential: false
    description: |
      Your {{ form-property.display-name }} OAuth application's client ID.
    value: "<YOUR_{{ form-property.display-name | upcase }}_OAUTH_CLIENT_ID>"

  - name: "client_secret"
    type: "string"
    required: true
    credential: true
    description: |
      Your {{ form-property.display-name }} OAuth application's client secret.
    value: "<YOUR_{{ form-property.display-name | upcase }}_OAUTH_CLIENT_SECRET>"

  - name: "domain"
    type: "string"
    required: true
    credential: false
    description: |
      The {{ form-property.display-name }} subdomain of the user authorizing the connection.
    value: "your-deputy-subdomain.na.deputy.com"

  - name: "redirect_uri"
    type: "string"
    required: true
    credential: false
    description: |
      A URL where {{ form-property.display-name }} will forward the user with access credentials for your application.
    value: "https://your-deputy-app.com/app/"

  - name: "refresh_token"
    type: "string"
    required: true
    credential: true
    description: |
      A long-lived token, used to generate new {{ form-property.display-name }} access tokens when old ones expire.
    value: "<REFRESH_TOKEN>"
---