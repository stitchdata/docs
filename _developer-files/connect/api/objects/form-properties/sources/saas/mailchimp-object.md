---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-form"
form-type: "source"
key: "source-form-properties-mailchimp-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "MailChimp Source Form Property"
api-type: "platform.mailchimp"
display-name: "MailChimp"

source-type: "saas"
docs-name: "mailchimp"

description: ""


# -------------------------- #
#       FORM PROPERTIES      #
# -------------------------- #

uses-start-date: true

object-attributes:
  - name: "page_size"
    type: "string"
    required: false
    description: |
      An optional parameter used to reduce the amount of data requested in a single API request. Refer to the [{{ form-property.display-name }} repository](https://github.com/singer-io/tap-mailchimp/pull/12){:target="new"} for more info.
    value: "250"


# -------------------------- #
#       OAUTH PROPERTIES     #
# -------------------------- #

oauth-link: "https://mailchimp.com/developer/guides/how-to-use-oauth2/"

oauth-description: ""

oauth-properties:
  - name: "access_token"
    type: "string"
    required: true
    credential: true
    description: |
      The {{ form-property.display-name }} token to use in future requests to the {{ form-property.display-name }} API, created after a successful OAuth handshake.
    value: "<ACCESS_TOKEN>"

  - name: "client_id"
    type: "string"
    required: true
    credential: false
    description: |
      Your {{ form-property.display-name }} OAuth application's client ID.
    value: "<YOUR_OAUTH_CLIENT_ID>"

  - name: "client_secret"
    type: "string"
    required: true
    credential: true
    description: |
      Your {{ form-property.display-name }} OAuth application's client secret.
    value: "<YOUR_OAUTH_CLIENT_SECRET>"
---