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
docs-name: "workday-raas"


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

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
      A stringified JSON array containing objects with `report_url` and `report_name` keys. For every report you want to replicate from {{ form-property.display-name }}, include an object with these keys:

      - `report_url` - A report's Workday XML REST link. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#retrieve-report-url" }}) for instructions on retrieving this info from {{ form-property.display-name }}.
      - `report_name` - A report name of your choice

      Refer to the [example object](#{{ form-property.key }}-example-usage) below to see what this value should look like.
      
    value: |
      [{\"report_url\": \"<REPORT_URL_1>", \"table_name\": \"REPORT_ONE\"},{\"report_url\": \"<REPORT_URL_2>", \"table_name\": \"REPORT_TWO\"}]
    
  - name: "username"
    type: "string"
    required: true
    description: "Your username for your {{ form-property.display-name }} account."
    value: "<YOUR_USERNAME>"    
---