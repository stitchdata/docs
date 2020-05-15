---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-form"
form-type: "source"
key: "source-form-properties-xero-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Xero Source Form Property"
api-type: "platform.xero"
display-name: "Xero"

source-type: "saas"
docs-name: "xero"

description: ""


# -------------------------- #
#       FORM PROPERTIES      #
# -------------------------- #

uses-start-date: true


# TODO: LOOK INTO THESE
# object-attributes:
#   - name: "oauth_s3_bucket"
#     type: "string"
#     read-only: true
#     required: true
#     description: |
#     value: ""

#   - name: "oauth_s3_path"
#     type: "string"
#     read-only: true
#     required: true
#     description: |
#     value: ""


# -------------------------- #
#       OAUTH PROPERTIES     #
# -------------------------- #

oauth-link: ""

oauth-description: ""

# **Note**: Stitch's {{ form-property.display-name }} source is designed to work only with [{{ form-property.display-name }} Partner Applications](https://developer.xero.com/documentation/auth-and-limits/partner-applications){:target="new"}. Private Applications aren't currently supported.

oauth-attributes:
  - name: "consumer_key"
    type: "string"
    required: true
    credential: true
    description: |
    value: ""

  - name: "consumer_secret"
    type: "string"
    required: true
    credential: true
    description: |
    value: ""

  - name: "oauth_session_handle"
    type: "string"
    required: true
    credential: true
    description: |
    value: ""

  - name: "oauth_token"
    type: "string"
    required: true
    credential: true
    description: |
    value: ""

  - name: "oauth_token_secret"
    type: "string"
    required: true
    credential: true
    description: |
    value: ""

  - name: "organization_name"
    type: "string"
    required: false
    credential: false
    description: |
    value: ""

  - name: "rsa_key"
    type: "string"
    required: true
    credential: true
    description: |
      https://developer.xero.com/documentation/api-guides/create-publicprivate-key
    value: ""
---