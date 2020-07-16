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
key: "source-form-properties-trello-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Trello Source Form Property"
api-type: "platform.trello"
display-name: "Trello"

source-type: "saas"
docs-name: "trello" # This should be whatever integration.name is. Ex: LinkedIn Ads is linkedin-ads

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

oauth-link: "https://developer.atlassian.com/cloud/trello/guides/rest-api/authorization/#using-basic-oauth"

oauth-description: ""

oauth-attributes:
  - name: "access_token"
    type: "string"
    required: true
    credential: true
    description: ""
    value: "<ACCESS_TOKEN>"

  - name: "access_token_secret"
    type: "string"
    required: true
    credential: true
    description: ""
    value: "<ACCESS_TOKEN_SECRET>"

  - name: "consumer_key"
    type: "string"
    required: true
    credential: true
    description: ""
    value: "<CONSUMER_KEY>"

  - name: "consumer_secret"
    type: "string"
    required: true
    credential: true
    description: ""
    value: "<CONSUMER_SECRET>"
---