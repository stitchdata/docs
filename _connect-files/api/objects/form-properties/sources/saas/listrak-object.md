---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

content-type: "api-form"
form-type: "source"
key: "source-form-properties-listrak-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Listrak Source Form Property"
api-type: "listrak"
display-name: "Listrak"

source-type: "saas"
docs-name: "listrak"

description: ""


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

object-attributes:
  - name: "password"
    type: "string"
    required: true
    description: "The password associated with the Listrak user."
    value: "{{ sample-property-data.password }}"

  - name: "username"
    type: "string"
    required: true
    description: "The user's Listrak username."
    value: "{{ sample-property-data.user }}"
---