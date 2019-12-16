---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

product-type: "import-api"
content-type: "api-object"
endpoint: "push"
version: "2"
order: 4


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Push"
description: "{{ site.data.import-api.core-objects.push.object | flatify }}"
endpoint-url: "/import/push"


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
  - id: "push-data"
    title: "Push data"
    method: "post"
    short: "{{ site.data.import-api.core-objects.push.description | flatify }}"


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