---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

content-type: "api-object"
endpoint: "sessions"
order: 2


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Session"
endpoint-url: "/sessions"

description: "{{ api.core-objects.sessions.description | flatify }}"
intro-short: "Access Stitch client accounts" # Used in the API functionality section of the docs

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