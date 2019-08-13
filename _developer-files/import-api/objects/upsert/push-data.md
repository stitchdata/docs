---
# -------------------------- #
#      ENDPOINT DETAILS      #
# -------------------------- #

product-type: "import-api"
content-type: "api-endpoint"
endpoint: "push"
key: "push-data"
version: "2"


# -------------------------- #
#       METHOD DETAILS       #
# -------------------------- #

title: "Push data"
method: "post"
short-url: |
  /v{{ object.version }}{{ object.endpoint-url | flatify }}
full-url: |
  {{ api.base-url }}{{ endpoint.short-url | flatify }}
short: "{{ api.core-objects.push.short | flatify }}"
description: |
  {{ site.data.import-api.core-objects.push.description | flatify | markdownify }}

  When data for a table is pushed for the first time, Stitch will create the table in the destination in the specified integration schema.

  During subsequent pushes, one of two things will happen depending on the destination being used:

  1. **If the destination supports upserts**, Stitch will perform an update operation on applicable existing rows to overwrite the data.
  2. **If the destination doesn't support upserts**, Stitch will load the records in an append-only fashion. This means that existing records in the destination table will not be updated, and all records in subsequent pushes will be appended to the end of the table.

  #### Structuring request body data {#push--structure-request-body-data}

  Refer to the [Structuring data for the Import API guide]({{ link.import-api.guides.structure-data | prepend: site.baseurl }}) for instructions and examples.

request-body: |
  The request body should provide an array (batch) of records to be inserted into the pipeline that adhere to the following:

  {% for requirement in general.request-body-requirements %}
  - {{ requirement.description | markdownify }}
  {% endfor %}

  
# -------------------------- #
#       METHOD ARGUMENTS     #
# -------------------------- #

arguments:
## The copy for these attributes lives in:
## _data/import-api/general.yml

  - name: "client_id"
    type: "integer"
    required: true
    description: |
      {{ general.attributes.client-id }}

      **Note**: This must be the same for every record in the request body. 
    example-value: "7723"

  - name: "table_name"
    type: "string"
    required: true
    description: "{{ general.attributes.table-name | flatify }}"
    example-value: "customers"

  - name: "sequence"
    type: "integer"
    required: true
    description: "{{ general.attributes.sequence | flatify }}"
    example-value: ""

  - name: "action"
    type: "string"
    required: true
    description: "This will always be `upsert`."
    example-value: "upsert"

  - name: "key_names"
    type: "array"
    required: true
    description: "{{ general.attributes.key-names | flatify }}"
    example-value: "id"

  - name: "data"
    type: "object"
    required: true
    description: "{{ general.attributes.data | flatify }}"


# -------------------------- #
#           RETURNS          #
# -------------------------- #

returns: |
  {% assign response-codes = site.data.import-api.response-codes.general-codes.all-codes %}

  If successful, the API will return a `2xx` status and a [Batch Status object]({{ site.data.import-api.api.data-structures.batch-status.section }}):

  {% for response-code in response-codes %}
  {% if response-code.code == "201" or response-code.code == "202" %}
  - `{{ response-code.code }}` - {{ response-code.description }}
  {% endif %}
  {% endfor %}


# ------------------------------ #
#   EXAMPLE REQUEST & RESPONSES  #
# ------------------------------ #

examples:
  - type: "Request"
    language: "json"
    subexamples:
      - type: "Pushing a single record for a single table"
        code: |
          {% capture request-header %}
          curl -X {{ endpoint.method | upcase }} {{ endpoint.full-url | flatify | strip_newlines }} \
               -H 'Authorization: Bearer <IMPORT_API_ACCESS_TOKEN>' \
               -H "Content-Type: application/json" \
               -d $
          {% endcapture %}

          {{ request-header | rstrip }}
                  '[
                    {
                      "client_id": 7723,
                      "table_name": "customers",
                      "sequence": 100,
                      "key_names": [
                        "id"
                      ],
                      "data": {
                        "id": 1,
                        "name": "Finn"
                      },
                      "action": "upsert"
                    }
                  ]'


      - type: "Pushing multiple records for a single table"
        code: |
          {{ request-header | rstrip }}
                  '[
                    {
                      "client_id": 7723,
                      "table_name": "customers",
                      "sequence": 106,
                      "data": {
                        "id": 4,
                        "name": "Beamo"
                      },
                      "key_names": [
                        "id"
                      ],
                      "action": "upsert"
                    },
                    {
                      "client_id": 7723,
                      "table_name": "customers",
                      "sequence": 107,
                      "key_names": [
                        "id"
                      ],
                      "data": {
                        "id": 5,
                        "name": "Ice King"
                      },
                      "action": "upsert"
                    }
                  ]'


      - type: "Pushing records for multiple tables"
        code: |
          {{ request-header | rstrip }}
                  '[
                    {
                      "client_id": 7723,
                      "table_name": "customers",
                      "sequence": 106,
                      "data": {
                        "id": 4,
                        "name": "Beamo"
                      },
                      "key_names": [
                        "id"
                      ],
                      "action": "upsert"
                    },
                    {
                      "client_id": 7723,
                      "table_name": "orders",
                      "sequence": 100,
                      "key_names": [
                        "order_id"
                      ],
                      "data": {
                        "order_id": 561,
                        "customer_id": 4
                      },
                      "action": "upsert"
                    }
                  ]'



  - type: "Response"
    language: "json"
    subexamples:
      - type: "201 Created"
        code: |
          {{ site.data.import-api.code-examples.responses.push-data.batch-created }}

      - type: "202 Accepted"
        code: |
          {{ site.data.import-api.code-examples.responses.push-data.batch-accepted }}

  - type: "Errors"
---