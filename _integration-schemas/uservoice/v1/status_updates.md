---
tap: "uservoice"
version: "1.0"

name: "status_updates"
doc-link: https://developer.uservoice.com/docs/api/v2/reference/#/status_updates
singer-schema: https://github.com/singer-io/tap-uservoice/blob/master/tap_uservoice/streams/status_updates.py
description: |
  The `{{ table.name }}` table contains info about admin changes to the statuses of suggestions.

replication-method: "Key-based Incremental"

api-method:
  name: List status updates
  doc-link: https://developer.uservoice.com/docs/api/v2/reference/#list-status-updates

attributes:
  - name: "id"
    type: "integer"
    foreign-key: true
    description: "The status update ID."
    foreign-key-id: "status-update-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the status update was last updated."

  - name: "created_at"
    type: "date-time"
    description: "The time the status update was created."

  - name: "body"
    type: "string"
    description: "If applicable, the admin's message to the subscriber."

  - name: "supporters_notified"
    type: "boolean"
    description: "If `true`, supporters were notified of the status update."

  - name: "notification_email_address"
    type: "string"
    description: "The email address status update notifications are sent to."

  - name: "mail_sent_count"
    type: "integer"
    description: "The number of emails sent as a result of the status update."

  - name: "mail_opened_count"
    type: "integer"
    description: "The number of status update emails that were opened."

  - name: "mail_clicked_count"
    type: "integer"
    description: "The number of status update emails that were clicked."

  - name: "links"
    type: "object"
    description: "Details about the status change, suggestion, and user associated with the change."
    subattributes: 
      - name: "suggestion"
        type: "integer"
        description: "The ID of the suggestion associated with the status change."
        foreign-key-id: "suggestion-id"

      - name: "user"
        type: "integer"
        description: "The ID of the user associated with the status change."
        foreign-key-id: "user-id"

      - name: "new_status"
        type: "integer"
        description: "The ID of the new status."
        foreign-key-id: "status-id"

      - name: "old_status"
        type: "integer"
        description: "The ID of the previous status."
        foreign-key-id: "status-id"
---