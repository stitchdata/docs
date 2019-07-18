---
# -------------------------- #
#      ENDPOINT DETAILS      #
# -------------------------- #

content-type: "api-endpoint"
endpoint: "notifications"
key: "list-hook-notifications"
version: "1"


# -------------------------- #
#       METHOD DETAILS       #
# -------------------------- #

title: "List hook notifications"
method: "get"
short-url: |
  {{ api.core-objects.notifications.hooks.list.name | flatify }}
full-url: |
  {{ api.base-url }}{{ endpoint.short-url | flatify }}
short: "{{ api.core-objects.notifications.hooks.list.description }}"
description: |
  {{ api.core-objects.notifications.hooks.list.description }} This includes hooks that have been disabled.

  **Note**: To use this endpoint, your Stitch plan must include access to the [Post-load hooks]({{ link.account.post-load-notifications | prepend: site.baseurl }}) feature.


# -------------------------- #
#           RETURNS          #
# -------------------------- #

returns: |
  If successful, the API will return a status of <code class="api success">200 OK</code> and a `post_load` property containing an array of [Hook Notification objects]({{ api.data-structures.notifications.custom-email.section }}), one for each hook notification in the Stitch account.

# ------------------------------ #
#   EXAMPLE REQUEST & RESPONSES  #
# ------------------------------ #

examples:
  - type: "Request"
    language: "json"
    code: |
      {% assign right-bracket = "}" %}
      curl -X {{ endpoint.method | upcase }} {{ endpoint.full-url | flatify | strip }}
           -H "Authorization: Bearer <ACCESS_TOKEN>" 
           -H "Content-Type: application/json"

  - type: "Responses"
    language: "json"
    code: |
      {
        "post_load": [
          {
            "id": 8,
            "client_id": 116078,
            "type": "post_load",
            "version": 1,
            "config": {
              "url": "https://hooks.zapier.com/hooks/catch/some/webhook/id"
            },
            "created_at": "2019-07-16T16:47:54Z",
            "modified_at": "2019-07-16T16:47:54Z",
            "disabled_at": null
          },
          {
            "id": 9,
            "client_id": 116078,
            "type": "post_load",
            "version": 1,
            "config": {
              "url": "https://hooks.zapier.com/hooks/catch/some/webhook/id"
            },
            "created_at": "2019-07-16T16:51:20Z",
            "modified_at": "2019-07-16T16:51:20Z",
            "disabled_at": null
          },
          {
            "id": 10,
            "client_id": 116078,
            "type": "post_load",
            "version": 1,
            "config": {
              "url": "https://hooks.zapier.com/hooks/catch/some/webhook/id"
            },
            "created_at": "2019-07-17T15:54:25Z",
            "modified_at": "2019-07-18T15:36:53Z",
            "disabled_at": "2019-07-18T15:36:53Z"
          }
        ]
      }

  # - type: "Errors"
  #   error-file: "hook-notifications"
  # The errors live in: _data/connect/response-codes/hook-notifications.yml
---