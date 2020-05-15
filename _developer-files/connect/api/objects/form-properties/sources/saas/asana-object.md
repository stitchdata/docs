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
key: "source-form-properties-asana-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Asana Source Form Property"
api-type: "platform.asana"
display-name: "Asana"

source-type: "saas"
docs-name: "asana"

description: ""

# -------------------------- #
#       FORM PROPERTIES      #
# -------------------------- #

uses-start-date: true


# -------------------------- #
#       OAUTH PROPERTIES     #
# -------------------------- #

oauth-link: "https://developers.asana.com/docs/authentication-basics"

oauth-description: |
  TODO

oauth-attributes:
  - name: "access_token"
    type: "string"
    required: true
    credential: true
    description: |
      The {{ form-property.display-name }} token to use in future requests to the {{ form-property.display-name }} API, created after a successful OAuth handshake.
    value: "<ACCESS_TOKEN>"

  - name: "client_id"
    type: "string"
    required: true
    credential: false
    description: |
      Your {{ form-property.display-name }} OAuth application client ID.
    value: "<YOUR_OAUTH_CLIENT_ID>"

  - name: "client_secret"
    type: "string"
    required: true
    credential: true
    description: |
      Your {{ form-property.display-name }} OAuth application client secret.
    value: "<YOUR_OAUTH_CLIENT_SECRET>"

  - name: "redirect_uri"
    type: "string"
    required: true
    credential: false
    description: |
      Your {{ form-property.display-name }} OAuth application redirect URL. This is provided to {{ form-property.display-name }} when you register your OAuth application.
    value: "<YOUR_OAUTH_REDIRECT_URI>"

  - name: "refresh_token"
    type: "string"
    required: true
    credential: true
    description: |
      If exchanging a code with {{ form-property.display-name }}, a long-lived token that can be used to retrieve new `access_tokens` when old ones expire.
    value: "<REFRESH_TOKEN>"
---