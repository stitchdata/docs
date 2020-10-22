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
key: "source-form-properties-ms-teams-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Microsoft Teams Source Form Property"
api-type: "platform.ms-teams"
display-name: "Microsoft Teams"

source-type: "saas"
docs-name: "ms-teams" # This should be whatever integration.name is. Ex: LinkedIn Ads is linkedin-ads


# -------------------------- #
#       OAUTH PROPERTIES     #
# -------------------------- #

oauth-link: "https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-v2-protocols"

oauth-description: ""

oauth-attributes:
  - name: "client_id"
    type: "string"
    required: true
    credential: false
    description: |
      Your OAuth application's client ID, obtained when you create an app with Azure.
    value: "<YOUR_CLIENT_ID>"

  - name: "client_secret"
    type: "string"
    required: true
    credential: true
    description: |
      Your OAuth application's client secret, obtained when you create an app with Azure.
    value: "<YOUR_CLIENT_SECRET>"

  - name: "tenant_id"
    type: "string"
    required: true
    credential: false
    description: |
      Your Office 365 tenant ID. This is ID is located on the **Properites** page in your Azure Active Directory.
    value: "<YOUR_TENANT_ID>"