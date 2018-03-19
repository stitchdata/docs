---
content-type: "api-object"
endpoint: "sessions"
order: 2

title: "Session"
description: "{{ api.core-objects.sessions.description }}"
endpoint-url: "/sessions"
version: "3"

object-attributes:
  - name: "ephemeral_token"
    type: "string"
    description: "{{ connect.common.attributes.ephemeral-token | flatify }}"
---