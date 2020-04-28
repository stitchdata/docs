---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "connect"
content-type: "api-form"
form-type: "source"
key: "source-form-properties-import-api-object"


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Import API Source Form Property"
api-type: "import_api"
display-name: "Import API"

source-type: "import-api"
docs-name: "import-api"

description: |
  To create an Import API source, the only required property is `type`, which must have a value of `import_api`.

  **Note**: While Import API source form properties don't technically have any form properties, some setup is still required to fully configure this source. Refer to the [Create and Configure an Import API Source with the Connect API guide]({{ link.connect.guides.create-import-api-source | prepend: site.baseurl }}) for help setting up this source.

## Used to override code in _includes/developers/api-form-properties.html and _includes/developers/api-form-property-example-object.html
override-attributes: true
---