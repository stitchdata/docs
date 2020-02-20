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
key: "source-form-properties-darksky-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Darksky Source Form Property"
api-type: "platform.darksky"
display-name: "Darksky"

source-type: "saas"
docs-name: "darksky"


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

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
    description: |
      The longitude and latitude of the locations to be returned. The locations must be semi-colon delineated. 

      For example: `<latitude>,<longitude>` is an accepted value for a single location, and `<latitude>,<longitude>;<latitude>,<longitude>; ... etc` is accepted for multiple locations.
    value: "00.000000,-000.000000"
    
  - name: "secret_key"
    type: "string"
    required: true
    description: "Your {{ form-property.display-name }} secret API key. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link }}) for instructions on obtaining this credential."
    value: "<{{ form-property.display-name | upcase }}_SECRET_KEY>"
    
  - name: "units"
    type: "string"
    required: true
    description: |
      The requested unit of measurement for weather conditions to be returned.

      For example: `us` for Imperial Units, and `si` for International System of Units.
    value: "us"
---