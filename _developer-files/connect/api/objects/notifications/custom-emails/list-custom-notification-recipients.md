---
# -------------------------- #
#      ENDPOINT DETAILS      #
# -------------------------- #

product-type: "connect"
content-type: "api-endpoint"
endpoint: "notifications"
key: "list-custom-notification-recipients"
version: "1"


# -------------------------- #
#       METHOD DETAILS       #
# -------------------------- #

title: "List custom emails"
method: "get"
short-url: |
  {{ site.data.connect.core-objects.notifications.custom-emails.list.name | flatify }}
full-url: |
  {{ api.base-url }}{{ endpoint.short-url | flatify }}
short: "{{ site.data.connect.core-objects.notifications.custom-emails.list.description }}"
description: |
  {{ site.data.connect.core-objects.notifications.custom-emails.list.description }} This includes custom notification recipients that have been disabled.
  **Note**: To use this endpoint, your Stitch plan must include access to the [Custom notification list]({{ link.account.customize-notifications | prepend: site.baseurl }}) feature.


# -------------------------- #
#           RETURNS          #
# -------------------------- #

returns: |
  If successful, the API will return a status of <code class="api success">200 OK</code> and an array of [Custom Email Notification objects]({{ site.data.connect.data-structures.notifications.custom-email.section }}), one for each custom notification recipient.


# ------------------------------ #
#   EXAMPLE REQUEST & RESPONSES  #
# ------------------------------ #

examples:
  - type: "Request"
    request-url: "{{ endpoint.short-url | flatify | strip }}"
    header: "{{ site.data.connect.request-headers.get | flatify }}"
    code: ""

  - type: "Response"
    code: |
      [
        {
          "id": 22,
          "client_id": 116078,
          "email_address": "stitch-custom-notification@stitchdata.com",
          "created_at": "2019-07-16T19:49:51Z",
          "disabled_at": null
        },
        {
          "id": 23,
          "client_id": 116078,
          "email_address": "another-custom-notification@stitchdata.com",
          "created_at": "2019-07-16T20:43:51Z",
          "disabled_at": null
        }
      ]

  # - type: "Errors"
  #   error-file: "custom-email-notifications"
  # The errors live in: _data/connect/response-codes/custom-email-notifications.yml
---