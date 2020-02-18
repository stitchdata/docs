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
key: "source-form-properties-google-sheets-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Google Sheets Source Form Property"
api-type: "platform.google-sheets"
display-name: "Google Sheets"

source-type: "saas"
docs-name: "google-sheets" # This should be whatever integration.name is. Ex: LinkedIn Ads is linkedin-ads


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

# Only source-specific attributes need to be listed here.
# The following attributes are considered common,
# and therefore don't need to be listed:
# anchor_time, cron_expression, frequency_in_minutes, image_version, start_date 

object-attributes:
  - name: "spreadsheet_id"
    type: "string"
    required: true
    description: "The unique identifier of your spreadsheet. It's also a good idea to link back to the setup docs for this, since locating the spreadsheet ID isn't totally straightforward. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#obtain-spreadsheet-id" }}) for instructions on locating this info."
    value: "<YOUR_SPREADSHEET_ID>"   
---