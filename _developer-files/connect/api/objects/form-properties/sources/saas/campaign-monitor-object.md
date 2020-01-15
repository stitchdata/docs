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
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

object-attributes:
  - name: "client_id"
    type: "string"
    required: true
    description: |
      The user's {{ form-property.display-name }} API client ID. This can be found in the {{ form-property.display-name }} app in **Account Settings > API keys**.
    value: "<CAMPAIGN_MONITOR_CLIENT_ID>"
---