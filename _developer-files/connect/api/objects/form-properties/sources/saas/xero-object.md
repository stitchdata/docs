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

object-attributes:
  - name: "oauth_s3_bucket"
    type: "string"
    read-only: true
    required: true
    description: |
      **This is an internal Stitch field**.
    value: "<STITCH_OAUTH_S3_BUCKET>"

  - name: "oauth_s3_path"
    type: "string"
    read-only: true
    required: true
    description: |
      **This is an internal Stitch field**.
    value: "<STITCH_OAUTH_S3_PATH>"


# -------------------------- #
#       OAUTH PROPERTIES     #
# -------------------------- #

oauth-link: "https://developer.xero.com/documentation/auth-and-limits/partner-applications"

oauth-description: |
  When configuring OAuth for {{ form-property.display-name }} sources, note that:

  - **Only Partner Applications are supported.** Stitch's {{ form-property.display-name }} source is designed to work only with [{{ form-property.display-name }} Partner Applications](https://developer.xero.com/documentation/auth-and-limits/partner-applications){:target="new"}. Private Applications aren't currently supported.
  - **This version of the source uses {{ form-property.display-name }}'s OAuth 1.0a implementation**. Upgrading to OAuth 2.0 is on the roadmap, but there currently isn't a release timeline.

oauth-attributes:
  - name: "consumer_key"
    type: "string"
    required: true
    credential: true
    description: |
      Your OAuth 1.0a application's consumer key, generated when you register your application with {{ form-property.display-name }}.
    value: "<OAUTH_1.0A_CONSUMER_KEY>"

  - name: "consumer_secret"
    type: "string"
    required: true
    credential: true
    description: |
      Your OAuth 1.0a application's consumer secret, generated when you register your application with {{ form-property.display-name }}.
    value: "<OAUTH_1.0A_CONSUMER_SECRET>"

  - name: "oauth_session_handle"
    type: "string"
    required: true
    credential: true
    description: |
      An OAuth 1.0a session handle, used to refresh the `oauth_token`.
    value: "<OAUTH_1.0A_SESSION_HANDLE>"

  - name: "oauth_token"
    type: "string"
    required: true
    credential: true
    description: |
      An OAuth 1.0a access token.
    value: "<OAUTH_1.0A_ACCESS_TOKEN>"

  - name: "oauth_token_secret"
    type: "string"
    required: true
    credential: true
    description: |
      An OAuth 1.0a access token secret.
    value: "<OAUTH_1.0A_ACCESS_TOKEN_SECRET>"

  - name: "organization_name"
    type: "string"
    required: false
    credential: false
    description: |
      The name of the organization allowing access.
    value: "<ORGANIZATION_NAME>"

  - name: "rsa_key"
    type: "string"
    required: true
    credential: true
    description: |
      An RSA Key, generated when you register your application with {{ form-property.display-name }}. Refer to [{{ form-property.display-name }}'s documentation](https://developer.xero.com/documentation/auth-and-limits/create-publicprivate-key){:target="new"} for more info.
    value: "<RSA_KEY>"
---