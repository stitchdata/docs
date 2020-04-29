---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-form"
form-type: "source"
key: "source-form-properties-covid-19-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "COVID-19 Public Data Source Form Property"
api-type: "platform.covid-19"
display-name: "COVID-19 Public Data"

source-type: "saas"
docs-name: "covid-19"

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
      A GitHub access token which allows access to any project the user wants to replicate data from. **Note**: This access token must have the `repo` scope at a minimum. Refer to the [{{ form-property.display-name }} documentation]({{ doc-link | append: "#create-access-token" }}) for more info.
    value: "<ACCESS_TOKEN>"
---