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
key: "source-form-properties-typeform-object"

# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Typeform Source Form Property"
api-type: "platform.typeform"
display-name: "Typeform"

source-type: "saas"
docs-name: "typeform"

description: ""


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

object-attributes:
  - name: "forms"
    type: "string"
    required: true
    description: |
      The {{ form-property.display-name }} form ID(s) Stitch should replicate. If replicating multiple forms, enter the IDs as a comma-separated list. For example: `"<FORM_ID_1>, <FORM_ID_2>"`
       Refer to our [{{ form-property.display-name }} documentation]({{ doc-link | append:"#retrieve-typeform-form-ids" }}) for instructions on retrieving form IDs.
    value: "<FORM_ID_1>, <FORM_ID_2>"

  - name: "incremental_range"
    type: "string"
    required: true
    description: |
      The type of data aggregation Stitch should use when replicating {{ form-property.display-name }} data. Accepted values are:
       - `daily`
      - `hourly`
    value: "daily"

  - name: "token"
    type: "string"
    required: true
    description: |
      Your {{ form-property.display-name }} API token. Refer to our [{{ form-property.display-name }} documentation]({{ doc-link | append: "#generate-typeform-api-token" }}) for instructions on generating the token.
    value: "<{{ form-property.display-name | upcase }}_API_TOKEN>"
---