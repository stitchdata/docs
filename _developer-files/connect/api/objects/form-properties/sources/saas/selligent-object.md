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
key: "source-form-properties-selligent-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Selligent Source Form Property"
api-type: "platform.selligent"
display-name: "Selligent"

source-type: "saas"
docs-name: "selligent" # This should be whatever integration.name is. Ex: LinkedIn Ads is linkedin-ads

property-description: ""
## Used to create a description for the object that doesn't adhere to the standard in _developers/connect/api/documentation/api-form-properties.html
## See the Heap object for an example


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

object-attributes:
  - name: "organization"
    type: "string"
    required: true
    description: "The name of your organization in {{ form-property.display-name }}."
    value: "Organization"

  - name: "base_url"
    type: "string"
    required: true
    description: "The base URL for your {{ form-property.display-name }} installation."
    value: "https://organization.yourhost.com:443"
    
  - name: "api_key"
    type: "string"
    required: true
    description: "Your {{ form-property.display-name }} API key. Contact your {{ form-property.display-name }} account manager for assistance in generating your API key."
    value: "<API_KEY>"    
---