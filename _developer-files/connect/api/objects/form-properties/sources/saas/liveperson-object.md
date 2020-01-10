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
key: "source-form-properties-liveperson-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "LivePerson Source Form Property"
api-type: "platform.liveperson"
display-name: "LivePerson"

source-type: "saas"
docs-name: "liveperson"

property-description: |
  the [{{ form-property.display-name }} Data Access API](https://developers.liveperson.com/data-access-api-overview.html){:target="new"}


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

object-attributes:
  - name: "access_token"
    type: "string"
    required: true
    description: |
      Your {{ form-property.display-name }} API access token. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link }}) for instructions on creating this credential.
    value: "<{{ form-property.display-name | upcase }}_ACCESS_TOKEN>"

  - name: "access_token_secret"
    type: "string"
    required: true
    description: |
      Your {{ form-property.display-name }} API access token secret. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link }}) for instructions on creating this credential.
    value: "<{{ form-property.display-name | upcase }}_ACCESS_TOKEN_SECRET>"

  - name: "account_id"
    type: "string"
    required: true
    description: |
      Your {{ form-property.display-name }} account ID.
    value: "<{{ form-property.display-name | upcase }}_ACCOUNT_ID>"

  - name: "app_key"
    type: "string"
    required: true
    description: |
      Your {{ form-property.display-name }} API app key. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link }}) for instructions on creating this credential.
    value: "<{{ form-property.display-name | upcase }}_APP_KEY>"

  - name: "app_secret"
    type: "string"
    required: true
    description: |
      Your {{ form-property.display-name }} API app secret. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link }}) for instructions on creating this credential.
    value: "<{{ form-property.display-name | upcase }}_APP_SECRET>"
---