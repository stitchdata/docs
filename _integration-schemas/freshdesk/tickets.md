---
tap: "freshdesk"
# version:

name: "tickets"
doc-link: https://developers.freshdesk.com/api/#tickets
singer-schema:  https://github.com/singer-io/tap-freshdesk/blob/master/tap_freshdesk/schemas/tickets.json
description: |
  The `tickets` table contains info about the tickets in your {{ integration.display_name }} account.

  #### Custom Fields

  If applicable, Stitch will replicate custom fields related to `tickets` in {{ integration.display_name }}.

replication-method: "Key-based Incremental"
api-method:
  name: listAllTickets
  doc-link: https://developers.freshdesk.com/api/#tickets

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The ticket ID."
    foreign-key-id: "ticket-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the ticket was most recently updated."

  - name: "cc_emails"
    type: "array"
    description: "The email addresses added in the `cc` field of the ticket."
    subattributes:
      - name: "value"
        type: "string"
        description: "The email address added in the `cc` field of the ticket."

  - name: "type"
    type: "string"
    description: "The category/type of ticket."

  - name: "to_emails"
    type: "array"
    description: "Email addresses to which the ticket was originally sent."
    subattributes:
      - name: "value"
        type: "string"
        description: "The email address to which the ticket was originally sent."

  - name: "fwd_emails"
    type: "array"
    description: "Email addresses added while forwarding a ticket."
    subattributes:
      - name: "value"
        type: "string"
        description: "The email address that was added while forwarding a ticket."

  - name: "source"
    type: "number"
    description: "The channel through which the ticket was created."

  - name: "due_by"
    type: "date-time"
    description: "Denotes the due time of the ticket."

  - name: "company_id"
    type: "integer"
    description: "The ID of the company to which the ticket belongs."
    foreign-key-id: "company-id"

  - name: "responder_id"
    type: "integer"
    description: "The ID of the agent assigned to the ticket."
    foreign-key-id: "agent-id"

  - name: "priority"
    type: "number"
    description: "The priority of the ticket."

  - name: "deleted"
    type: "boolean"
    description: "Indicates if the ticket has been deleted/trashed."

  - name: "facebook_id"
    type: "string"
    description: "The Facebook ID of the requester."

  - name: "subject"
    type: "string"
    description: "The subject of the ticket."

  - name: "fr_due_by"
    type: "date-time"
    description: "The time when the first response is due."

  - name: "email"
    type: "string"
    description: "The email address of the requester."

  - name: "status"
    type: "number"
    description: "The status of the ticket."

  - name: "is_escalated"
    type: "boolean"
    description: "Indicates if the ticket has been escalated for any reason."

  - name: "reply_cc_emails"
    type: "array"
    description: "Email addresses added while responding to the ticket."
    subattributes:
      - name: "value"
        type: "string"
        description: "The email address added while responding to the ticket."

  - name: "description"
    type: "string"
    description: "The HTML content of the ticket."

  - name: "tags"
    type: "array"
    description: "The tags associated with the ticket."
    subattributes:
      - name: "value"
        type: "string"
        description: "The tag associated with the ticket."

  - name: "email_config_id"
    type: "integer"
    description: "The ID of the email config used for the ticket. Ex: `support@stitchdata.com`"

  - name: "phone"
    type: "string"
    description: "The phone number associated with the requester."

  - name: "description_text"
    type: "string"
    description: "The content of the ticket in plain text."

  - name: "requester_id"
    type: "integer"
    description: "The ID of the requester."

  - name: "name"
    type: "string"
    description: "The name of the requester."

  - name: "product_id"
    type: "integer"
    description: "The ID of the product associated with the ticket."
    # foreign-key-id: "product-id"

  - name: "fr_escalated"
    type: "boolean"
    description: "Indicates if the ticket has been escalated as a result of the first response time being breached."

  - name: "created_at"
    type: "date-time"
    description: "The time the ticket was created."

  - name: "spam"
    type: "boolean"
    description: "Indicates if the ticket has been marked as spam."

  - name: "twitter_id"
    type: "string"
    description: "The Twitter handle of the requester."

  - name: "group_id"
    type: "integer"
    description: "The ID of the group to which the ticket has been assigned."
    foreign-key-id: "group-id"
---