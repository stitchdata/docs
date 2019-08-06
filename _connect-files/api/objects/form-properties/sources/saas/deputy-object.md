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

content-type: "api-form"
form-type: "source"
key: "source-form-properties-deputy-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Deputy Source Form Property"
api-type: "platform.deputy"
display-name: "Deputy"

source-type: "saas"
docs-name: "deputy"


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

object-attributes:
  - name: "client_id"
    type: "string"
    required: true
    description: |
      A {{ form-property.display-name }} OAuth client ID. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#create-a-oauth-client" }}) for instructions on generating this credential.
    value: "<CLIENT_ID>"

  - name: "client_secret"
    type: "string"
    required: true
    description: |
      A {{ form-property.display-name }} OAuth client secret. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#create-a-oauth-client" }}) for instructions on generating this credential.
    value: "<CLIENT_SECRET>"

  - name: "domain"
    type: "string"
    required: true
    description: |
      A {{ form-property.display-name }} subdomain, used to sign into {{ form-property.display-name }}.

      For example: If the URL to sign into {{ form-property.display-name }} is `https://stitchdata.deputy.com`, this value would be `stitchdata.deputy.com`.
    value: "<SUBDOMAIN>.deputy.com"

  - name: "redirect_uri"
    type: "string"
    required: true
    description: |
      A {{ form-property.display-name }} OAuth redirect URI.

      You can enter anything for this value, such as `https://localhost`. Based on [{{ form-property.display-name }}'s documentation](https://www.deputy.com/api-doc/API/Authentication){:target="new"}, this value is required but not used.
    value: "https://localhost"

  - name: "refresh_token"
    type: "string"
    required: true
    description: |
      A {{ form-property.display-name }} OAuth refresh token. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#create-a-oauth-client" }}) for instructions on generating this credential.
    value: "<REFRESH_TOKEN>"
---