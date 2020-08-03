---
# -------------------------- #
#      ENDPOINT DETAILS      #
# -------------------------- #

product-type: "import-api"
content-type: "api-endpoint"
endpoint: "validate"
key: "validate-request"
version: "2"


# -------------------------- #
#       METHOD DETAILS       #
# -------------------------- #

title: "Validate a push request"
method: "post"
short-url: |
  /v{{ object.version }}{{ object.endpoint-url | flatify }}
full-url: |
  {{ api.base-url }}{{ endpoint.short-url | flatify }}
short: "{{ api.core-objects.status.short | flatify }}"
description: |
  **Note**: With the exception of not persisting data, this endpoint is functionally identical to the [Push endpoint]({{ site.data.import-api.core-objects.push.anchor }}). The Validate endpoint will not work if a request body intended for the [Batch endpoint]({{ site.data.import-api.core-objects.batch.anchor }}) is sent.

  {{ site.data.import-api.core-objects.validate.description | flatify | markdownify }} 

  Regardless of whether the Import API is functional, this endpoint will never return a `503 Service Unavailable` response. Use the [Status endpoint]({{ site.data.import-api.core-objects.api-status.anchor }}) to determine if the Import API is experiencing issues.

request-body: |
  The request body should provide an array (batch) of records to be inserted into the pipeline that comply with the following:

  {% assign request-body-requirements = general.request-body-requirements.common | concat: general.request-body-requirements.push %}

  {% for requirement in request-body-requirements %}
  - {{ requirement | markdownify }}
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
    description: "{{ general.attributes.table-name }}"
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
    description: "{{ general.attributes.key-names }}"
    example-value: "id"

  - name: "data"
    type: "object"
    required: true
    description: "{{ general.attributes.data | flatify }}"


# -------------------------- #
#           RETURNS          #
# -------------------------- #

returns: |
  If successful, the API will return a `200 OK` status and a [Batch Status object]({{ site.data.import-api.data-structures.batch-status.section }}).


# ------------------------------ #
#   EXAMPLE REQUEST & RESPONSES  #
# ------------------------------ #

examples:
  - type: "Request"
    header: "{{ site.data.connect.request-headers.post.with-body }}"
    request-url: "{{ endpoint.short-url | flatify }}"
    code: |
      '[
         {
            "client_id":7723,
            "table_name":"customers",
            "sequence":1565881320,
            "key_names":[
               "id"
            ],
            "data":{
               "id":1,
               "name":"Finn"
            },
            "action":"upsert"
         }
      ]'

  - type: "Response"
    language: "json"
    code: |
      {{ site.data.import-api.code-examples.responses.validate-request }}

# This endpoint uses the same errors as the Push endpoint
# The list of those errors live in _data/import-api/response-codes/push.yml
  - type: "Errors"
    error-file: "push"
---