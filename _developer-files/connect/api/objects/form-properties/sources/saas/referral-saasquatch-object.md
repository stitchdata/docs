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
key: "source-form-properties-referral-saasquatch-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Referral SaaSquatch Source Form Property"
api-type: "platform.referral-saasquatch"
display-name: "Referral SaaSquatch"

source-type: "saas"
docs-name: "referral-saasquatch"


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

object-attributes:
  - name: "api_key"
    type: "string"
    required: true
    description: |
      Your {{ form-property.display-name }} API key. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#retrieve-api-credentials" }}) for instructions on retrieving this credential.
    value: "<API_KEY>"

  - name: "tenant_alias"
    type: "string"
    required: true
    description: "Your {{ form-property.display-name }} tenant alias."
    value: "<TENANT_ALIAS>"
---