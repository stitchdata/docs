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
key: "source-form-properties-outbrain-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Outbrain Source Form Property"
api-type: "platform.outbrain"
display-name: "Outbrain"

source-type: "saas"
docs-name: "outbrain"

# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

object-attributes:
  - name: "account_id"
    type: "string"
    required: true
    description: |
      Your {{ form-property.display-name }} account (or marketer) ID.

      You can find this info by looking at the URL when you’re logged into your {{ form-property.display-name }} account. The Account ID looks something like this: `0f4b02153ee75f3c9dc4fc128ab041962` and is located between `marketers` and `campaigns`, if you’re looking at the Overview dashboard:

      `https://my.outbrain.com/amplify/site/marketers/[account-id-will-be-here]/campaigns/overview`
    value: "0f4b02153ee75f3c9dc4fc128ab041962"

  - name: "password"
    type: "string"
    required: true
    description: |
      Your {{ form-property.display-name }} password.
    value: "<PASSWORD>"

  - name: "username"
    type: "string"
    required: true
    description: |
      Your {{ form-property.display-name }} username.
    value: "<USERNAME>"
---