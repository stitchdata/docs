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

# uses-common-fields: true/false
# See these fields in _data/connect/common/all-sources.yml
# May also include applicable fields in _data/connect/common/all-sources.yml

object-attributes:
  - name: "api_key"
    type: "string"
    required: true
    description: "The user's {{ form-property.display-name }} API key. The user can obtain this by contacting their {{ form-property.display-name }} sales representative or account manager."
    value: "<API_KEY>"

  - name: "api_secret"
    type: "string"
    required: true
    description: "The user's {{ form-property.display-name }} API secret. The user can obtain this by contacting their {{ form-property.display-name }} sales representative or account manager."
    value: "<API_SECRET>"

  - name: "username"
    type: "string"
    required: true
    description: "The user's {{ form-property.display-name }} username."
    value: "<USERNAME>"
---