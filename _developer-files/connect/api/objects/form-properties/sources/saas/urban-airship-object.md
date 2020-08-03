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
key: "source-form-properties-urban-airship-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Urban Airship Source Form Property"
api-type: "platform.urban-airship"
display-name: "Urban Airship"

source-type: "saas"
docs-name: "urban-airship"


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

object-attributes:
  - name: "app_key"
    type: "string"
    required: true
    description: |
      Your {{ form-property.display-name }} app key. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#retrieve-app-creds" }}) for instructions on retrieving this credential.
    value: "<APP_KEY>"

  - name: "app_secret"
    type: "string"
    required: true
    description: |
      Your {{ form-property.display-name }} app secret. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#retrieve-app-creds" }}) for instructions on retrieving this credential.
    value: "<APP_SECRET>"
---