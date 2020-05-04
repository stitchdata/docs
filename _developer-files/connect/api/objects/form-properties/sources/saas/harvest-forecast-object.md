---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-form"
form-type: "source"
key: "source-form-properties-harvest-forecast-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Harvest Forecast Source Form Property"
api-type: "platform.harvest-forecast"
display-name: "Harvest Forecast"

source-type: "saas"
docs-name: "harvest-forecast"

description: ""


# -------------------------- #
#       FORM PROPERTIES      #
# -------------------------- #

uses-start-date: true

# -------------------------- #
#       OAUTH PROPERTIES     #
# -------------------------- #

oauth-link: "https://help.getharvest.com/api-v2/authentication-api/authentication/authentication/#oauth2-authorization-flow"

oauth-description: ""

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

  - name: "refresh_token"
    type: "string"
    required: true
    credential: true
    description: |
      If exchanging a code with {{ form-property.display-name }}, a long-lived token that can be used to retrieve new `access_tokens` when old ones expire.
    value: "<REFRESH_TOKEN>"
---