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
key: "source-form-properties-saasoptics-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "SaaSOptics Source Form Property"
api-type: "platform.saasoptics"
display-name: "SaaSOptics"

source-type: "saas"
docs-name: "saasoptics" # This should be whatever integration.name is. Ex: LinkedIn Ads is linkedin-ads


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

# Only source-specific attributes need to be listed here.
# The following attributes are considered common,
# and therefore don't need to be listed:
# anchor_time, cron_expression, frequency_in_minutes, image_version, start_date 

object-attributes:
  - name: "account_name"
    type: "string"
    required: true
    description: |
      The name of your unique SaaSOptics database schema, called an "account." This account is the one in which your subscription financial records are managed.
    value: "<YOUR_ACCOUNT_NAME>"

  - name: "server_subdomain"
    type: "string"
    required: true
    description: "The subdomain of the SaaSOptics server where the account is running."
    value: "<YOUR_SUBDOMAIN>"
    
  - name: "token"
    type: "string"
    required: true
    description: |
      The API token. This token allows Stitch to access your {{ form-property.diaplay-name }} account's API. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#obtain-token" }}) for instructions on retrieving this credential.
    value: "<YOUR_API_TOKEN>"
    
  - name: "date_window_size"
    type: "string"
    required: true
    description: "This is an internal field for Stitch use. The value is defaulted to 60."
    value: "60"
---