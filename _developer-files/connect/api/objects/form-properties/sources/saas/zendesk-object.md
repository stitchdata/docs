---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-form"
form-type: "source"
key: "source-form-properties-zendesk-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Zendesk Source Form Property"
api-type: "platform.zendesk"
display-name: "Zendesk"

source-type: "saas"
docs-name: "zendesk"

description: ""


# -------------------------- #
#       FORM PROPERTIES      #
# -------------------------- #

uses-start-date: true

object-attributes:
  - name: "subdomain"
    type: "string"
    required: true
    description: |
      The prefix of the {{ form-property.display-name }} subdomain Stitch should replicate data from.

      For example: If the address is `stitchdata.{{ form-property.display-name | downcase }}.com`, only `stitchdata` would be entered as the value.
    value: "<YOUR_{{ form-property.display-name | upcase }}_SUBDOMAIN>"


# -------------------------- #
#       OAUTH PROPERTIES     #
# -------------------------- #

oauth-link: "https://support.zendesk.com/hc/en-us/articles/203663836"

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

  - name: "oauth_token"
    type: "string"
    required: true
    credential: true
    description: |
      TODO: It might be this? https://develop.zendesk.com/hc/en-us/articles/360001074348
    value: ""

  - name: "marketplace_app_id"
    type: "string"
    required: true
    credential: false
    description: |
    value: ""

  - name: "marketplace_name"
    type: "string"
    required: true
    credential: false
    description: |
    value: ""

  - name: "marketplace_organization_id"
    type: "string"
    required: true
    credential: false
    description: |
    value: ""
---