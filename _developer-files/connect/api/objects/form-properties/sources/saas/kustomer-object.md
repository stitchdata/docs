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
key: "source-form-properties-kustomer-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Kustomer Source Form Property"
api-type: "platform.kustomer"
display-name: "Kustomer"

source-type: "saas"
docs-name: "kustomer" # This should be whatever integration.name is. Ex: LinkedIn Ads is linkedin-ads

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
      Your {{ form-propery.display-name }} API key. Refer to the [{{ form-propery.display-name }} documentation]({{ doc-link | append: "#obtain-api-key" }}) for instruction on how to obtain this.
    value: "<YOUR_API_KEY>"

  - name: "date_window_size"
    type: "string"
    required: false
    description: "This is an internal field for Stitch use."
    value: "<DATE_WINDOW_SIZE>"
    
  - name: "page_size_limit"
    type: "string"
    required: false
    description: "This is an internal field for Stitch use."
    value: "<PAGE_SIZE_LIMIT>"    
---