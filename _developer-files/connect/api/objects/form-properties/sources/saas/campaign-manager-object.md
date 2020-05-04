---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-form"
form-type: "source"
key: "source-form-properties-campaign-manager-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Campaign Manager Source Form Property"
api-type: "platform.doubleclick-campaign-manager"
display-name: "Campaign Manager"

source-type: "saas"
docs-name: "campaign-manager"

description: ""


# -------------------------- #
#       FORM PROPERTIES      #
# -------------------------- #

uses-start-date: false

object-attributes:
  - name: "profile_id"
    type: "string"
    required: true
    description: |
      The ID of the {{ form-property.display-name }} profile you want to replicate data from. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | prepend: site.baseurl | append: "#locate-your-profile-id" }}) for instructions on retrieving this info.
    value: "<CAMPAIGN_MANAGER_PROFILE_ID>"


# -------------------------- #
#       OAUTH PROPERTIES     #
# -------------------------- #

oauth-link: "https://developers.google.com/doubleclick-advertisers/authorizing"

oauth-description: ""

oauth-properties:
  - name: "client_id"
    type: "string"
    required: true
    credential: true
    description: |
      Your {{ form-property.display-name }} OAuth application's client ID. Refer to [Google's documentation]({{ form-property.oauth-link }}){:target="new"} for more info.
    value: "<YOUR_OAUTH_CLIENT_ID>"

  - name: "client_secret"
    type: "string"
    required: true
    credential: true
    description: |
      Your {{ form-property.display-name }} OAuth application's client secret. Refer to [Google's documentation]({{ form-property.oauth-link }}){:target="new"} for more info.
    value: "<YOUR_OAUTH_CLIENT_SECRET>"

  - name: "refresh_token"
    type: "string"
    required: true
    credential: true
    description: |
      A long-lived token, used to generate new access tokens when needed. Refer to [Google's documentation](https://developers.google.com/identity/protocols/oauth2#5.-refresh-the-access-token,-if-necessary.){:target="new"} for more info.
    value: "<REFRESH_TOKEN>"
---