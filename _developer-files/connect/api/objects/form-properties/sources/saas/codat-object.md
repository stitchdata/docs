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
key: "source-form-properties-codat-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Codat Source Form Property"
api-type: "platform.codat"
display-name: "Codat"

source-type: "saas"
docs-name: "codat" 


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

object-attributes:
  - name: "api_key"
    type: "string"
    required: true
    description: |
      The API key for the {{ form-property.display-name }} account Stitch should replicate data from. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#retrieve-codat-api-key" }}) for instructions for retrieving this credential.
    value: "<API_KEY>"

  - name: "uat_urls"
    type: "string"
    required: true
    description: |
      Indicates if the source is a UAT (sandbox) environment in {{ form-property.display-name }}. Accepted values are `true` and `false`.

      **Note**: This property should be `true` only if the source is a UAT (sandbox) environment. Setting this as `true` when the instance isn't a sandbox will prevent a successful connection in Stitch.
    value: "false"
---