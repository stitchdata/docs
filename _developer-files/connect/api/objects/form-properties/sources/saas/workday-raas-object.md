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
key: "source-form-properties-workday-raas-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Workday RaaS Source Form Property"
api-type: "platform.workday-raas"
display-name: "Workday RaaS"

source-type: "saas"
docs-name: "workday-raas" # This should be whatever integration.name is. Ex: LinkedIn Ads is linkedin-ads


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

# Only source-specific attributes need to be listed here.
# The following attributes are considered common,
# and therefore don't need to be listed:
# anchor_time, cron_expression, frequency_in_minutes, image_version, start_date 

object-attributes:
  - name: "password"
    type: "string"
    required: true
    description: "Your password for your {{ form-property.display-name }} account."
    value: "<YOUR_PASSWORD>"

  - name: "reports"
    type: "string"
    required: true
    description: |
      Your {{ form-property.display-name }} report URL and table name of your choice. It is a stringified JSON array containing objects with the keys `report_url` and `report_name`.
    value: |
      [{\"report_url\": \"<YOUR_REPORT_URL>", \"table_name\": \"THIS IS MY FIRST TABLE\"},{\"report_url\": \"<YOUR_REPORT_URL", \"table_name\": \"THIS IS MY SECOND TABLE\"}]
    
  - name: "username"
    type: "string"
    required: true
    description: "Your username for your {{ form-property.display-name }} account."
    value: "<YOUR_USERNAME>"    
---