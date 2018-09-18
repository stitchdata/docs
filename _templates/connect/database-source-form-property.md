---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/connect-templates/database-source-form-property/
## FOR INSTRUCTIONS & REFERENCE INFO

## PLEASE REMOVE COMMENTS WHEN FINISHED


content-type: "api-form"
form-type: "source"
key: "source-form-properties-[integration]-object"

title: "[INTEGRATION] Source Form Property"
api-type: ""
display-name: "[INTEGRATION]"

source-type: "database"
docs-name: ""
db-type: ""

description: ""
uses-common-fields: true

# NOTE: object-attributes is only required if the object has attributes
# 		  that are specific to it. Ex: platform.s3-csv has a `bucket` attribute
#				that is only specific to S3.
# 			Otherwise, when `uses-common-fields` is `true`, the applicable fields
#				from _data/connect/common/database-sources.yml will display. You don't
# 			need to do a thing :)
# 			Other common fields:  _data/connect/common/all-sources.yml

#				Please remove me ^

# object-attributes:
#   - name: ""
#     type: ""
#     required: true/false
#     description: ""
#     value: ""
---