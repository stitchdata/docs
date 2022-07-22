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
key: "destination-form-properties-microsoft-sql-server-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Microsoft SQL Server Destination Form Property"
api-type: "mssql_server"
display-name: "Microsoft SQL Server"

docs-name: "microsoft-sql-server"
db-type: "microsoft-sql-server"

property-description: ""
## Used to create a description for the object that doesn't adhere to the standard in _developers/connect/api/documentation/api-form-properties.html
## See the Heap object for an example

description: ""


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

uses-common-fields: true
## See these fields in _data/connect/common/destination-forms.yml > all-destinations

 object-attributes:
  - name: "ssl"
    required: false
    internal: false
    type: "boolean"
    description: "If `true`, SSL will be used to connect to the database."
    value: "true"
---