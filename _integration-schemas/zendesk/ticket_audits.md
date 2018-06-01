---
tap: "zendesk"
version: "1.0"

name: "ticket_audits"
doc-link: https://developer.zendesk.com/rest_api/docs/core/ticket_audits
singer-schema: https://github.com/singer-io/tap-zendesk/blob/master/tap_zendesk/schemas/ticket_audits.json
description: |
  **Note**: This table uses Append-Only Incremental Replication. This means that new audit records, or updates made to existing audits, are appended as new rows to the end of the table.

  The `ticket_audits` table contains info about the activity associated with a ticket. An audit is a history of all updates to a given ticket. When a ticket is updated in Zendesk, an audit record is created. Each audit represents a single update to a ticket.

  A single audit record may include multiple event types. For example: A ticket comment, satisfaction rating, and a change event. For a full list of Zendesk audit event types, [refer to Zendesk's documentation](https://developer.zendesk.com/rest_api/docs/core/ticket_audits#audit-events).

replication-method: "Append-Only Incremental"

api-method:
  name: List all ticket audits
  doc-link: https://developer.zendesk.com/rest_api/docs/core/ticket_audits#list-all-ticket-audits

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The ticket audit ID."

  - name: "created_at"
    type: "date-time"
    replication-key: true
    description: "The time the audit was created."

  - name: "author_id"
    type: "integer"
    description: "The ID of the user who created the audit."
    foreign-key: true

  - name: "ticket_id"
    type: "integer"
    description: "The ID of the ticket associated with the audit."
    foreign-key: true

# START METADATA OBJECT
  - name: "metadata"
    type: "object"
    description: "Metadata for the audit, custom, and system data."
    object-attributes:
      - name: "custom"
        type: 
        description: "[TODO]"

      - name: "trusted"
        type: "boolean"
        description: "[TODO]"

      - name: "notifications_suppressed_for"
        type: "array"
        description: "[TODO]"
        array-attributes:
          - name: "value"
            type: "integer"
            description: "[TODO]"

      - name: "flags"
        type: "array"
        description: "For `Comment` and `VoiceComment` events, the comment flags applied to the comment."
        array-attributes:
          - name: "value"
            type: "integer"
            description: |
              The value of the flag applied to the comment. [Refer to Zendesk's documentation for more info](https://developer.zendesk.com/rest_api/docs/core/ticket_comments#comment-flags).

              Possible values are:

              - `0` - Zendesk is unsure the comment should be trusted.
              - `2` - The comment author was not part of the conversation.
              - `3` - The comment author wasn't signed in when the comment was submitted.
              - `4` - The comment was automatically generated.
              - `5` - The attached file was rejected because it's too big.
              - `11` - The comment was submitted by the user on behalf of the author.

      - name: "flags_options"
        type: "object"
        description: "For `Comment` and `VoiceComment` events, additional information about the comment flags."
        object-attributes:
          - name: ""
            type: 
            description: "[TODO]"

  # START METADATA > SYSTEM OBJECT
      - name: "system"
        type: "object"
        description: "Metadata about the system of the user who created the audit."
        object-attributes:
          - name: "location"
            type: "string"
            description: "The user's location. For example: `Philadelphia, PA, United States`"

          - name: "longitude"
            type: "number"
            description: "The user's longitude."

          - name: "message_id"
            type: "string"
            description: 

          - name: "raw_email_identifier"
            type: "string"
            description: 

          - name: "ip_address"
            type: "string"
            description: "The user's IP address."

          - name: "json_email_identifier"
            type: "string"
            description: 

          - name: "client"
            type: "string"
            description: "The user's client, or web browser."

          - name: "latitude"
            type: "number"
            description: "The user's latitude."
  # END METADATA > SYSTEM OBJECT

# END METADATA OBJECT

# START EVENTS ARRAY
  - name: "events"
    type: "array"
    description: "The events that happened in the audit."
    array-attributes:
      - name: "id"
        type: "integer"
        description: "The audit event ID."

      - name: "audit_id"
        type: "integer"
        description: "The ticket audit ID."
        foreign-key: true

      - name: "type"
        type: "string"
        description: |
          The event type. Refer to [Zendesk's documentation](https://developer.zendesk.com/rest_api/docs/core/ticket_audits#audit-events) for a full list of event types.
        doc-link: "https://developer.zendesk.com/rest_api/docs/core/ticket_audits#audit-events"

      # - name: "macro_id"
      #   type: "string"
      #   description: ""
      #   foreign-key: true

      # - name: "macro_title"
      #   type: "string"
      #   description: 

      - name: "body"
        type: "string"
        description: |
          - For `VoiceComment` events - The comment added to the ticket.
          - For `Notification` events - The message sent to the recipients.
          - For `Cc` events - The message sent to the recipients.
          - For `SatisfactionRating` events - The user's comment posted during the rating.
          - For `OrganizationActivity` events - The message sent to the recipients.
          - For `Tweet` events - The body of the tweet.
          - For `FacebookEvent` events - The message posted to Facebook.
          - For `FacebookComment` events - The comment made by the author.
          - For `External` events - The trigger message for the target event.
          - For `LogMeInTranscript` events - The audit of the transcript.

      # - name: "macro_deleted"
      #   type: "boolean"
      #   description:

      - name: "plain_body"
        type: "string"
        description: |
          - For `VoiceComment` events - The comment in plaintext format.
          - For `FacebookComment` events - The comment in plaintext format.

      - name: "value"
        type: "string"
        description: |
          - For `Create` events - The value of the field that was set.
          - For `Change` events - The value of the field that was changed.

      - name: "author_id"
        type: "integer"
        description: |
          - For `VoiceComment` events - The comment author, typically the agent assigned to the ticket.
          - For `FacebookComment` events - The ID of the comment author.

      - name: "html_body"
        type: "string"
        description: |
          - For `VoiceComment` events - The comment in HTML format.
          - For `FacebookComment` events - The comment in HTML format.

      - name: "subject"
        type: "string"
        description: |
          - For `Notification` events - The subject of the message sent to recipients.
          - For `OrganizationActivity` events - The subject of the message sent to recipients.

      - name: "field_name"
        type: "string"
        description: |
          - For `Create` events - The name of the field that was set.
          - For `Change` events - The name of the field that was changed.
          - For `Push` events - The data being pushed out of Zendesk.

      - name: "public"
        type: "boolean"
        description: |
          - For `VoiceComment` events - If `true`, the ticket requester can see the comment. Otherwise, only agents can see it.
          - For `CommentPrivacyChange` events - If `true`, the comment was public.
          - For `FacebookComment` events - If `true`, the comment was public. Otherwise, only agents can see it.

      - name: "previous_value"
        type: "string"
        description: |
          Applicable to `Change` events. The previous value of the field that was changed.

          **Note**: This field may occasionally be an `array`, which will create a subtable in your destination if nested structures are unsupported. This occurs when the `field_name` value is `tags`. [Refer to Zendesk's documentation for more info](https://developer.zendesk.com/rest_api/docs/core/ticket_audits#change-event).

  # START RECIPIENTS
      - name: "recipients"
        type: "array"
        description: |
          For `Notification`, `Cc`, `OrganizationActivity`, and `Tweet` events, the IDs of the recipients.
        array-attributes:
          - name: "value"
            type: "integer"
            description: "The ID of the recipient."
  # END RECIPIENTS

  # START ATTACHMENTS OBJECT
      - name: "attachments"
        type: "object"
        description: |
          Details about the attachments associated with the event, if any.
        object-attributes:
          - name: "id"
            type: "integer"
            description: "The attachment ID."

          - name: "size"
            type: "integer"
            description: "The size of the attachment in bytes."

          - name: "url"
            type: "string"
            description: "The API URL associated with the attachment."

          - name: "inline"
            type: "boolean"
            description: "If `true`, the attachment is excluded from the attachment list. Additionally, the attachment's URL can be referenced within the comment of a ticket."

          - name: "height"
            type: "integer"
            description: "The height of the attachment, if applicable."

          - name: "width"
            type: "integer"
            description: "The width of the attachment, if applicable."

          - name: "content_url"
            type: "string"
            description: "The full URL where the attachment image file may be downloaded."

          - name: "mapped_content_url"
            type: "string"
            description: 

          - name: "content_type"
            type: "string"
            description: "The content type of the image. For example: `image/png`"

          - name: "file_name"
            type: "string"
            description: "The name of the image file."

          # - name: "html_body"
          #   type: "string"
          #   description: 

          # - name: "subject"
          #   type: "string"
          #   description:

          - name: "file_name"
            type: "string"
            description: "The name of the image file." 

      # START THUMBNAILS OBJECT
          - name: "thumbnails"
            type: "object"
            description: "Details about the thumbnails associated with image attachments."
            object-attributes:
              - name: "id"
                type: "integer"
                description:

              - name: "size"
                type: "integer"
                description:

              - name: "url"
                type: "string"
                description:

              - name: "inline"
                type: "boolean"
                description:

              - name: "height"
                type: "integer"
                description:

              - name: "width"
                type: "integer"
                description:

              - name: "content_url"
                type: "string"
                description:

              - name: "mapped_content_url"
                type: "string"
                description:

              - name: "content_type"
                type: "string"
                description:

              - name: "file_name"
                type: "string"
                description:
      # END THUMBNAILS

  # END ATTACHMENTS

  # START VIA OBJECT
      - name: "via"
        type: "object"
        description: "Details about how the event was created."
        object-attributes:
          - name: "channel"
            type: "string"
            description: "The channel used to create the event."

          - name: "source"
            type: "object"
            description: "Additional details about how the event was created."
            object-attributes: &source-attributes

          # START TO OBJECT
              - name: "to"
                type: "object"
                description: ""
                object-attributes:
                  - name: "address"
                    type: "string"
                    description: ""

                  - name: "name"
                    type: "string"
                    description:
          # END TO

          # START FROM OBJECT
              - name: "from"
                type: "object"
                description: ""
                object-attributes:
                  - name: "id"
                    type: "integer"
                    description: 

                  - name: "ticket_id"
                    type: "integer"
                    description:
                    foreign-key: true

                  - name: "revision_id"
                    type: "string"
                    description:

                  - name: "title"
                    type: "string"
                    description:

                  - name: "address"
                    type: "string"
                    description:

                  - name: "subject"
                    type: "string"
                    description:

                  - name: "deleted"
                    type: "boolean"
                    description:

                  - name: "name"
                    type: "string"
                    description:

                  - name: "original_recipients"
                    type: "array"
                    description:
                    array-attributes:
                      - name: "value"
                        type: "string"
                        description:
          # END FROM
              - name: "rel"
                type: "string"
                description:

  # END VIA

  - name: "via"
    type: "object"
    description: "Details about how the audit record was created."
    object-attributes:
      - name: "channel"
        type: "string"
        description: 

      - name: "source"
        type: "object"
        description:
        object-attributes: *source-attributes
---
