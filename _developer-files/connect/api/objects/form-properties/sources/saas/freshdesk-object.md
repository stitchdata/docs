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
key: "source-form-properties-freshdesk-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Freshdesk Source Form Property"
api-type: "platform.freshdesk"
display-name: "Freshdesk"

source-type: "saas"
docs-name: "freshdesk"


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

object-attributes:
  - name: "api_key"
    type: "string"
    required: true
    description: |
      The API key for the {{ form-property.display-name }} account Stitch should replicate data from. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link }}#retrieve-api-credentials) for instructions on retrieving this credential.
    value: "<API_KEY>"

  - name: "domain"
    type: "string"
    required: true
    description: |
      The subdomain prefix of the {{ form-property.display-name }} account Stitch should replicate data from. For example: If the URL were `stitch.{{ {{ form-property.docs-name }} }}.com`, this value would be `stitch`.
    value: "<SUBDOMAIN_PREFIX>"
---