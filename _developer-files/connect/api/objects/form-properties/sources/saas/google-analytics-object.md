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
key: "source-form-properties-google-analytics-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Google Analytics Source Form Property"
api-type: "platform.google-analytics"
display-name: "Google Analytics"

source-type: "saas"
docs-name: "google-analytics"


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

object-attributes:
  - name: "quota_user"
    type: "string"
    required: true
    read-only: true
    description: ""
    value: ""

  - name: "report_definitions"
    type: "array"
    required: true
    description: |
      A list of the custom reports you want to create.

      Each report you want to create should be its own object and contain `name` and `id` properties.
    value: |
      [
           {
              "name":"Visitor Traffic",
              "id":"visitor-traffic-report"
           },
           {
              "name":"Site A ECommerce",
              "id":"site-a-ecommerce-report"
           }
         ]
    subattributes:
      - name: "id"
        type: "string"
        required: true
        description: "A unique ID for the custom report."

      - name: "name"
        type: "string"
        required: true
        description: "The name of the custom report. This will be used to create the name of the corresponding table in the destination."
---