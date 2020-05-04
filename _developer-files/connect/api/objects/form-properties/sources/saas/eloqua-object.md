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
key: "source-form-properties-eloqua-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Eloqua Source Form Property"
api-type: "platform.eloqua"
display-name: "Eloqua"

source-type: "saas"
docs-name: "eloqua"

property-description: |
  the {{ form-property.display-name }} Bulk and REST APIs

description: ""

# -------------------------- #
#       FORM PROPERTIES      #
# -------------------------- #

uses-start-date: true

object-attributes:
  - name: "bulk_page_size"
    type: "string"
    required: false
    description: |
      The number of records each page in a bulk export should contain. **Note**: This setting only affects streams that use the {{ form-property.display-name }} Bulk API. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#schema" }}) for info about how each stream is replicated.
    value: "5000"


# -------------------------- #
#       OAUTH PROPERTIES     #
# -------------------------- #

oauth-link: "https://docs.oracle.com/en/cloud/saas/marketing/eloqua-rest-api/Authentication_Auth.html"

oauth-description: ""

oauth-properties:
  - name: "client_id"
    type: "string"
    required: true
    credential: false
    description: |
      Your {{ form-property.display-name }} OAuth application's client ID, obtained when you register your app with {{ form-property.display-name }}.
    value: "<YOUR_{{ form-property.display-name | upcase }}_OAUTH_CLIENT_ID>"

  - name: "client_secret"
    type: "string"
    required: true
    credential: true
    description: |
      Your {{ form-property.display-name }} OAuth application's client secret, obtained when you register your app with {{ form-property.display-name }}.
    value: "<YOUR_{{ form-property.display-name | upcase }}_OAUTH_CLIENT_ID>"

  - name: "redirect_uri"
    type: "string"
    required: true
    credential: false
    description: |
      Your {{ form-property.display-name }} OAuth application's registered redirection endpoint. This should be the same URL entered as the **Callback Url** when you registered your app.
    value: "https://your-awesome-company.com/app"

  - name: "refresh_token"
    type: "string"
    required: true
    credential: true
    description: |
      A long-lived token, used to generate new {{ form-property.display-name }} access tokens when old ones expire.
    value: "<REFRESH_TOKEN>"
---