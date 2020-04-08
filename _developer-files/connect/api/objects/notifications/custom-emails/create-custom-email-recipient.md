---
# -------------------------- #
#      ENDPOINT DETAILS      #
# -------------------------- #

product-type: "connect"
content-type: "api-endpoint"
endpoint: "notifications"
key: "create-custom-notification-recipient"
version: "1"


# -------------------------- #
#       METHOD DETAILS       #
# -------------------------- #

title: "Create a custom email"
method: "post"
short-url: |
  {{ api.core-objects.notifications.custom-emails.post.name | flatify }}
full-url: |
  {{ api.base-url }}{{ endpoint.short-url | flatify }}
short: "{{ api.core-objects.notifications.custom-emails.post.description }}"
description: |
  {{ api.core-objects.notifications.custom-emails.post.description }}
  **Note**: To use this endpoint, your Stitch plan must include access to the [Custom notification list]({{ link.account.customize-notifications | prepend: site.baseurl }}) feature.
# -------------------------- #
#       METHOD ARGUMENTS     #
# -------------------------- #

arguments:
  - name: "email_address"
    required: true
    type: "string"
    description: |
      The email address that custom email notifications should be sent to.
    example-value: |
      stitch-custom-notification@yourdomain.com
# -------------------------- #
#           RETURNS          #
# -------------------------- #

returns: |
  If successful, the API will return a status of <code class="api success">200 OK</code> and a single [Custom Email Notification object]({{ api.data-structures.notifications.custom-email.section }}).
# ------------------------------ #
#   EXAMPLE REQUEST & RESPONSES  #
# ------------------------------ #

examples:
  - type: "Request"
    language: "json"
    code: |
      {% assign right-bracket = "}" %}
      curl -X {{ endpoint.method | upcase }} {{ endpoint.full-url | flatify | strip }} \
           -H "Authorization: Bearer <ACCESS_TOKEN>" \
           -H "Content-Type: application/json" \
           -d "{
                 "email_address": "stitch-custom-notification@yourdomain.com"
               }"
  - type: "Responses"
    language: "json"
    code: |
      {
        "id": 22,
        "client_id": 116078,
        "email_address": "stitch-custom-notification@yourdomain.com",
        "created_at": "2019-07-16T19:49:51Z",
        "disabled_at": null
      }
  - type: "Errors"
    error-file: "custom-email-notifications"
  # The errors live in: _data/connect/response-codes/custom-email-notifications.yml
---