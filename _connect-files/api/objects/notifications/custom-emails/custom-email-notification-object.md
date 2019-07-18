---
# -------------------------- #
#        CONTENT TYPE        #
# -------------------------- #

content-type: "api-structure"
key: "custom-email-notification-object"

# -------------------------- #
#        OBJECT INFO         #
# -------------------------- #

title: "Custom Email Notification"
description: "{{ api.data-structures.notifications.custom-email.description | flatify }}"


# -------------------------- #
#      OBJECT ATTRIBUTES     #
# -------------------------- #

object-attributes:
  - name: "id"
    type: "integer"
    description: "The notification ID."
    value: |
      9

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

  - name: "email_address"
    type: "string"
    description: |
      The email address of the custom notification recipient.
    value: |
      stitch-custom-notification@yourdomain.com


examples:
  - code: |
      {
        "id": 21,
        "client_id": 116078,
        "email_address": "stitch-custom-notification@yourdomain.com",
        "created_at": "2019-07-16T17:35:25Z",
        "disabled_at": null
      }
---