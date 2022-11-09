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
key: "source-form-properties-activecampaign-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "ActiveCampaign Source Form Property"
api-type: "platform.activecampaign"
display-name: "ActiveCampaign"

source-type: "saas"
docs-name: "activecampaign" # This should be whatever integration.name is. Ex: LinkedIn Ads is linkedin-ads

# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

# Only source-specific attributes need to be listed here.
# The following attributes are considered common,
# and therefore don't need to be listed:
# anchor_time, cron_expression, frequency_in_minutes, image_version, start_date 

object-attributes:
  - name: "api_token"
    type: "string"
    required: true
    description: |
      Your {{ form-property.display-name }} API token. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#retrieve-api" }}) for instructions on retrieving this info.
    value: "<YOUR_API_TOKEN>"

  - name: "api_url"
    type: "string"
    required: true
    description: |
      Your {{ form-property.display-name }} API URL. Your URL should begin with `https://`. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#retrieve-api" }}) for instructions on retrieving this info.
    value: "<YOUR_API_URL>"
---