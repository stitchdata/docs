---
# -------------------------- #
#      ENDPOINT DETAILS      #
# -------------------------- #

content-type: "api-endpoint"
endpoint: "streams"
key: "list-streams"
version: "4"


# -------------------------- #
#       METHOD DETAILS       #
# -------------------------- #

title: "List streams for a source"
method: "get"
short-url: |
  /v{{ endpoint.version }}{{ object.endpoint-url }}
full-url: |
  {{ api.base-url }}{{ endpoint.short-url | flatify }}
short: "{{ api.core-objects.streams.list.description }}"
description: "{{ api.core-objects.streams.list.description }}"


# -------------------------- #
#           RETURNS          #
# -------------------------- #

returns: |
  If successful, the API will return a status of <code class="api success">200 OK</code> and an array of [Source Objects]({{ api.core-objects.sources.object }}).


# ------------------------------ #
#   EXAMPLE REQUEST & RESPONSES  #
# ------------------------------ #

examples:
  - type: "Request"
    language: "json"
    code: |
      curl -X {{ endpoint.method | upcase }} {{ endpoint.full-url | flatify | strip_newlines }}
           -H "Authorization: Bearer <ACCESS_TOKEN>" 
           -H "Content-Type: application/json"

  - type: "Response"
    language: "json"
    code: |

---