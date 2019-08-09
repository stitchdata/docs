---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

content-type: "api-form"
form-type: "source"
key: "source-form-properties-bigcommerce-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "BigCommerce Source Form Property"
api-type: "platform.bigcommerce"
display-name: "BigCommerce"

source-type: "saas"
docs-name: "bigcommerce"

description: ""


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

object-attributes:
  - name: "access_token"
    type: "string"
    required: true
    description: |
      The user's {{ form-property.display-name }} API access token. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link }}) for instructions on retrieving this credential.
    value: "<API_ACCESS_TOKEN>"

  - name: "client_id"
    required: true
    type: "string"
    description: |
      The user's {{ form-property.display-name }} API client ID. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link }}) for instructions on retrieving this credential.
    value: "<API_CLIENT_ID>"

  - name: "store_hash"
    type: "string"
    required: true
    description: |
      The user's {{ form-property.display-name }} store hash. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link }}) for instructions on retrieving this credential.
    value: "<STORE_HASH>"
---