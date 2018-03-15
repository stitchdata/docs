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
short: "{{ api.core-objects.sessions.create.description }}"
description: "{{ api.core-objects.sessions.create.description }}"

returns: "A [Session object]({{ api.core-objects.sessions.object }})."

examples:
  - type: "request"
    language: ""
    code: |
      curl -X {{ endpoint.method | upcase }} {{ endpoint.full-url | flatify | strip_newlines }}
           -H "Authorization: Bearer <ACCESS_TOKEN>" 
           -H "Content-Type: application/json"

  - type: "response"
    language: "json"
    code: |
      {
        "ephemeral_token":"<EPHEMERAL_TOKEN>"
      }

---