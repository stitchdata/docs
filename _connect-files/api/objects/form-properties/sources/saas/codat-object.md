---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/connect-templates/destination-form-property/
## FOR INSTRUCTIONS & REFERENCE INFO

## This integration doesn't currently have a report card, so it can't be created
## through the API. This object will be visible in the docs when the report card
## has been created.


# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

# content-type: "api-form"
form-type: "source"
key: "source-form-properties-codat-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Codat Source Form Property"
api-type: "platform.codat"
display-name: "Codat"

source-type: "saas"
docs-name: "codat"

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
      The user's {{ form-property.display-name }} API key. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | prepend: site.baseurl }}) for instructions on retrieving this credential.
    value: "<{{ form-property.display-name | upcase }}_API_KEY>"

  - name: "uat_urls"
    type: "string"
    required: false
    description: |
      Indicates whether the instance being connected is a UAT (sandbox) instance or not.
    value: ""
---