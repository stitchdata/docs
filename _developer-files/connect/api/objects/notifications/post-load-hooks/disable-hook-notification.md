---
# -------------------------- #
#      ENDPOINT DETAILS      #
# -------------------------- #

product-type: "connect"
content-type: "api-endpoint"
endpoint: "notifications"
key: "disable-hook-notification"
version: "1"


# -------------------------- #
#       METHOD DETAILS       #
# -------------------------- #

title: "Disable a webhook"
method: "put"
short-url: |
  {{ api.core-objects.notifications.hooks.disable.name | flatify }}
full-url: |
  {{ api.base-url }}{{ endpoint.short-url | flatify }}
short: "{{ api.core-objects.notifications.hooks.disable.description }}"
description: |
  {{ api.core-objects.notifications.hooks.disable.description }}
  **Note**: To use this endpoint, your Stitch plan must include access to the [Post-load hooks]({{ link.account.post-load-notifications | prepend: site.baseurl }}) feature.


# -------------------------- #
#       METHOD ARGUMENTS     #
# -------------------------- #

arguments:
  - name: "id"
    required: true
    type: "path parameter"
    description: "A path parameter corresponding to the unique ID of the hook notification to be paused."
    example-value: |
      8

  - name: "enable"
    required: true
    type: "boolean"
    description: |
      Controls whether a hook notification is active or not. **To disable a hook**, this value must be `false`.
    example-value: |
      false


# -------------------------- #
#           RETURNS          #
# -------------------------- #

returns: |
  If successful, the API will return a status of <code class="api success">200 OK</code> and a single [Hook notification object]({{ api.data-structures.notifications.hook.section }}) with a populated `disabled_at` property.


# ------------------------------ #
#   EXAMPLE REQUEST & RESPONSES  #
# ------------------------------ #

examples:
  - type: "Request"
    language: "json"
    code: |
      {% assign right-bracket = "}" %}
      curl -X {{ endpoint.method | upcase }} {{ endpoint.full-url | flatify | replace: "{id","8" | remove: right-bracket | strip_newlines }}
           -H "Authorization: Bearer <ACCESS_TOKEN>" 
           -H "Content-Type: application/json"
           -d "{
                 "enable":false
               }"

  - type: "Responses"
    language: "json"
    code: |
      {
        "id": 8,
        "client_id": 116078,
        "type": "post_load",
        "version": 1,
        "config": {
          "url": "https://hooks.zapier.com/hooks/catch/some/webhook/id"
        },
        "created_at": "2019-07-16T16:47:54Z",
        "modified_at": "2019-07-17T16:04:29Z",
        "disabled_at": "2019-07-17T16:04:29Z"
      }

  - type: "Errors"
    error-file: "hook-notifications"
  # The errors live in: _data/connect/response-codes/hook-notifications.yml
---