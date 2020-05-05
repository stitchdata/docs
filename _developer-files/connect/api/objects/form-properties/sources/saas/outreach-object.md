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
key: "source-form-properties-outreach-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Outreach Source Form Property"
api-type: "platform.outreach"
display-name: "Outreach"

source-type: "saas"
docs-name: "outreach" # This should be whatever integration.name is. Ex: LinkedIn Ads is linkedin-ads

# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

# Only source-specific attributes need to be listed here.
# The following attributes are considered common,
# and therefore don't need to be listed:
# anchor_time, cron_expression, frequency_in_minutes, image_version, start_date 

object-attributes:
  - name: "quota_limit"
    type: "string"
    required: false
    description: |
      The percentage of your standard {{ form-property.display-name }} API quota Stitch is allowed to use. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#add-integration" }}) for more information on defining this limit.
    value: "XX"
---