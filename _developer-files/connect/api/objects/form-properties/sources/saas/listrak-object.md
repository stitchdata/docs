---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-form"
form-type: "source"
key: "source-form-properties-listrak-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Listrak Source Form Property"
api-type: "platform.listrak"
display-name: "Listrak"

source-type: "saas"
docs-name: "listrak"

description: ""


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-start-date: true

object-attributes:
  - name: "password"
    type: "string"
    required: true
    description: "The password associated with the {{ form-property.display-name }} user."
    value: "{{ sample-property-data.password }}"

  - name: "username"
    type: "string"
    required: true
    description: "Your {{ form-property.display-name }} username."
    value: "{{ sample-property-data.user }}"
---