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
key: "source-form-properties-google-search-console-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Google Search Console Source Form Property"
api-type: "platform.google-search-console"
display-name: "Google Search Console"

source-type: "saas"
docs-name: "google-search-console" # This should be whatever integration.name is. Ex: LinkedIn Ads is linkedin-ads


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

# Only source-specific attributes need to be listed here.
# The following attributes are considered common,
# and therefore don't need to be listed:
# anchor_time, cron_expression, frequency_in_minutes, image_version, start_date 

object-attributes:
  - name: "site_urls"
    type: "string"
    required: true
    description: "The domains and websites that belong to your organization. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#set-up-console" }}) for instructions on how to set these URLs up in your {{ form-property.display-name }} account."
    value: ""


# -------------------------- #
#       OAUTH PROPERTIES     #
# -------------------------- #

oauth-link: "https://developers.google.com/webmaster-tools/search-console-api-original/v3/how-tos/authorizing"

oauth-description: ""

oauth-attributes:
  - name: "client_id"
    type: "string"
    required: true
    credential: true
    description: |
      Your {{ form-property.display-name }} OAuth application's client ID, obtained when you create an OAuth app with Google. Refer to [Google's documentation](https://developers.google.com/identity/protocols/oauth2){:target="new"} for more info.
    value: "<YOUR_OAUTH_CLIENT_ID>"

  - name: "client_secret"
    type: "string"
    required: true
    credential: true
    description: |
      Your {{ form-property.display-name }} OAuth application's client secret, obtained when you create an OAuth app with Google. Refer to [Google's documentation](https://developers.google.com/identity/protocols/oauth2){:target="new"} for more info.
    value: "<YOUR_OAUTH_CLIENT_SECRET>"

  - name: "refresh_token"
    type: "string"
    required: true
    credential: true
    description: |
      A long-lived token, used to generate new {{ form-property.display-name }} access tokens when old ones expire.
    value: "<REFRESH_TOKEN>"
---