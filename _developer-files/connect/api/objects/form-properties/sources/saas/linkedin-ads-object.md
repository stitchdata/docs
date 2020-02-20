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
key: "source-form-properties-linkedin-ads-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "LinkedIn Ads Source Form Property"
api-type: "platform.linkedin-ads"
display-name: "LinkedIn Ads"

source-type: "saas"
docs-name: "linkedin-ads"

description: ""

# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

object-attributes:
  - name: "accounts"
    type: "string"
    required: true
    description: "A comma-separated list of accounts to replicate."
    value: "123456789"
---