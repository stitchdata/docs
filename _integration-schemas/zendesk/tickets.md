---
tap: "zendesk"
version: "1.0"

name: "tickets"
doc-link: https://developer.zendesk.com/rest_api/docs/support/tickets
singer-schema: https://github.com/singer-io/tap-zendesk/blob/master/tap_zendesk/schemas/tickets.json
description: |
  The `{{ table.name }}` table contains info about the tickets in your {{ integration.display_name }} account. Tickets are the means through which your end users (customers) communicate with your {{ integration.display_name }} agents.

  **Note**: Retrieving ticket data requires {{ integration.display_name }} Admin permissions.

  #### Custom ticket fields {#custom-ticket-fields}

  Stitch's {{ integration.display_name }} integration will replicate all custom ticket fields.

replication-method: "Key-based Incremental"

api-method:
  name: Incremental ticket export
  doc-link: https://developer.zendesk.com/rest_api/docs/support/incremental_export#incremental-ticket-export

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The ticket ID."
    foreign-key-id: "ticket-id"

  - name: "updated_at"
    type: "date-time"
    description: "The time the ticket was last updated."
    replication-key: true

  - name: "organization_id"
    type: "integer"
    description: "The ID of the organization associated with the requester (`requester_id`)."
    foreign-key-id: "organization-id"

  - name: "requester_id"
    type: "integer"
    description: "The ID of the user who requested the ticket."
    foreign-key-id: "user-id"

  - name: "is_public"
    type: "boolean"
    description: "If `true`, the ticket contains public comments."

  - name: "description"
    type: "string"
    description: "The first comment on the ticket."

  - name: "follower_ids"
    type: "array"
    description: "The IDs of agents currently following the ticket."
    subattributes:
      - name: "value"
        type: "integer"
        description: "The ID of the agent currently following the ticket."
        foreign-key-id: "user-id"

  - name: "submitter_id"
    type: "integer"
    description: |
      The ID of the ticket submitter. Unless the ticket was created as a follow-up ticket, this will always be the ID of the first comment author.

      In the case of a follow-up ticket, the value of this field will be the ID of the user who created the ticket.
    foreign-key-id: "user-id"

  # - name: "generated_timestamp"
  #   type: "integer"
  #   description:

  - name: "brand_id"
    type: "integer"
    description: "**{{ integration.display_name }} Enterprise only.** The ID of the brand associated with the ticket."

  - name: "group_id"
    type: "integer"
    description: "The ID of the group the ticket is assigned to."
    foreign-key-id: "group-id"

  - name: "type"
    type: "string"
    description: |
      The ticket type. Possible values are:

      - `problem`
      - `incident`
      - `question`
      - `task`

  - name: "recipient"
    type: "string"
    description: "The original recipient email address of the ticket."

  - name: "collaborator_ids"
    type: "array"
    description: "The IDs of the collaborators currently CC'ed on the ticket."
    subattributes:
      - name: "value"
        type: "integer"
        description: "The ID of the collaborator currently CC'ed on the ticket."
        foreign-key-id: "user-id"

  - name: "tags"
    type: "array"
    description: "The tags associated with the ticket."
    subattributes:
      - name: "value"
        type: "string"
        description: "The tag associated with the ticket."
        foreign-key-id: "tag-id"

  - name: "has_incidents"
    type: "boolean"
    description: "If `true`, the ticket has been marked as a problem."

  - name: "created_at"
    type: "date-time"
    description: "The time the ticket was created."

  - name: "raw_subject"
    type: "string"
    description: "The dynamic content placeholder, if present, or the `subject` value, if not."

  - name: "status"
    type: "string"
    description: |
      The state of the ticket. Possible values are:

      - `new`
      - `open`
      - `pending`
      - `hold`
      - `solved`
      - `closed`

  - name: "custom_fields"
    type: "array"
    description: "The custom fields associated with the ticket."
    subattributes:
      - name: "id"
        type: "integer"
        description: "The ID of the custom ticket field."
        foreign-key-id: "ticket-field-id"

      - name: "value"
        type: "string"
        description: "The value of the custom field."

  - name: "url"
    type: "string"
    description: "The API URL of the ticket."

  - name: "allow_channelback"
    type: "boolean"
    description: "If `true`, channelback is enabled. Only applicable for channels framework tickets."

  - name: "due_at"
    type: "date-time"
    description: "For task tickets (`type: task`), the ISO 8601 date that the ticket is due."

  - name: "followup_ids"
    type: "array"
    description: "The IDs of the follow-ups created from the ticket. The IDs are only available once the ticket is closed (`status: closed`)."
    subattributes:
      - name: "value"
        type: "integer"
        description: "The ID of the follow-up created from the ticket."

  - name: "priority"
    type: "string"
    description: |
      The urgency with which the ticket should be addressed. Possible values are:

      - `urgent`
      - `high`
      - `normal`
      - `low`

  - name: "assignee_id"
    type: "integer"
    description: "The ID of the agent currently assigned to the ticket."
    foreign-key-id: "user-id"

  - name: "subject"
    type: "string"
    description: "The value of the subject field for the ticket."

  - name: "external_id"
    type: "string"
    description: "An ID that can be used to link the ticket to local (outside of {{ integration.display_name }}) records."

  - name: "via"
    type: "object"
    description: "Details about how the ticket was created."
    subattributes:
      - name: "source"
        type: "object"
        description: "Details about how the ticket was created."
        subattributes:
          - name: "from"
            type: "object"
            description: ""
            subattributes:
              - name: "name"
                type: "string"
                description: ""

              - name: "ticket_id"
                type: "integer"
                description: ""
                foreign-key-id: "ticket-id"

              - name: "address"
                type: "string"
                description: ""

              - name: "subject"
                type: "string"
                description: ""

          - name: "to"
            type: "object"
            description: ""
            subattributes:
              - name: "address"
                type: "string"
                description: ""

              - name: "name"
                type: "string"
                description: ""

          - name: "rel"
            type: "string"
            description: ""

      - name: "channel"
        type: "string"
        description: "The channel used to create the ticket. For example: `web`, `rule`, `mobile`"

  - name: "ticket_form_id"
    type: "integer"
    description: "**{{ integration.display_name }} Enterprise only**. The ID of the ticket form to render for the ticket."
    foreign-key-id: "ticket-form-id"

  - name: "sharing_agreement_ids"
    type: "array"
    description: "The IDs of the sharing agreements used for the ticket."
    subattributes:
      - name: "value"
        type: "integer"
        description: "The ID of the sharing agreement used for the ticket."

  - name: "email_cc_ids"
    type: "array"
    description: "The IDs of the email CCs associated with the ticket."
    subattributes:
      - name: "value"
        type: "integer"
        description: "The ID of the email CC associated with the ticket."
---