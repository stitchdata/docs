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
key: "source-form-properties-invoiced-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Invoiced Source Form Property"
api-type: "platform.invoiced"
display-name: "Invoiced"

source-type: "saas"
docs-name: "invoiced"

description: ""

# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

object-attributes:
  - name: "api_key"
    type: "string"
    required: true
    description: |
      Your {{ form-property.display-name }} API key. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#generate-api-key" }}) for instructions on generating this credential.
    value: "<{{ form-property.display-name | upcase }}_API_KEY>"

  - name: "sandbox"
    type: "string"
    required: false
    description: "If `true`, the {{ form-property.display-name }} instance is a sandbox."
    value: "false"
---