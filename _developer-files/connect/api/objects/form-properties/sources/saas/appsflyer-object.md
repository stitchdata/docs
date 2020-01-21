---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-form"
form-type: "source"
key: "source-form-properties-appsflyer-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "AppsFlyer Source Form Property"
api-type: "platform.appsflyer"
display-name: "AppsFlyer"

source-type: "saas"
docs-name: "appsflyer"

description: ""


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

object-attributes:
  - name: "api_token"
    type: "string"
    required: true
    description: |
      The API token for the {{ form-property.display-name }} account Stitch should replicate data from. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#retrieve-your-api-key" }}) for instructions on retrieving this info.
    value: "<API_TOKEN>"

  - name: "app_id"
    type: "string"
    required: true
    description: |
      The app ID for the {{ form-property.display-name }} account Stitch should replicate data from. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#retrieve-the-app-id" }}) for instructions on retrieving this info.
    value: "<API_TOKEN>"
---