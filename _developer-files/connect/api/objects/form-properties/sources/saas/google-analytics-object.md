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
key: "source-form-properties-google-analytics-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Google Analytics Source Form Property"
api-type: "platform.google-analytics"
display-name: "Google Analytics"

source-type: "saas"
docs-name: "google-analytics"


# -------------------------- #
#       FORM PROPERTIES      #
# -------------------------- #

uses-start-date: true

object-attributes:
  - name: "quota_user"
    type: "string"
    required: true
    read-only: true
    description: ""
    value: ""

  - name: "report_definitions"
    type: "array"
    required: true
    description: |
      An array of objects, each object pertaining to a custom report you want to create.

      **Note**: Metrics and dimensions for each report can be selected when the source proceeds to the `field_selection` step.
    value: |
      [
           {
              "name":"Visitor Traffic",
              "id":"visitor-traffic-report"
           },
           {
              "name":"Site A ECommerce",
              "id":"site-a-ecommerce-report"
           }
         ]
    subattributes:
      - name: "id"
        type: "string"
        required: true
        description: "A unique ID for the custom report."

      - name: "name"
        type: "string"
        required: true
        description: "The name of the custom report. This will be used to create the name of the corresponding table in the destination."


# -------------------------- #
#       OAUTH PROPERTIES     #
# -------------------------- #

oauth-link: "https://developers.google.com/analytics/devguides/reporting/core/v4/authorization"

oauth-description: ""

oauth-properties:
  - name: "client_id"
    type: "string"
    required: true
    credential: true
    description: |
      Your {{ form-property.display-name }} OAuth application's client ID, obtained when you create an OAuth app with Google. Refer to [Google's documentation](https://developers.google.com/identity/protocols/oauth2/web-server#creatingcred){:target="new"} for more info.
    value: "<YOUR_OAUTH_CLIENT_ID>"

  - name: "client_secret"
    type: "string"
    required: true
    credential: true
    description: |
      Your {{ form-property.display-name }} OAuth application's client secret, obtained when you create an OAuth app with Google. Refer to [Google's documentation](https://developers.google.com/identity/protocols/oauth2/web-server#creatingcred){:target="new"} for more info.
    value: "<YOUR_OAUTH_CLIENT_SECRET>"

  - name: "refresh_token"
    type: "string"
    required: true
    credential: true
    description: |
      A long-lived token, used to generate new {{ form-property.display-name }} access tokens when old ones expire.
    value: "<REFRESH_TOKEN>"

  - name: "view_id"
    type: "string"
    required: true
    credential: false
    description: |
      The ID of the {{ form-property.display-name }} view (profile) to extract data from. You can use [Google's Account Explorer](https://ga-dev-tools.appspot.com/account-explorer/){:target="new"} to search or browse through your accounts, properties, and views.
    value: "<A_VIEW_ID>"
---