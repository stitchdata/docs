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
key: "source-form-properties-ga4-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Google Analytics 4 Source Form Property"
api-type: "platform.ga4"
display-name: "Google Analytics 4"

source-type: "saas"
docs-name: "google-analytics-4"


# -------------------------- #
#       FORM PROPERTIES      #
# -------------------------- #

uses-start-date: true

object-attributes:
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

  - name: "conversion_window"
    type: "integer"
    required: false
    description: |
      The conversion window. The value can be 30, 60 or 90 days. The conversion window is 90 days by default.    
    value: "X0"    


# -------------------------- #
#       OAUTH PROPERTIES     #
# -------------------------- #

oauth-link: "https://developers.google.com/analytics/devguides/reporting/core/v4/authorization"

oauth-description: ""

oauth-attributes:
  - name: "access_token"
    type: "string"
    required: true
    credential: true
    description: |
      The token used to access your {{ form-property.display-name }} data via API.
    value: "<YOUR_ACCESS_TOKEN>"

  - name: "account_id"
    type: "string"
    required: true
    credential: false
    description: |
      Your {{ form-property.display-name }} account ID. Refer to [Google's documentation](https://developers.google.com/identity/protocols/oauth2/web-server#creatingcred){:target="new"} for more info.
    value: "<YOUR_ACCOUNT_ID>"

  - name: "oauth_client_id"
    type: "string"
    required: true
    credential: false
    description: |
      Your {{ form-property.display-name }} OAuth application's client ID, obtained when you create an OAuth app with Google. Refer to [Google's documentation](https://developers.google.com/identity/protocols/oauth2/web-server#creatingcred){:target="new"} for more info.
    value: "<YOUR_OAUTH_CLIENT_ID>"  

  - name: "oauth_client_secret"
    type: "string"
    required: true
    credential: true
    description: |
      Your {{ form-property.display-name }} OAuth application's client secret, obtained when you create an OAuth app with Google. Refer to [Google's documentation](https://developers.google.com/identity/protocols/oauth2/web-server#creatingcred){:target="new"} for more info.
    value: "<YOUR_OAUTH_CLIENT_SECRET>"

  - name: "property_id"
    type: "string"
    required: true
    credential: false
    description: |
      The ID of the {{ form-property.display-name }} property to extract data from. You can use [Google's Account Explorer](https://ga-dev-tools.appspot.com/account-explorer/){:target="new"} to search or browse through your accounts, properties, and views.
    value: "<A_PROPERTY_ID>"

  - name: "refresh_token"
    type: "string"
    required: true
    credential: true
    description: |
      A long-lived token, used to generate new {{ form-property.display-name }} access tokens when old ones expire.
    value: "<REFRESH_TOKEN>"

  - name: "user_id"
    type: "string"
    required: true
    credential: false
    description: |
      TThe ID of the Google user authorizing the connection. You can use [Google's Account Explorer](https://ga-dev-tools.appspot.com/account-explorer/){:target="new"} to search or browse through your accounts, properties, and views.
    value: "<A_USER_ID>"
---