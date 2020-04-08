---
# -------------------------- #
#      ENDPOINT DETAILS      #
# -------------------------- #

product-type: "connect"
content-type: "api-endpoint"
endpoint: "notifications"
key: "create-hook-notification"
version: "1"


# -------------------------- #
#       METHOD DETAILS       #
# -------------------------- #

title: "Create a webhook"
method: "post"
short-url: |
  {{ api.core-objects.notifications.hooks.post.name | flatify }}
full-url: |
  {{ api.base-url }}{{ endpoint.short-url | flatify }}
short: "{{ api.core-objects.notifications.hooks.post.description }}"
description: |
  {{ api.core-objects.notifications.hooks.post.description }}
  **Note**: To use this endpoint, your Stitch plan must include access to the [Post-load hooks]({{ link.account.post-load-notifications | prepend: site.baseurl }}) feature.


# -------------------------- #
#       METHOD ARGUMENTS     #
# -------------------------- #

arguments:
  - name: "type"
    required: true
    type: "string"
    description: |
      The type of hook notification to be created. This must be `post_load`.
    example-value: |
      post_load

  - name: "config"
    required: true
    type: "object"
    description: "The configuration details of the hook."
    subattributes:
      - name: "url"
        required: true
        type: "string"
        description: "The webhook URL that Stitch should deliver hook notifications to."
        example-value: |
          https://hooks.zapier.com/hooks/catch/some/webhook/id


# -------------------------- #
#           RETURNS          #
# -------------------------- #

returns: |
  If successful, the API will return a status of <code class="api success">200 OK</code> and a single [Hook notification object]({{ api.data-structures.notifications.hook.section }}).


# ------------------------------ #
#   EXAMPLE REQUEST & RESPONSES  #
# ------------------------------ #

examples:
  - type: "Request"
    language: "json"
    code: |
      {% assign right-bracket = "}" %}curl -X {{ endpoint.method | upcase }} {{ endpoint.full-url | flatify | strip }} \
           -H "Authorization: Bearer <ACCESS_TOKEN>" \
           -H "Content-Type: application/json" \
           -d "{
                 "type":"post_load",
                 "config":{  
                    "url":"https://hooks.zapier.com/hooks/catch/some/webhook/id"
                 }
               }"

  - type: "Response"
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
        "created_at": "2019-07-17T17:30:37Z",
        "modified_at": "2019-07-17T17:30:37Z",
        "disabled_at": null
      }

  - type: "Errors"
    error-file: "hook-notifications"
  # The errors live in: _data/connect/response-codes/hook-notifications.yml
---