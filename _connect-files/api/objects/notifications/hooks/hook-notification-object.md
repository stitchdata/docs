---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

content-type: "api-structure"
key: "hook-notification-object"

# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Hook Notification"
description: "{{ api.data-structures.notifications.hook.description | flatify }}"


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

object-attributes:
  - name: "id"
    type: "integer"
    description: "The notification ID."
    value: |
      21

  - name: "client_id"
    type: "integer"
    description: "The ID of the Stitch client account."
    value: |
      116078

  - name: "created_at"
    type: "date-time"
    description: "The time at which the notification was created."
    value: |
      2019-07-16T16:51:20Z

  - name: "modified_at"
    type: "date-time"
    description: "The time at which the notification was last modified."
    value: |
      2019-07-16T16:51:20Z

  - name: "disabled_at"
    type: "date-time"
    description: |
      The time at which the notification was disabled. This will be `null` unless the notification has been disabled.
    value: |
      null

  - name: "type"
    type: "string"
    description: |
      The type of the notification. Possible values are:

      - `post_load`
    value: |
      post_load

  - name: "version"
    type: "integer"
    description: |
      The version of the hook service the notification is using.
    value: |
      1

  - name: "config"
    type: "object"
    description: |
      The configuration for the hook.
    subattributes:
      - name: "url"
        type: "string"
        description: "The webhook URL that Stitch should deliver hook notifications to."
        value: |
          https://hooks.zapier.com/hooks/catch/some-hook-id

examples:
  - code: |
      {
        "id": 9,
        "client_id": 116078,
        "type": "post_load",
        "version": 1,
        "config": {
          "url": "https://hooks.zapier.com/hooks/catch/some-hook-id"
        },
        "created_at": "2019-07-16T16:51:20Z",
        "modified_at": "2019-07-16T16:51:20Z",
        "disabled_at": null
      }
---