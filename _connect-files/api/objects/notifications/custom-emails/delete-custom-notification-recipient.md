---
# -------------------------- #
#      ENDPOINT DETAILS      #
# -------------------------- #

content-type: "api-endpoint"
endpoint: "notifications"
key: "delete-custom-notification-recipient"
version: "1"


# -------------------------- #
#       METHOD DETAILS       #
# -------------------------- #

title: "Delete a custom email"
method: "delete"
short-url: |
  {{ api.core-objects.notifications.custom-emails.delete.name | flatify }}
full-url: |
  {{ api.base-url }}{{ endpoint.short-url | flatify }}
short: "{{ api.core-objects.notifications.custom-emails.delete.description }}"
description: |
  {{ api.core-objects.notifications.custom-emails.delete.description }}

  **Note**: To use this endpoint, your Stitch plan must include access to the [Custom notification list]({{ link.account.customize-notifications | prepend: site.baseurl }}) feature.


# -------------------------- #
#       METHOD ARGUMENTS     #
# -------------------------- #

arguments:
  - name: "id"
    required: true
    type: "path parameter"
    description: "A path parameter corresponding to the unique ID of the custom notification recipient to be deleted."
    example-value: |
      22

# -------------------------- #
#           RETURNS          #
# -------------------------- #

returns: |
  If successful, the API will return a status of <code class="api success">200 OK</code> and an array containing `1`, indicating that one custom notification recipient was successfully deleted.

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

  - type: "Responses"
    language: "json"
    code: |
      [
        1
      ]

  - type: "Errors"
    error-file: "custom-email-notifications"
  # The errors live in: _data/connect/response-codes/replication-jobs.yml
---