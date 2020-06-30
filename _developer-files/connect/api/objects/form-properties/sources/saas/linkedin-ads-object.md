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
#       FORM PROPERTIES      #
# -------------------------- #

uses-start-date: true

object-attributes:
  - name: "accounts"
    type: "string"
    required: true
    description: "A comma-separated list of accounts to replicate."
    value: "123456789"


# -------------------------- #
#       OAUTH PROPERTIES     #
# -------------------------- #

oauth-link: "https://docs.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow?context=linkedin/context"

oauth-description: ""

oauth-attributes:
  - name: "access_token"
    type: "string"
    required: true
    credential: true
    description: |
      The {{ form-property.display-name }} token to use in future requests to the {{ form-property.display-name }} API, created after a successful OAuth handshake.
    value: "<ACCESS_TOKEN>"
---