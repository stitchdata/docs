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
key: "source-form-properties-pardot-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Pardot Source Form Property"
api-type: "platform.pardot"
display-name: "Pardot"

source-type: "saas"
docs-name: "pardot" # This should be whatever integration.name is. Ex: LinkedIn Ads is linkedin-ads


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

# Only source-specific attributes need to be listed here.
# The following attributes are considered common,
# and therefore don't need to be listed:
# anchor_time, cron_expression, frequency_in_minutes, image_version, start_date 

object-attributes:
  - name: "user_key"
    type: "string"
    required: true
    description: |
      32-character hexadecimal user key for your user account. This user key allows Stitch to access your {{ form-property.diaplay-name }} account's API. You can retrieve your user key in the **API User Key** row on the settings page of your {{ form-property.display-name }} account.
    value: "<YOUR_USER_KEY>"

  - name: "email"
    type: "string"
    required: true
    description: "The email address used for your {{ form-property.diaplay-name }} account."
    value: "<YOUR_EMAIL_ADDRESS>"
    
  - name: "password"
    type: "string"
    required: true
    description: "The password used for your {{ form-property.diaplay-name }} account."
    value: "<YOUR_PASSWORD>"

  - name: "pardot_business_unit_id"
    type: "string"
    required: true
    description: "The 18-character long business unit ID for your {{ form-property.diaplay-name }} account. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#retrieve-business-unit" }}) for instructions on retrieving this credential."
    value: "<YOUR_BUSINESS_UNIT_ID>"


# -------------------------- #
#       OAUTH PROPERTIES     #
# -------------------------- #

oauth-link: "https://developer.pardot.com/kb/authentication/"

oauth-description: ""

oauth-attributes:
  - name: "client_id"
    type: "string"
    required: true
    credential: false
    description: |
      Your Salesforce connected app's consumer key. This info can be found on the connected app's **Manage Connected Apps** page or from the connected app's definition. Refer to [Salesforce's documentation](https://help.salesforce.com/articleView?id=connected_app_create_api_integration.htm&type=5){:target="new"} for more info.
    value: "<YOUR_CONNECTED_APP_CLIENT_ID>"

  - name: "client_secret"
    type: "string"
    required: true
    credential: true
    description: |
      Your Salesforce connected app's consumer secret. This info can be found on the connected app's **Manage Connected Apps** page or from the connected app's definition. Refer to [Salesforce's documentation](https://help.salesforce.com/articleView?id=connected_app_create_api_integration.htm&type=5){:target="new"} for more info.
    value: "<YOUR_CONNECTED_APP_CLIENT_SECRET>"

  - name: "refresh_token"
    type: "string"
    required: true
    credential: true
    description: |
      A token that your Salesforce connected app will use to obtain new access tokens, when needed.
    value: "<REFRESH_TOKEN>"   
---