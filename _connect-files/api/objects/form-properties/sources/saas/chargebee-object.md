---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/connect-templates/destination-form-property/
## FOR INSTRUCTIONS & REFERENCE INFO

## PLEASE REMOVE COMMENTS WHEN FINISHED


# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

content-type: "api-form"
form-type: "source"
key: "source-form-properties-chargebee-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Chargebee Source Form Property"
api-type: "platform.chargebee"
display-name: "Chargebee"

source-type: "saas"
docs-name: "chargebee"

description: ""

# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

# uses-common-fields: true/false
# See these fields in _data/connect/common/all-sources.yml
# May also include applicable fields in _data/connect/common/all-sources.yml

object-attributes:
  - name: "api_key"
    type: "string"
    required: true
    description: |
      The user's {{ form-property.display-name }} API key. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link }}) for info on generating this credential.
    value: "<{{ form-property.display-name | upcase }}_API_KEY>"

  - name: "site"
    type: "string"
    required: true
    description: |
      The name of the user's {{ form-property.display-name }} site. This can be found in the {{ form-property.display-name }} site URL. For example: If the URL was `https://stitch.chargebee.com`, only `stitch` would be entered into this field.
    value: "<{{ form-property.display-name | upcase }}_SITE_NAME>"
---