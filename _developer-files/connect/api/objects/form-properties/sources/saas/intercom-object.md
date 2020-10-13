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

content-type: "api-form"
form-type: "source"
key: "source-form-properties-intercom-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Intercom Source Form Property"
api-type: "platform.intercom"
display-name: "Intercom"

source-type: "saas"
docs-name: "intercom" 

# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

# Only source-specific attributes need to be listed here.
# The following attributes are considered common,
# and therefore don't need to be listed:
# anchor_time, cron_expression, frequency_in_minutes, image_version, start_date 


# -------------------------- #
#       OAUTH PROPERTIES     #
# -------------------------- #

oauth-link: "https://developers.intercom.com/building-apps/docs/setting-up-oauth"

oauth-description: ""

oauth-attributes:
  - name: "access_token"
    type: "string"
    required: true
    credential: true
    description: |
      The token used to access your {{ form-property.display-name }} workspace's data via API.
    value: "<YOUR_API_ACCESS_TOKEN>"   
---