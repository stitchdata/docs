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
key: "source-form-properties-clubspeed-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Club Speed Source Form Property"
api-type: "clubspeed"
display-name: "Club Speed"

source-type: "saas"
docs-name: "clubspeed"

description: ""


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

# uses-common-fields: true/false
# See these fields in _data/connect/common/all-sources.yml
# May also include applicable fields in _data/connect/common/all-sources.yml

object-attributes:
  - name: "private_key"
    type: "string"
    required: true
    description: "The user's {{ form-property.display-name }} private API key. The user will need to contact [{{ form-property.display-name }} support](mailto: support@clubspeed.com) to obtain this credential."
    value: "<PRIVATE_API_KEY>"

  - name: "subdomain"
    type: "string"
    required: true
    description: |
      The user's {{ form-property.display-name }} subdomain.

      **For example:** If the full URL is `stitchdata.clubspeedtiming.com`, only `stitchdata` should be entered.
    value: "<SUBDOMAIN>"    
---