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
api-type: "platform.google-ads"
display-name: "Google Ads"

source-type: "saas"
docs-name: "google-ads"

description: ""


# -------------------------- #
#       FORM PROPERTIES      #
# -------------------------- #

uses-start-date: true

object-attributes:  
  - name: "conversion_window"
    type: "string"
    required: false
    description: |
      The number of days for the conversion window. The value can be any number between 1 and 30, 60 or 90.  
    value: "30"


# -------------------------- #
#       OAUTH PROPERTIES     #
# -------------------------- #

oauth-link: "https://developers.google.com/google-ads/api/docs/oauth/overview"

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
      Your {{ form-property.display-name }} developer token, which identifies your app to the AdWords API. Refer to [Google's documentation](https://developers.google.com/google-ads/api/docs/first-call/dev-token){:target="new"} for more info.
    value: "<YOUR_DEVELOPER_TOKEN>"

  - name: "oauth_client_id"
    type: "string"
    required: true
    credential: true
    description: |
      Your {{ form-property.display-name }} OAuth application's client ID, obtained when you create an OAuth app with Google. Refer to [Google's documentation](https://developers.google.com/google-ads/api/docs/first-call/oauth-cloud-project#create_a_client_id_and_client_secret){:target="new"} for more info.
    value: "<YOUR_OAUTH_CLIENT_ID>"

  - name: "oauth_client_secret"
    type: "string"
    required: true
    credential: true
    description: |
      Your {{ form-property.display-name }} OAuth application's client secret, obtained when you create an OAuth app with Google. Refer to [Google's documentation](https://developers.google.com/google-ads/api/docs/first-call/oauth-cloud-project#create_a_client_id_and_client_secret){:target="new"} for more info.
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
      The ID of the Google user authorizing the connection.
    value: "<USER_ID>"

  - name: "login_customer_ids"
    type: "array"
    required: true
    credential: false
    description: |
      An array of objects, each containing a pair of customer IDs.
    value: |
      [
           {
              "customerId":"<CUSTOMER_ID>",
              "loginCustomerId":"<MANAGER_ACCOUNT_CUSTOMER_ID>"
           }
         ]
    subattributes:
      - name: "customerId"
        type: "string"
        required: true
        description: "The Ads account's customer ID"

      - name: "loginCustomerId"
        type: "string"
        required: true
        description: "The manager account's customer ID."
---