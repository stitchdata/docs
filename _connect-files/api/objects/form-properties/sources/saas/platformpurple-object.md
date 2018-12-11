---
content-type: "api-form"
form-type: "source"
key: "source-form-properties-platformpurple-object"

title: "Platform Purple Source Form Property"
api-type: "platformpurple"
display-name: "Platform Purple"

source-type: "saas"
docs-name: "platformpurple"

description: ""

object-attributes:
  - name: "api_key"
    type: "string"
    required: true
    description: "The user's {{ form-property.display-name }} API key. This can be obtained by contacting {{ form-property.display-name }}."
    value: "<API_KEY>"

  - name: "environment"
    type: "sting"
    required: true
    description: "The user's {{ form-property.display-name }} environment. This can be obtained by contacting {{ form-property.display-name }}."
    value: "<ENVIRONMENT>"
---