---
# -------------------------- #
#      ENDPOINT DETAILS      #
# -------------------------- #

product-type: "connect"
content-type: "api-endpoint"
endpoint: "notifications"
key: "delete-hook-notification"
version: "1"


# -------------------------- #
#       METHOD DETAILS       #
# -------------------------- #

title: "Delete a hook"
method: "delete"
short-url: |
  {{ site.data.connect.core-objects.notifications.hooks.delete.name | flatify }}
full-url: |
  {{ api.base-url }}{{ endpoint.short-url | flatify }}
short: "{{ site.data.connect.core-objects.notifications.hooks.delete.description }}"
description: |
  {{ site.data.connect.core-objects.notifications.hooks.delete.description }}
  **Note**: To use this endpoint, your Stitch plan must include access to the [Post-load hooks]({{ link.account.post-load-notifications | prepend: site.baseurl }}) feature.


# -------------------------- #
#       METHOD ARGUMENTS     #
# -------------------------- #

arguments:
  - name: "id"
    required: true
    type: "path parameter"
    description: "A path parameter corresponding to the unique ID of the hook notification to be deleted."
    example-value: |
      8


# -------------------------- #
#           RETURNS          #
# -------------------------- #

returns: |
  If successful, the API will return a status of <code class="api success">200 OK</code> and a `null` body.


# ------------------------------ #
#   EXAMPLE REQUEST & RESPONSES  #
# ------------------------------ #

examples:
  - type: "Request"
    request-url: |
      {% assign right-bracket = "}" %}{{ endpoint.short-url | flatify | replace: "{id","8" | remove: right-bracket | strip_newlines }}
    header: "{{ site.data.connect.request-headers.delete | flatify }}"
    code: ""

  - type: "Response"
    code: |
      null

  - type: "Errors"
    error-file: "hook-notifications"
  # The errors live in: _data/connect/response-codes/hook-notifications.yml
---