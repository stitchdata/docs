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
key: "source-form-properties-taboola-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Taboola Source Form Property"
api-type: "platform.taboola"
display-name: "Taboola"

source-type: "saas"
docs-name: "taboola"


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

object-attributes:
  - name: "account_id"
    type: "string"
    required: true
    description: |
      Your {{ form-property.display-name }} account ID.
    value: "<ACCOUNT_ID>"

  - name: "client_id"
    type: "string"
    required: true
    description: |
      Your {{ form-property.display-name }} client ID.
    value: "<CLIENT_ID>"

  - name: "client_secret"
    type: "string"
    required: true
    description: |
      Your {{ form-property.display-name }} client secret.
    value: "<CLIENT_SECRET>"

  - name: "password"
    type: "string"
    required: true
    description: "Your {{ form-property.display-name }} password."
    value: "<PASSWORD>"

  - name: "username"
    type: "string"
    required: true
    description: "Your {{ form-property.display-name }} username."
    value: "<USERNAME>"
---