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
key: "source-form-properties-eloqua-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Eloqua Source Form Property"
api-type: "platform.eloqua"
display-name: "Eloqua"

source-type: "saas"
docs-name: "eloqua"

property-description: |
  the {{ form-property.display-name }} Bulk and REST APIs

description: ""

# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

# uses-common-fields: true/false
# See these fields in _data/connect/common/all-sources.yml
# May also include applicable fields in _data/connect/common/all-sources.yml

object-attributes:
  - name: "bulk_page_size"
    type: "string"
    required: false
    description: |
      The number of records each page in a bulk export should contain. **Note**: This setting only affects streams that use the {{ form-property.display-name }} Bulk API. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#schema" }}) for info about how each stream is replicated.
    value: "5000"
---