---
# -------------------------- #
#      ENDPOINT DETAILS      #
# -------------------------- #

product-type: "import-api"
content-type: "api-endpoint"
endpoint: "batch"
key: "batch-data"
version: "2"


# -------------------------- #
#       METHOD DETAILS       #
# -------------------------- #

title: "Create a batch"
method: "post"
short-url: |
  /v{{ object.version }}{{ object.endpoint-url | flatify }}
full-url: |
  {{ api.base-url }}{{ endpoint.short-url | flatify }}
short: "{{ api.core-objects.push.short | flatify }}"
description: |
  Pushes a record or multiple records for a specified table to Stitch. Each request to this endpoint may only contain data for a single table.

  When data for a table is pushed for the first time, Stitch will create the table in the destination in the specified integration schema.

  How data is loaded during subsequent pushes depends on:

  1. **The loading behavior types used by the destination**. Stitch supports <a href="#" data-toggle="tooltip" data-original-title="{{ site.data.tooltips.upsert }}">Upsert</a> and <a href="#" data-toggle="tooltip" data-original-title="{{ site.data.tooltips.append-only }}">Append-Only</a> loading.
  2. **Whether the `key_names` property specifies Primary Key fields.** If Primary Keys aren't specified, data will be loaded using Append-Only loading.

  Refer to the [Understanding loading behavior guide]({{ link.destinations.storage.loading-behavior | prepend: site.baseurl }}) for more info and examples.

  #### Structuring request body data {#batch--structure-request-body-data}

  Refer to the [Structuring data for the Import API guide]({{ link.import-api.guides.structure-data | prepend: site.baseurl }}) for instructions and examples.

accepts-transit: false

request-body: |
  The request body must also comply with the following:

  {% assign request-requirements = general.request-body-requirements.common | concat: general.request-body-requirements.batch %}

  {% for requirement in request-requirements %}
  - {{ requirement | flatify | markdownify | replace:"[NAME]","batch" }}
  {% endfor %}

  
# -------------------------- #
#       METHOD ARGUMENTS     #
# -------------------------- #

arguments:
## The copy for these attributes lives in:
## _data/import-api/general.yml

  - name: "table_name"
    type: "string"
    required: true
    description: |
      {{ general.attributes.table-name | remove: "A single request can push data to multiple tables." }}
    example-value: "customers"

  # - name: "table_version"
  #   type: "integer"
  #   required: true
  #   description: "{{ general.attributes.table-version | flatify }}"
  #   examole-value: "1"

  - name: "schema"
    type: "object"
    sub-type: "schema"
    url: "{{ site.data.import-api.data-structures.schema.section }}"
    required: true
    description: |
      A [Schema object]({{ site.data.import-api.data-structures.schema.section }}) containing the JSON schema describing the record(s) in the [Message object's]({{ site.data.import-api.data-structures.message.section }}) `data` property.

      Records must conform to this schema or an error will be returned when the request is sent.
    example-value: ""

  - name: "messages"
    type: "array"
    sub-type: "message"
    url: "{{ site.data.import-api.data-structures.message.section }}"
    required: true
    description: |
      An array of [Message]({{ site.data.import-api.data-structures.message.section }}) objects, each representing a record to be upserted into the table.
    example-value: ""

  - name: "key_names"
    type: "array"
    required: false
    description: |
      An array of strings representing the Primary Key fields in the source table. Stitch use these Primary Keys to de-dupe data during loading. If not provided, the table will be loaded in an append-only manner.

      **Note**: If included, a value must be provided. However, it may be an empty list to indicate that the source table doesn't have a Primary Key.

      If fields are provided, they must adhere to the following:

      1. Each field in the list must be the name of a top-level property defined in the [Schema object]({{ site.data.import-api.data-structures.schema.section }}). Primary Key fields cannot be contained in an object or an array.
      2. Fields in the list may not be `null` in the source.
      3. If a field is a string, its value must be less than 256 characters.

      All fields included in `key_names` must be present in the [Schema object]({{ site.data.import-api.data-structures.schema.section }}) and every [Message object]({{ site.data.import-api.data-structures.message.section }}) in the request.
    example-value: "id"


# -------------------------- #
#           RETURNS          #
# -------------------------- #

returns: |
  {% assign response-codes = site.data.import-api.response-codes.general-codes.all-codes %}

  If successful, the API will return a `2xx` status and a [Batch status object]({{ site.data.import-api.data-structures.batch-status.section }}):

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
      - type: "Pushing a single record"
        code: |
          {% capture request-header %}
          curl -X {{ endpoint.method | upcase }} {{ endpoint.full-url | flatify | strip_newlines }} \
               -H 'Authorization: Bearer <IMPORT_API_ACCESS_TOKEN>' \
               -H "Content-Type: application/json" \
               -d $
          {% endcapture %}

          {{ request-header | rstrip }}
                    {
                      "table_name": "customers",
                      "schema": {
                        "properties": {
                          "id": {
                            "type": "integer"
                          },
                          "name": {
                            "type": "string"
                          },
                          "age": {
                            "type": "integer"
                          },
                          "has_magic": {
                            "type": "boolean"
                          }
                        }
                      },
                      "messages": [
                        {
                          "action": "upsert",
                          "sequence": 1565880017,
                          "data": {
                            "id": 1,
                            "name": "Finn",
                            "age": 15,
                            "has_magic": false
                          }
                        }
                      ],
                      "key_names": [
                        "id"
                      ]
                    }


      - type: "Pushing multiple records"
        code: |
          {{ request-header | rstrip }}
                    {
                       "table_name":"customers",
                       "schema":{
                          "properties":{
                             "id":{
                                "type":"integer"
                             },
                             "name":{
                                "type":"string"
                             },
                             "age":{
                                "type":"integer"
                             },
                             "has_magic":{
                                "type":"boolean"
                             }
                          }
                       },
                       "messages":[
                          {
                             "action":"upsert",
                             "sequence":1565881320,
                             "data":{
                                "id":2,
                                "name":"Jake",
                                "age":6,
                                "has_magic":true
                             }
                          },
                          {
                             "action":"upsert",
                             "sequence":1565838645,
                             "data":{
                                "id":3,
                                "name":"Bubblegum",
                                "age":17,
                                "has_magic":true
                             }
                          }
                       ],
                       "key_names":[
                          "id"
                       ]
                    }

      - type: "Pushing a record without a Primary Key"
        code: |
          {{ request-header | rstrip }}
                    {
                       "table_name":"customers_no_primary_keys",
                       "schema":{
                          "properties":{
                             "name":{
                                "type":"string"
                             },
                             "age":{
                                "type":"integer"
                             },
                             "has_magic":{
                                "type":"boolean"
                             }
                          }
                       },
                       "messages":[
                          {
                             "action":"upsert",
                             "sequence":1565881320,
                             "data":{
                                "name":"BMO",
                                "age":2,
                                "has_magic":false
                             }
                          }
                       ]
                    }

  - type: "Response"
    language: "json"
    subexamples:
      - type: "201 Created"
        code: |
          {{ site.data.import-api.code-examples.responses.batch-created }}

      - type: "202 Accepted"
        code: |
          {{ site.data.import-api.code-examples.responses.batch-accepted }}

  - type: "Errors"
---