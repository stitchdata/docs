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
key: "source-form-properties-revinate-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Revinate Source Form Property"
api-type: "revinate"
display-name: "Revinate"

source-type: "saas"
docs-name: "revinate"

description: ""


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

object-attributes:
  - name: "api_key"
    type: "string"
    required: true
    description: "Your {{ form-property.display-name }} API key. You can obtain this by contacting your {{ form-property.display-name }} sales representative or account manager."
    value: "<API_KEY>"

  - name: "api_secret"
    type: "string"
    required: true
    description: "Your {{ form-property.display-name }} API secret. The user can obtain this by contacting their {{ form-property.display-name }} sales representative or account manager."
    value: "<API_SECRET>"

  - name: "username"
    type: "string"
    required: true
    description: "Your {{ form-property.display-name }} username."
    value: "<USERNAME>"
---