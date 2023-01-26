---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/connect-templates/destination-form-property/
## FOR INSTRUCTIONS & REFERENCE INFO


# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-form"
form-type: "source"
key: "source-form-properties-zendesk-chat-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Zendesk Chat Source Form Property"
api-type: "platform.zendesk-chat"
display-name: "Zendesk Chat"

source-type: "saas"
docs-name: "zendesk-chat" # This should be whatever integration.name is. Ex: LinkedIn Ads is linkedin-ads


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

# Only source-specific attributes need to be listed here.
# The following attributes are considered common,
# and therefore don't need to be listed:
# anchor_time, cron_expression, frequency_in_minutes, image_version, start_date 

object-attributes:    
  - name: "subdomain"
    type: "string"
    required: false
    description: |
      The subdomain of your {{ form-property.display-name }} account URL.
    value: "<YOUR_SUBDOMAIN>"


# -------------------------- #
#       OAUTH PROPERTIES     #
# -------------------------- #

oauth-link: "https://developer.zendesk.com/api-reference/live-chat/introduction/#oauth-access-token"

oauth-description: ""

oauth-attributes:
  - name: "access_token"
    type: "string"
    required: true
    credential: true
    description: |
      The access token of the {{ form-property.display-name }} account being connected to Stitch.
    value: "<ACCESS_TOKEN>"

---