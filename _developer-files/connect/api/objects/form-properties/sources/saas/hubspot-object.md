---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-form"
form-type: "source"
key: "source-form-properties-hubspot-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "HubSpot Source Form Property"
api-type: "platform.hubspot"
display-name: "HubSpot"

source-type: "saas"
docs-name: "hubspot"

description: ""


# -------------------------- #
#       FORM PROPERTIES      #
# -------------------------- #

uses-start-date: true


# -------------------------- #
#       OAUTH PROPERTIES     #
# -------------------------- #

oauth-link: "https://developers.hubspot.com/docs/methods/oauth2/oauth2-overview"

oauth-description: ""

## scopes: content, contacts
## optional scopes: reports, automation, forms, sales-email-read
# https://developers.hubspot.com/docs/methods/oauth2/initiate-oauth-integration#scopes

oauth-properties:
  - name: "client_id"
    type: "string"
    required: true
    credential: true
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
    credential: true
    description: |
      The URL that the user will be redirected to after they authorize your app for the requested scopes.
    value: "https://www.yourcompany.com/auth-callback"

  - name: "refresh_token"
    type: "string"
    required: true
    credential: true
    description: |
      If exchanging a code with {{ form-property.display-name }}, a long-lived token that can be used to retrieve new `access_tokens` when old ones expire.
    value: "<REFRESH_TOKEN>"
---