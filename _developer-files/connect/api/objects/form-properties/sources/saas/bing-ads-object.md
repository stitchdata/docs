---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-form"
form-type: "source"
key: "source-form-properties-bing-ads-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Microsoft Advertising (Bing Ads) Source Form Property"
api-type: "platform.bing-ads"
display-name: "Microsoft Advertising (Bing Ads)"

source-type: "saas"
docs-name: "bing-ads"

description: ""


# -------------------------- #
#       FORM PROPERTIES      #
# -------------------------- #

uses-start-date: true


# -------------------------- #
#       OAUTH PROPERTIES     #
# -------------------------- #

oauth-link: "https://docs.microsoft.com/en-us/advertising/guides/authentication-oauth-live-connect?view=bingads-133"

oauth-description: ""

oauth-properties:
  - name: "account_ids"
    type: "string"
    required: true
    credential: false
    description: |
      The ID of the account that owns the entities in API requests. Refer to [Microsoft's documentation](https://docs.microsoft.com/en-us/advertising/guides/get-started?view=bingads-13#get-ids){:target="new"} for more info about this identifer.
    value: "<ACCOUNT_ID>"

  - name: "customer_id"
    type: "string"
    required: true
    credential: false
    description: |
      The ID of the customer that contains and owns the {{ form-property.display-name }} account being accessed. Refer to [Microsoft's documentation](https://docs.microsoft.com/en-us/advertising/guides/get-started?view=bingads-13#get-ids){:target="new"} for more info about this identifer.
    value: "<CUSTOMER_ID>"

  - name: "developer_token"
    type: "string"
    required: true
    credential: true
    description: |
      Your {{ form-property.display-name }} developer token, used to access the {{ form-property.display-name }} API. Refer to [Microsoft's documentation](https://docs.microsoft.com/en-us/advertising/guides/get-started?view=bingads-13#get-developer-token){:target="new"} for instructions on obtaining this credential.
    value: |
      <YOUR_{{ form-property.display-name | upcase | replace: " ","_" }}_DEVELOPER_TOKEN>

  - name: "oauth_client_id"
    type: "string"
    required: true
    credential: true
    description: |
      The application (client) ID that the **Azure portal - App registrations portal** assigned your OAuth application. Refer to [Microsoft's documentation](https://docs.microsoft.com/en-us/advertising/guides/authentication-oauth-live-connect?view=bingads-13#registerapplication){:target="new"} for more info.
    value: |
      <YOUR_{{ form-property.display-name | upcase | replace: " ","_" }}_OAUTH_CLIENT_ID>

  - name: "oauth_client_secret"
    type: "string"
    required: true
    credential: true
    description: |
      Your {{ form-property.display-name }} OAuth application's client secret.
    value: |
      <YOUR_{{ form-property.display-name | upcase | replace: " ","_" }}_OAUTH_CLIENT_SECRET>

  - name: "refresh_token"
    type: "string"
    required: true
    credential: true
    description: |
      A long-lived token that can be used to retrieve new {{ form-property.display-name }} `access_tokens` when old ones expire.
    value: "<REFRESH_TOKEN>"

  - name: "user_id"
    type: "string"
    required: false
    credential: false
    description: |
      TODO: What is this? Is this equal to `UserName` here: https://docs.microsoft.com/en-us/advertising/guides/get-started?view=bingads-13#request-headers
    value: ""
---