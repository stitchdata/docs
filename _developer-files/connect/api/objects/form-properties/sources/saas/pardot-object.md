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
      32-character hexadecimal user key for your user account. This user key allows Stitch to access your {{ form-property.diaplay-name }} account's API. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#retrieve-user-key" }}) for instructions on retrieving this credential.
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
---