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
key: "source-form-properties-braintree-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Braintree Source Form Property"
api-type: "platform.braintree"
display-name: "Braintree"

source-type: "saas"
docs-name: "braintree"


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

object-attributes:
  - name: "merchant_id"
    type: "string"
    required: true
    description: |
      The {{ form-property.display-name }} account's merchant ID. **Note**: Stitch's {{ form-property.display-name }} integration replicates data from the default merchant account under this merchant ID. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#retrieve-api-credentials" }}) for instructions on retrieving this info.
    value: "<MERCHANT_ID>"

  - name: "private_key"
    type: "string"
    required: true
    description: |
      The {{ form-property.display-name }} account's private key. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#retrieve-api-credentials" }}) for instructions on retrieving this info.
    value: "<PRIVATE_KEY>"

  - name: "public_key"
    type: "string"
    required: true
    description: |
      The {{ form-property.display-name }} account's public key. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#retrieve-api-credentials" }}) for instructions on retrieving this info.
    value: "<PUBLIC_KEY>"
---