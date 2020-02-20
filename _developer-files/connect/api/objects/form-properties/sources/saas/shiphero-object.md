---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-form"
form-type: "source"
key: "source-form-properties-shiphero-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "ShipHero Source Form Property"
api-type: "platform.shiphero"
display-name: "ShipHero"

source-type: "saas"
docs-name: "shiphero"

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
      A {{ form-property.display-name }} API token, used to authenticate to ShipHero's API.

      **Note**: [In the {{ form-property.display-name }} app](https://help.shiphero.com/article/32-where-can-i-get-my-api-credentials){:target="new"}, this is referred to as an **API Key**.
    value: "<API_TOKEN>"
---