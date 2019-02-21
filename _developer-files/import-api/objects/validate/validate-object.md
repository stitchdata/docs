---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "import-api"
content-type: "api-object"
endpoint: "validate"
version: "2"
order: 1


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Validate"
description: "{{ api.core-objects.validate.object-description | flatify }}"
endpoint-url: "/import/validate"


# -------------------------- #
#        VERSION INFO        #
# -------------------------- #

latest-version: "2"
versions:
  - number: "2"
    deprecated: false

# -------------------------- #
#      AVAILABLE METHODS     #
# -------------------------- #

available-methods:
  - id: "validate-request"
    title: "Validate request"
    method: "post"
    short: "{{ api.core-objects.validate.description | flatify }}"


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

## The copy for these attributes lives in:
## _data/import-api/general.yml

object-attributes:
  - name: "client_id"
    type: "integer"
    description: "{{ general.attributes.client-id }}"
    value: "7723"

  - name: "table_name"
    type: "string"
    description: "{{ general.attributes.table-name }}"
    value: "customers"

  - name: "sequence"
    type: "integer"
    description: "{{ general.attributes.sequence | flatify }}"
    value: "1550702340229"

  - name: "action"
    type: "string"
    description: "This will always be `upsert`."
    value: "upsert"

  - name: "key_names"
    type: "array"
    description: "{{ general.attributes.key-names }}"
    value: "id"

  - name: "data"
    type: "object"
    description: "{{ general.attributes.data | flatify }}"
---