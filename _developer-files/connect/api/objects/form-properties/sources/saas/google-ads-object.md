---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-form"
form-type: "source"
key: "source-form-properties-google-ads-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Google Ads Source Form Property"
api-type: "platform.adwords"
display-name: "Google Ads"

source-type: "saas"
docs-name: "google-ads"

description: ""


# -------------------------- #
#       FORM PROPERTIES      #
# -------------------------- #

uses-start-date: true


# -------------------------- #
#       OAUTH PROPERTIES     #
# -------------------------- #

oauth-link: "https://developers.google.com/adwords/api/docs/guides/authentication"

oauth-description: ""

oauth-attributes:
  - name: "customer_ids"
    type: "string"
    required: true
    credential: false
    description: |
      A comma-separated list of {{ form-property.display-name }} account IDs to replicate data from.
    value: "1234567890,0987654321"

  - name: "developer_token"
    type: "string"
    required: true
    credential: true
    description: |
      Your {{ form-property.display-name }} developer token, which identifies your app to the AdWords API. Refer to [Google's documentation](https://developers.google.com/adwords/api/docs/guides/first-api-call#request_a_developer_token){:target="new"} for more info.
    value: "<YOUR_DEVELOPER_TOKEN>"

  - name: "oauth_client_id"
    type: "string"
    required: true
    credential: true
    description: |
      Your {{ form-property.display-name }} OAuth application's client ID, obtained when you create an OAuth app with Google. Refer to [Google's documentation](https://developers.google.com/adwords/api/docs/guides/authentication#create_a_client_id_and_client_secret){:target="new"} for more info.
    value: "<YOUR_OAUTH_CLIENT_ID>"

  - name: "oauth_client_secret"
    type: "string"
    required: true
    credential: true
    description: |
      Your {{ form-property.display-name }} OAuth application's client secret, obtained when you create an OAuth app with Google. Refer to [Google's documentation](https://developers.google.com/adwords/api/docs/guides/authentication#create_a_client_id_and_client_secret){:target="new"} for more info.
    value: "<YOUR_OAUTH_CLIENT_SECRET>"

  - name: "refresh_token"
    type: "string"
    required: true
    credential: true
    description: |
      A long-lived token, used to generate new {{ form-property.display-name }} access tokens when old ones expire.
    value: "<REFRESH_TOKEN>"

  - name: "user_id"
    type: "string"
    required: true
    credential: false
    description: |
      TODO
    value: "<USER_ID>"
---