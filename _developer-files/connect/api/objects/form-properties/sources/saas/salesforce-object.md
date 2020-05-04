---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-form"
form-type: "source"
key: "source-form-properties-salesforce-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Salesforce Source Form Property"
api-type: "platform.salesforce"
display-name: "Salesforce"

source-type: "saas"
docs-name: "salesforce"

description: ""


# -------------------------- #
#       FORM PROPERTIES      #
# -------------------------- #

uses-start-date: true

object-attributes:
  - name: "api_type"
    type: "string"
    required: true
    description: "The {{ form-property.display-name }} API Stitch should use to extract data. Possible values are `REST` or `BULK`. [Read about the pros and cons of each API here]({{ site.baseurl }}/integrations/saas/salesforce#bulk-vs-rest-api)."
    value: "BULK"

  - name: "is_sandbox"
    type: "string"
    required: false
    description: "If `true`, the {{ form-property.display-name }} account being connected is a sandbox."
    value: "false"

  - name: "quota_percent_per_run"
    type: "string"
    required: false
    description: "The maximum percentage of {{ form-property.display-name }} API quota allowed per replication job."
    value: "20"

  - name: "quota_percent_total"
    type: "string"
    required: false
    description: "The maximum percentage of {{ form-property.display-name }} API quota allowed per day."
    value: "80"

  - name: "select_fields_by_default"
    type: "string"
    required: true
    description: "If `true`, Stitch will automatically set new fields added in {{ form-property.display-name }} to replicate."
    value: "false"


# -------------------------- #
#       OAUTH PROPERTIES     #
# -------------------------- #

oauth-link: "https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_oauth_and_connected_apps.htm"

oauth-description: ""

oauth-properties:
  - name: "client_id"
    type: "string"
    required: true
    credential: false
    description: |
      Your {{ form-property.display-name }} connected app's consumer key. This info can be found on the connected app's **Manage Connected Apps** page or from the connected app's definition. Refer to [{{ form-property.display-name }}'s documentation](https://help.salesforce.com/articleView?id=connected_app_create_api_integration.htm&type=5){:target="new"} for more info.
    value: "<YOUR_CONNECTED_APP_CLIENT_ID>"

  - name: "client_secret"
    type: "string"
    required: true
    credential: true
    description: |
      Your {{ form-property.display-name }} connected app's consumer secret. This info can be found on the connected app's **Manage Connected Apps** page or from the connected app's definition. Refer to [{{ form-property.display-name }}'s documentation](https://help.salesforce.com/articleView?id=connected_app_create_api_integration.htm&type=5){:target="new"} for more info.
    value: "<YOUR_CONNECTED_APP_CLIENT_SECRET>"

  - name: "instance_url"
    type: "string"
    required: true
    credential: false
    description: |
      The URL indicating the instance of the authorizing user's org.
    value: "https://yourInstance.salesforce.com"

  - name: "orgid"
    type: "string"
    required: false
    credential: false
    description: |
      The ID of the org the authorizing user belongs to.
    value: "<USER_ORG>"

  - name: "refresh_token"
    type: "string"
    required: true
    credential: true
    description: |
      A token that your {{ form-property.display-name }} connected app will use to obtain new access tokens, when needed.
    value: "<REFRESH_TOKEN>"
---