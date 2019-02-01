---
# -------------------------- #
#      ENDPOINT DETAILS      #
# -------------------------- #

content-type: "api-endpoint"
endpoint: "destination-types"
key: "get-a-destination-type"
version: "4"


# -------------------------- #
#       METHOD DETAILS       #
# -------------------------- #

title: "Get a destination type"
method: "get"
short-url: |
  /v{{ endpoint.version }}{{ object.endpoint-url }}/{type}
full-url: |
  {{ api.base-url }}{{ endpoint.short-url | flatify }}
short: |
  {{ api.core-objects.destination-types.get.short }}
description: |
  {{ api.core-objects.destination-types.get.description | flatify }}


# -------------------------- #
#       METHOD ARGUMENTS     #
# -------------------------- #

arguments:
  - name: "type"
    required: true
    type: "string"
    description: |
      {{ connect.common.attributes.type-argument | replace: "[TYPE]","destination" | replace: "[TYPE-1]","s3" | replace: "[TYPE-2]","redshift" }}
    example-value:
      "snowflake"


# -------------------------- #
#           RETURNS          #
# -------------------------- #

returns: |
  If successful, the API will return a status of <code class="api success">200 OK</code> and a [Destination Report Card object]({{ api.data-structures.report-cards.destination.section }}) corresponding to `type`.


# ------------------------------ #
#   EXAMPLE REQUEST & RESPONSES  #
# ------------------------------ #

examples:
  - type: "Request"
    language: "json"
    code: |
      {% assign right-bracket = "}" %}
      curl -X {{ endpoint.method | upcase }} {{ endpoint.full-url | flatify | remove: right-bracket | replace:"{type","snowflake" | strip_newlines }}
           -H "Authorization: Bearer <ACCESS_TOKEN>" 
           -H "Content-Type: application/json"


  - type: "Response"
    language: "json"
    code: |
      HTTP/1.1 200 OK
      Content-Type: application/json;charset=ISO-8859-1
      
      {{ site.data.connect.code-examples.destination-report-cards.snowflake | remove: "+*" }}
---