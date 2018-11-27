---
# -------------------------- #
#      ENDPOINT DETAILS      #
# -------------------------- #

content-type: "api-endpoint"
endpoint: "destination-types"
key: "list-destination-types"
version: "4"


# -------------------------- #
#       METHOD DETAILS       #
# -------------------------- #

title: "List destination types"
method: "get"
short-url: |
  /v{{ endpoint.version }}{{ object.endpoint-url }}
full-url: |
  {{ api.base-url }}{{ endpoint.short-url | flatify }}
short: "{{ api.core-objects.destination-types.list.short }}"
description: "{{ api.core-objects.destination-types.list.description | flatify }}"


# -------------------------- #
#           RETURNS          #
# -------------------------- #

returns: |
  If successful, the API will return a status of <code class="api success">200 OK</code> and an array of [Destination Report Card objects]({{ api.data-structures.report-cards.destination.section }}), one for each supported destination `type`.


# ------------------------------ #
#   EXAMPLE REQUEST & RESPONSES  #
# ------------------------------ #

examples:
  - type: "request"
    language: "json"
    code: |
      curl -X {{ endpoint.method | upcase }} {{ endpoint.full-url | flatify | strip_newlines }}
           -H "Authorization: Bearer <ACCESS_TOKEN>" 
           -H "Content-Type: application/json"

  - type: "response"
    language: "json"
    code: |
      HTTP/1.1 200 OK
      Content-Type: application/json;charset=ISO-8859-1

---