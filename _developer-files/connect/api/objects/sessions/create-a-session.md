---
# -------------------------- #
#      ENDPOINT DETAILS      #
# -------------------------- #

product-type: "connect"
content-type: "api-endpoint"
endpoint: "sessions"
key: "create-a-session"
version: "3"


# -------------------------- #
#       METHOD DETAILS       #
# -------------------------- #

title: "Create a session"
method: "post"
short-url: |
  /v{{ endpoint.version }}{{ object.endpoint-url }}/ephemeral
full-url: |
  {{ api.base-url }}{{ endpoint.short-url | flatify }}
short: "{{ api.core-objects.sessions.create.short }}"
description: |
  {{ api.core-objects.sessions.create.description | flatify }}


# -------------------------- #
#           RETURNS          #
# -------------------------- #

returns: |
  If successful, the API will return a status of <code class="api success">200 OK</code> and a [Session object]({{ api.core-objects.sessions.object }}).


# ------------------------------ #
#   EXAMPLE REQUEST & RESPONSES  #
# ------------------------------ #

examples:
  - type: "Request"
    language: "json"
    code: |
      curl -X {{ endpoint.method | upcase }} {{ endpoint.full-url | flatify | strip_newlines }} \
           -H "Authorization: Bearer <ACCESS_TOKEN>" \
           -H "Content-Type: application/json"

  - type: "Response"
    language: "json"
    code: |
      {
        "ephemeral_token":"<EPHEMERAL_TOKEN>"
      }
---