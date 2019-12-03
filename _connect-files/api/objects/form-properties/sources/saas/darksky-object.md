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

content-type: "api-form"
form-type: "source"
key: "source-form-properties-darksky-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Darksky Source Form Property"
api-type: "platform.darksky"
display-name: "Darksky"

source-type: "saas"
docs-name: "darksky"

property-description: ""
## Used to create a description for the object that doesn't adhere to the standard in _developers/connect/api/documentation/api-form-properties.html
## See the Heap object for an example


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

# Only source-specific attributes need to be listed here.
# The following attributes are considered common,
# and therefore don't need to be listed:
# anchor_time, cron_expression, frequency_in_minutes, image_version, start_date 

object-attributes:
  - name: "language"
    type: "string"
    required: true
    description: |
      The language that `summary` attributes in the `forecast` table should be returned in. For example: If set to `en`, `summary` data will be returned in English.
      
      Refer to [{{ form-property.display-name }}'s documentation](https://darksky.net/dev/docs#time-machine-request){:target="new"} for a list of accepted values.
    value: "en"

  - name: "location_list"
    type: "string"
    required: true
    description: "The longitude and latitude of the location the app was used."
    value: "00.000000, -000.000000"
    
  - name: "secret_key"
    type: "string"
    required: true
    description: "The secret API Key"
    value: "YOUR_SECRET_KEY"
    
  - name: "units"
    type: "string"
    required: true
    description: "The unit of measurement."
    value: "us"      
---
