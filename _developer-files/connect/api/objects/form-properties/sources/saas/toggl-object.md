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

type: "connect"
content-type: "api-form"
form-type: "source"
key: "source-form-properties-toggl-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Toggl Source Form Property"
api-type: "toggl"
display-name: "Toggl"

source-type: "saas"
docs-name: "toggl"

description: ""


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-common-fields: true

object-attributes:
  - name: "api_token"
    type: "string"
    required: true
    description: "The user's {{ form-property.display-name }} API token. For more info and instructions on retrieving this credential, refer to our [{{ form-property.display-name }} setup documentation]({{ doc-link }})."
    value: "<API_TOKEN>"

  - name: "detailed_report_trailing_days"
    type: "string"
    required: true
    description: |
      The number of days Stitch should replicate time entry data for during each replication job. This is only applicable to the `time_entries` stream.

      For example: If this value is `5`, Stitch will replicate the past five days' worth of data for the `time_entries` stream during every replication job. 
    value: "5"
---