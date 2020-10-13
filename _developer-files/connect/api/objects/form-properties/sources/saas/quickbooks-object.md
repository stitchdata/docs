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
key: "source-form-properties-quickbooks-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Quickbooks Source Form Property"
api-type: "platform.quickbooks"
display-name: "Quickbooks"

source-type: "saas"
docs-name: "quickbooks" # This should be whatever integration.name is. Ex: LinkedIn Ads is linkedin-ads

# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

# Only source-specific attributes need to be listed here.
# The following attributes are considered common,
# and therefore don't need to be listed:
# anchor_time, cron_expression, frequency_in_minutes, image_version, start_date 

object-attributes:
  - name: "sandbox"
    type: "string"
    required: false
    description: "Whether to replicate data from your {{ form-property.display-name }} sandbox or prod account for this integration. If `false`, Stitch will connect to your prouction account. The default value is false."
    value: "`true` or `false`"

  - name: "max_results"
    type: "string"
    required: false
    description: "The maximum amount of rows of data you want replicated from your {{ form-property.display-name }} account. If the amount is not specified, the default amount of rows replicated will be 100. The maximum amount of rows of data you can replicate at a time is 1000."
    value: "`true` or `false`"  


# -------------------------- #
#       OAUTH PROPERTIES     #
# -------------------------- #

oauth-link: "https://developer.intuit.com/app/developer/qbo/docs/develop/authentication-and-authorization"

oauth-description: ""

oauth-attributes:
  - name: "client_id"
    type: "string"
    required: true
    credential: true
    description: |
      Your {{ form-property.display-name }} OAuth application's client ID, obtained when you create an OAuth app.
    value: "<YOUR_OAUTH_CLIENT_ID>"

  - name: "client_secret"
    type: "string"
    required: true
    credential: true
    description: |
      Your {{ form-property.display-name }} OAuth application's client secret, obtained when you create an OAuth app.
    value: "<YOUR_OAUTH_CLIENT_SECRET>"

  - name: "refresh_token"
    type: "string"
    required: true
    credential: true
    description: |
      A long-lived token, used to generate new {{ form-property.display-name }} access tokens when old ones expire.
    value: "<REFRESH_TOKEN>"

  - name: "realm_id"
    type: "string"
    required: true
    credential: true
    description: |
      Your company ID in your {{ form-property.display-name }} account.
    value: "<REALM_ID>"
---