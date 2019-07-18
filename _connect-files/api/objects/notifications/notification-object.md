---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

content-type: "api-object"
endpoint: "notifications"
order: 10


# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Notification"
endpoint-url: "/notifications/public/v1/api"

description: |
  {{ api.core-objects.notifications.description | flatify }} This applies to the [Custom email notification list]({{ link.account.customize-notifications | prepend: site.baseurl }}) and [Post-load hook]({{ link.account.post-load-notifications | prepend: site.baseurl }}) features.

intro-short: "Create, pause, unpause, and delete notification settings for a Stitch client account" # Used in the API functionality section of the docs


# -------------------------- #
#        VERSION INFO        #
# -------------------------- #

latest-version: "1"
versions:
  - number: "1"
    deprecated: false


# -------------------------- #
#      AVAILABLE METHODS     #
# -------------------------- #

available-methods:
  - id: "create-custom-notification-recipient"
    title: "Create a custom email"
    method: "post"
    short: "{{ api.core-objects.notifications.custom-emails.post.description | flatify }}"

  - id: "disable-custom-notification-recipient"
    title: "Disable a custom email"
    method: "put"
    short: "{{ api.core-objects.notifications.custom-emails.disable.description | flatify }}"

  - id: "enable-custom-notification-recipient"
    title: "Re-enable a custom email"
    method: "put"
    short: "{{ api.core-objects.notifications.custom-emails.re-enable.description | flatify }}"

  - id: "list-custom-notification-recipients"
    title: "List custom emails"
    method: "get"
    short: "{{ api.core-objects.notifications.custom-emails.list.description | flatify }}"

  - id: "delete-custom-notification-recipient"
    title: "Delete a custom email"
    method: "delete"
    short: "{{ api.core-objects.notifications.custom-emails.delete.description | flatify }}"

  - id: "create-hook-notification"
    title: "Create a webhook"
    method: "post"
    short: "{{ api.core-objects.notifications.hooks.post.description | flatify }}"

  - id: "disable-hook-notification"
    title: "Disable a webhook"
    method: "put"
    short: "{{ api.core-objects.notifications.hooks.disable.description | flatify }}"

  - id: "enable-hook-notification"
    title: "Re-enable a webhook"
    method: "put"
    short: "{{ api.core-objects.notifications.hooks.re-enable.description | flatify }}"

  - id: "list-hook-notifications"
    title: "List webhooks"
    method: "get"
    short: "{{ api.core-objects.notifications.hooks.list.description | flatify }}"

  - id: "delete-hook-notification"
    title: "Delete a webhook"
    method: "delete"
    short: "{{ api.core-objects.notifications.hooks.delete.description | flatify }}"



# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

object-attributes:
  - name: "id"
    type: "integer"
    description: "The notification ID."
    example-value: |
      9

  - name: "client_id"
    type: "integer"
    description: "The ID of the Stitch client account."
    example-value: |
      116078

  - name: "created_at"
    type: "date-time"
    description: "The time at which the notification was created."
    example-value: |
      2019-07-16T16:51:20Z

  - name: "modified_at"
    type: "date-time"
    description: "The time at which the notification was last modified."
    example-value: |
      2019-07-16T16:51:20Z

  - name: "disabled_at"
    type: "date-time"
    description: |
      The time at which the notification was disabled. This will be `null` unless the notification has been disabled.
    example-value: |
      null

  - name: "email_address"
    type: "string"
    description: |
      **Applicable to custom email notifications only.** The email address of the custom notification recipient.
    example-value: |
      stitch-custom-notification@yourdomain.com

  - name: "version"
    type: "integer"
    description: |
      **Applicable to custom email notifications only.** The version of the hook service the notification is using.
    example-value: |
      1

  - name: "type"
    type: "string"
    description: |
      **Applicable to hook notifications only.** The type of the notification.
    example-value: |
      post_load

  - name: "config"
    type: "object"
    description: "**Applicable to hook notifications only.** The configuration for the hook."
    subattributes:
      - name: "url"
        type: "string"
        description: "**Applicable to hook notifications only.** The webhook URL that Stitch should deliver hook notifications to."
        example-value: |
          https://hooks.zapier.com/hooks/catch/some-hook-id
---