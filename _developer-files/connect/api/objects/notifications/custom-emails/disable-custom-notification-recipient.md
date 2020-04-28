---
# -------------------------- #
#      ENDPOINT DETAILS      #
# -------------------------- #

product-type: "connect"
content-type: "api-endpoint"
endpoint: "notifications"
key: "disable-custom-notification-recipient"
version: "1"


# -------------------------- #
#       METHOD DETAILS       #
# -------------------------- #

title: "Disable a custom email"
method: "put"
short-url: |
  {{ site.data.connect.core-objects.notifications.custom-emails.disable.name | flatify }}
full-url: |
  {{ api.base-url }}{{ endpoint.short-url | flatify }}
short: "{{ site.data.connect.core-objects.notifications.custom-emails.disable.description }}"
description: |
  {{ site.data.connect.core-objects.notifications.custom-emails.disable.description }}
  **Note**: To use this endpoint, your Stitch plan must include access to the [Custom notification list]({{ link.account.customize-notifications | prepend: site.baseurl }}) feature.

# -------------------------- #
#       METHOD ARGUMENTS     #
# -------------------------- #

arguments:
  - name: "id"
    required: true
    type: "path parameter"
    description: "A path parameter corresponding to the unique ID of the custom notification recipient to be paused."
    example-value: |
      22

  - name: "disabled_at"
    required: true
    type: "timestamp"
    description: |
      The time the custom notification was paused. This field must contain an [ISO 8601-compliant](https://en.wikipedia.org/wiki/ISO_8601){:target="new"} date.
      **Note**: Providing any value - past, present, or future - for this property will pause the custom notification recipient immediately if the request is successful.
    example-value: |
      "2019-06-01T00:00:00Z"

# -------------------------- #
#           RETURNS          #
# -------------------------- #

returns: |
  If successful, the API will return a status of <code class="api success">200 OK</code> and single object with a `disabled_at` property.


# ------------------------------ #
#   EXAMPLE REQUEST & RESPONSES  #
# ------------------------------ #

examples:
  - type: "Request"
    request-url: |
      {% assign right-bracket = "}" %}{{ endpoint.short-url | flatify | replace: "{id","22" | remove: right-bracket | strip_newlines }}
    header: "{{ site.data.connect.request-headers.put.with-body | flatify }}"
    code: |
      '{
         "disabled_at": "2019-06-01T00:00:00Z"
       }'

  - type: "Response"
    language: "json"
    code: |
      {
        "disabled_at": "2019-06-01T00:00:00Z"
      }

  - type: "Errors"
    error-file: "custom-email-notifications"
  # The errors live in: _data/connect/response-codes/custom-email-notifications.yml
---