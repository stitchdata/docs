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
key: "source-form-properties-3plcentral-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "3PL Central Source Form Property"
api-type: "platform.3plcentral"
display-name: "3PL Central"

source-type: "saas"
docs-name: "3plcentral"

description: |
  The credentials required to configure a {{ form-property.display-name }} source must be requested from a {{ form-property.display-name }} account manager. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link }}) for more info.


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

# Only source-specific attributes need to be listed here.
# The following attributes are considered common,
# and therefore don't need to be listed:
# anchor_time, cron_expression, frequency_in_minutes, image_version, start_date 

object-attributes:
  - name: "base_url"
    type: "string"
    required: true
    description: "The API URL to which /endpoints are appended."
    value: "https://secure-wms.com"

  - name: "client_id"
    type: "string"
    required: true
    description: "The secure OAuth 2.0 identifier for the {{ form-property.display-name }} application/client."
    value: "<OAUTH_CLIENT_ID>"
    
  - name: "client_secret"
    type: "string"
    required: true
    description: "The secure OAuth 2.0 secret key for the {{ form-property.display-name }} application/client authentication."
    value: "<OAUTH_CLIENT_SECRET>"
    
  - name: "customer_id"
    type: "string"
    required: true
    description: "The ID for the {{ form-property.display-name }} customer organization."
    value: "<CUSTOMER_INTEGER_ID>"
    
  - name: "facility_id"
    type: "string"
    required: true
    description: "The ID for the {{ form-property.display-name }} warehouse facility."
    value: "<FACILITY_INTEGER_ID>"
    
  - name: "tpl_key"
    type: "string"
    required: true
    description: "A {{ form-property.display-name }} warehouse-specific 3PL key."
    value: "<WH_SPECIFIC_3PL_KEY>"
    
  - name: "user_login_id"
    type: "string"
    required: true
    description: "The ID for the {{ form-property.display-name }} user."
    value: "<USER_INTEGER_ID>"
---