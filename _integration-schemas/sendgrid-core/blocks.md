---
tap: "sendgrid-core"

name: "blocks"
doc-link: https://sendgrid.com/docs/API_Reference/Web_API_v3/blocks.html#List-all-blocks-GET
singer-schema: https://github.com/singer-io/tap-sendgrid/blob/master/tap_sendgrid/schemas/blocks.json
description: |
  The `blocks` table contains info about the email addresses currently on your blocks list. There are several causes for blocked emails: A mail server IP address being on an ISP blacklist, blocked by an ISP, or if the receiving server flags the message content.

replication-method: "Key-based Incremental"

replication-key:
  name: "end_time"

api-method:
  name: "List all blocks"
  doc-link: "https://sendgrid.com/docs/API_Reference/Web_API_v3/blocks.html#List-all-blocks-GET"

attributes:
  - name: "email"
    type: "string"
    primary-key: true
    description: "The email address of the blocked email entry."

  - name: "created"
    type: "integer"
    description: "The Unix timestamp indicating when the email address was added to the blocks list."

  - name: "reason"
    type: "string"
    description: "An explanation for the reason of the block."

  - name: "status"
    type: "string"
    description: "The status of the block."
---