---
# -------------------------- #
#     USING THIS TEMPLATE    #
# -------------------------- #

## NEED HELP USING THIS TEMPLATE? SEE:
## https://docs-about-stitch-docs.netlify.com/reference/connect-templates/destination-form-property/
## FOR INSTRUCTIONS & REFERENCE INFO

## PLEASE REMOVE COMMENTS WHEN FINISHED



# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-form"
form-type: "destination"
key: "destination-form-properties-mysql-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "MySQL Destination Form Property"
api-type: "mysql"
display-name: "MySQL"

docs-name: "mysql"
db-type: "mysql"

property-description: ""
## Used to create a description for the object that doesn't adhere to the standard in _developers/connect/api/documentation/api-form-properties.html
## See the Heap object for an example

description: ""


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-common-fields: false
## See these fields in _data/connect/common/destination-forms.yml > all-destinations

object-attributes:
  - name: "host"
    required: true
    internal: false
    type: "string"
    description: "The IP address or hostname of the database server."
    value: |
      "<HOST_ADDRESS>"

  - name: "password"
    required: true
    internal: false
    type: "string"
    description: "The password for the user connecting to the database server. **Note**: This property will never be returned by the API, but it can be submitted when creating or modifying a connection."
    value: |
      "<PASSWORD>"

  - name: "port"
    required: true
    internal: false
    type: "string"
    description: "The port of the database server. The default is `{{ port }}`."
    value: |
      "{{ port }}"

  - name: "username"
    required: true
    internal: false
    type: "string"
    description: "The username of the database user."
    value: |
      "<USERNAME>"
---