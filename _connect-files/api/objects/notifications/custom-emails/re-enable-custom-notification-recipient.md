---
# -------------------------- #
#      ENDPOINT DETAILS      #
# -------------------------- #

content-type: "api-endpoint"
endpoint: "notifications"
key: "enable-custom-notification-recipient"
version: "1"


# -------------------------- #
#       METHOD DETAILS       #
# -------------------------- #

title: "Re-enable a custom email"
method: "put"
short-url: |
  {{ api.core-objects.notifications.custom-emails.re-enable.name | flatify }}
full-url: |
  {{ api.base-url }}{{ endpoint.short-url | flatify }}
short: "{{ api.core-objects.notifications.custom-emails.re-enable.description }}"
description: |
  {{ api.core-objects.notifications.custom-emails.re-enable.description }}

  **Note**: To use this endpoint, your Stitch plan must include access to the [Custom notification list]({{ link.account.customize-notifications | prepend: site.baseurl }}) feature.


# -------------------------- #
#       METHOD ARGUMENTS     #
# -------------------------- #

arguments:
  - name: "id"
    required: true
    type: "path parameter"
    description: "A path parameter corresponding to the unique ID of the custom notification recipient to be re-enabled."
    example-value: |
      22

  - name: "disabled_at"
    required: true
    type: "null"
    description: |
      **To re-enable a custom notification recipient**, this value must be `null`.
    example-value: |
      null


# -------------------------- #
#           RETURNS          #
# -------------------------- #

returns: |
  If successful, the API will return a status of <code class="api success">200 OK</code> and single object with a `disabled_at` property with a `null` value.

# ------------------------------ #
#   EXAMPLE REQUEST & RESPONSES  #
# ------------------------------ #

examples:
  - type: "Request"
    language: "json"
    code: |
      {% assign right-bracket = "}" %}
      curl -X {{ endpoint.method | upcase }} {{ endpoint.full-url | flatify | replace: "{id","22" | remove: right-bracket | strip_newlines }}
           -H "Authorization: Bearer <ACCESS_TOKEN>" 
           -H "Content-Type: application/json"
           -d "{
                 "disabled_at": null
               }"

  - type: "Responses"
    language: "json"
    code: |
      {
        "disabled_at": null
      }

  - type: "Errors"
    error-file: "custom-email-notifications"
  # The errors live in: _data/connect/response-codes/replication-jobs.yml
---