---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-form"
form-type: "source"
key: "source-form-properties-campaign-monitor-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Campaign Monitor Source Form Property"
api-type: "platform.campaign-monitor"
display-name: "Campaign Monitor"

source-type: "saas"
docs-name: "campaign-monitor"

description: ""


# -------------------------- #
#       FORM PROPERTIES      #
# -------------------------- #

uses-start-date: true

object-attributes:
  - name: "client_id"
    type: "string"
    required: true
    description: |
      The user's {{ form-property.display-name }} API client ID. This can be found in the {{ form-property.display-name }} app in **Account Settings > API keys**.
    value: "<CAMPAIGN_MONITOR_CLIENT_ID>"


# -------------------------- #
#       OAUTH PROPERTIES     #
# -------------------------- #

oauth-link: "https://www.campaignmonitor.com/api/getting-started/#authenticating-with-oauth"

oauth-description: ""

oauth-attributes:
  - name: "access_token"
    type: "string"
    required: true
    credential: true
    description: |
      An {{ form-property.display-name }} OAuth token.
    value: "<{{ form-property.display-name | upcase }}_ACCESS_TOKEN>"

  - name: "refresh_token"
    type: "string"
    required: true
    credential: true
    description: |
      A long-lived {{ form-property.display-name }} token which can be used to obtain a new {{ form-property.display-name }} `access_token`.
    value: "<{{ form-property.display-name | upcase }}_REFRESH_TOKEN>"
---