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
key: "source-form-properties-ilevel-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "iLEVEL Source Form Property"
api-type: "platform.ilevel"
display-name: "iLEVEL"

source-type: "saas"
docs-name: "ilevel"

description: |
  Connecting a {{ form-property.display-name }} data source requires {{ form-property.display-name }} Web Services access. Contact {{ form-property.display-name }} support to request this feature.


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

object-attributes:
  - name: "username"
    type: "string"
    required: true
    description: |
      An {{ form-property.display-name }} API user's username.
    value: "<{{ form-property.display-name | upcase }}_USERNAME>"

  - name: "password"
    type: "string"
    required: true
    description: |
      The {{ form-property.display-name }} API user's password.
    value: "<PASSWORD>"

  - name: "is_sandbox"
    type: "string"
    required: false
    description: |
      If `true`, the {{ form-property.display-name }} instance you're connecting is a sandbox. 
    value: "false"
---