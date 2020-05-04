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
key: "source-form-properties-helpscout-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Help Scout Source Form Property"
api-type: "platform.helpscout"
display-name: "Help Scout"

source-type: "saas"
docs-name: "helpscout"


# -------------------------- #
#       FORM PROPERTIES      #
# -------------------------- #

uses-start-date: true


# -------------------------- #
#       OAUTH PROPERTIES     #
# -------------------------- #

oauth-link: "https://developer.helpscout.com/mailbox-api/overview/authentication/#oauth2-application"

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
      A long-lived token that can be used to retrieve new `access_tokens` when old ones expire.
    value: "<REFRESH_TOKEN>"
---