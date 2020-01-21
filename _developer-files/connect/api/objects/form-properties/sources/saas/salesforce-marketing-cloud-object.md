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
key: "source-form-properties-exacttarget-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Salesforce Marketing Cloud Source Form Property"
api-type: "platform.exacttarget"
display-name: "Salesforce Marketing Cloud"

source-type: "saas"
docs-name: "salesforce-marketing-cloud"


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

object-attributes:
  - name: "client_id"
    type: "string"
    required: true
    description: |
      A {{ form-property.display-name }} client ID. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#generate-api-credentials" }}) for instructions on generating this credential.
    value: "<CLIENT_ID>"
    
  - name: "client_secret"
    type: "string"
    required: true
    description: |
      A {{ form-property.display-name }} client secret. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#generate-api-credentials" }}) for instructions on generating this credential.
    value: "<CLIENT_SECRET>"
---