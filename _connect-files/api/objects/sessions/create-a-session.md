---
content-type: "api-endpoint"
endpoint: "sessions"
key: "create-a-session"
version: "3"
order: 1


title: "Create a session"
method: "post"
short-url: |
  /v{{ object.version }}{{ object.endpoint-url }}/ephemeral
full-url: |
  {{ api.base-url }}{{ endpoint.short-url | flatify }}
short: "{{ api.core-objects.sessions.create.short }}"
description: |
  {{ api.core-objects.sessions.create.description | flatify }}

returns: |
  If successful, the API will return a status of <code class="api success">200 OK</code> and a [Session object]({{ api.core-objects.sessions.object }}).

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

      {
        "ephemeral_token":"<EPHEMERAL_TOKEN>"
      }

---