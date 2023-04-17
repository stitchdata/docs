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
key: "source-form-properties-twilio-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Twilio Source Form Property"
api-type: "platform.twilio"
display-name: "Twilio"

source-type: "saas"
docs-name: "twilio" # This should be whatever integration.name is. Ex: LinkedIn Ads is linkedin-ads


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

object-attributes:
  - name: "account_sid"
    type: "string"
    required: true
    description: |
      Your {{ form-property.display-name }} account SID. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#retrieve-auth-sid" }}) to retrieve this information.
    value: "<YOUR_ACCOUNT_SID>"

  - name: "auth_token"
    type: "string"
    required: true
    description: |
      Your {{ form-property.display-name }} auth token. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#retrieve-auth-sid" }}) to retrieve this information.
    value: "<YOUR_AUTH_TOKEN>"
  
  - name: "date_window_days"
    type: "integer"
    required: false
    description: "The number of days of data to replicate at a time. The default value is `30`."
    value: "XX"    
---