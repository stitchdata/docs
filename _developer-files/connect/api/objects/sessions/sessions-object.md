---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

type: "connect"
content-type: "api-object"
endpoint: "sessions"
order: 2


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Session"
description: "{{ api.core-objects.sessions.description | flatify }}"
endpoint-url: "/sessions"


# -------------------------- #
#      AVAILABLE METHODS     #
# -------------------------- #

available-methods:
  - id: "create-a-session"
    title: "Create a session"
    method: "post"
    short: "{{ api.core-objects.sessions.create.short | flatify }}"


# -------------------------- #
#        VERSION INFO        #
# -------------------------- #

latest-version: "3"
versions:
  - number: "3"
    deprecated: false


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

object-attributes:
  - name: "ephemeral_token"
    type: "string"
    description: |
      {{ connect.common.attributes.ephemeral-token | flatify }}
---