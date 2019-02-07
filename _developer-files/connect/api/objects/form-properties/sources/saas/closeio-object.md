---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-form"
form-type: "source"
key: "source-form-properties-closeio-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Close.io Source Form Property"
api-type: "closeio"
display-name: "Close.io"

source-type: "saas"
docs-name: "closeio"

description: ""


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

object-attributes:
  - name: "api_key"
    type: "string"
    required: true
    description: |
      The user's {{ form-property.display_name }} API key. API keys can be generated in {{ form-property.display_name }} by navigating to **Settings > Your API Keys**.
    value: "<API_KEY>"
---