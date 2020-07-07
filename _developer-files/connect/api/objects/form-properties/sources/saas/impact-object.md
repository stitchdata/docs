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
key: "source-form-properties-impact-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Impact Source Form Property"
api-type: "platform.impact"
display-name: "Impact"

source-type: "saas"
docs-name: "impact" # This should be whatever integration.name is. Ex: LinkedIn Ads is linkedin-ads

# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

# Only source-specific attributes need to be listed here.
# The following attributes are considered common,
# and therefore don't need to be listed:
# anchor_time, cron_expression, frequency_in_minutes, image_version, start_date 

object-attributes:
  - name: "account_sid"
    type: "string"
    required: true
    description: |
      The read-only version of your {{ form-property.display-name }} Account SID. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#retrieve-sid-auth" }}) for instructions on locating this info.
    value: "<YOUR_API_ACCOUNT_SID>"

  - name: "api_catalog"
    type: "string"
    required: true
    description: |
      The internal {{ form-property.display-name }} API you're using for the Stitch {{ form-property.display-name }} integration. Currently the only supported option is `advertisers`.
    value: "advertisers"
    
  - name: "auth_token"
    type: "string"
    required: true
    description: |
      The read-only version of your {{ form-property.display-name }} Auth Token. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#retrieve-sid-auth" }}) for instructions on locating this info.
    value: "<YOUR_API_AUTH_TOKEN>"
    
  - name: "model_id"
    type: "string/integer"
    required: false
    description: |
      Identifies the conversion process and the necessary steps from click to conversion. It is an optional parameter for the `conversion_paths` endpoint, which shows conversions from clicks to conversion purchases. The only way to access this ID, you need to contact [{{ form-property.display-name }} Radius Support](mailto:support@impactradius.com) or [open an {{ form-property.display-name }} help desk request](https://help.impactradius.com/hc/en-us/requests){:target="new"} with {{ form-property.display-name }}.
    value: "<YOUR_MODEL_ID>"
---