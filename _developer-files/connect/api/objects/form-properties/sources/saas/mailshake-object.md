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
key: "source-form-properties-mailshake-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Mailshake Source Form Property"
api-type: "platform.mailshake"
display-name: "Mailshake"

source-type: "saas"
docs-name: "mailshake"


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

object-attributes:
  - name: "api_key"
    type: "string"
    required: true
    description: |
      Your {{ form-property.display-name }} API key. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | prepend: site.baseurl | append: "#retrieve-api-key" }}) for instructions on retrieving this credential. 
    value: "<YOUR_MAILSHAKE_API_KEY>"
---