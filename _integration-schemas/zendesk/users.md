---
tap: "zendesk"
version: "1"

name: "users"
doc-link: https://developer.zendesk.com/rest_api/docs/support/users
singer-schema: https://github.com/singer-io/tap-zendesk/blob/master/tap_zendesk/schemas/users.json
description: |
  The `{{ table.name }}` table contains info about the users associated with your {{ integration.display_name }} account. This includes agents, admins, and end-users (customers).

  **Note**: Retrieving user data requires {{ integration.display_name }} Admin permissions.

  #### Custom user fields {#customer-user-fields}

  Stitch's {{ integration.display_name }} integration will replicate any custom fields associated with user records.

  **Note**: Replicating user custom fields requires that you be on a Team, Professional, or Enterprise {{ integration.display_name }} plan.

replication-method: "Key-based Incremental"

api-method:
  name: "Incremental user export"
  doc-link: https://developer.zendesk.com/rest_api/docs/support/incremental_export#incremental-user-export

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The user's ID."
    foreign-key-id: "user-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the user was last updated."

  - name: "active"
    type: "boolean"
    description: |
      If `true`, the user is currently active.

      If `false`, the user has been deleted.

  - name: "alias"
    type: "string"
    description: "The user's alias, displayed to end users."

  - name: "chat_only"
    type: "boolean"
    description: "If `true`, the user is a chat-only agent."

  - name: "created_at"
    type: "date-time"
    description: "The time the user was created."

  - name: "custom_role_id"
    type: "integer"
    description: "**Zendesk Enterprise only.** The user's custom role ID, if they are an agent."

  - name: "default_group_id"
    type: "integer"
    description: "The ID of the user's default group."
    foreign-key-id: "group-id"

  - name: "details"
    type: "string"
    description: "Details about the user, such as an address."

  - name: "email"
    type: "string"
    description: "The user's primary email address."

  - name: "external_id"
    type: "string"
    description: "The user's ID from another system."

  - name: "last_login_at"
    type: "date-time"
    description: "The time the user last logged in."

  - name: "locale"
    type: "string"
    description: "The user's locale."

  - name: "locale_id"
    type: "integer"
    description: "The user's language identifier."

  - name: "name"
    type: "string"
    description: "The user's name."

  - name: "notes"
    type: "string"
    description: "Notes about the user."

  - name: "moderator"
    type: "boolean"
    description: "If `true`, the user has forum moderation capabilities."

  - name: "organization_id"
    type: "integer"
    description: "The ID of the organization the user is associated with."
    foreign-key-id: "organization-id"

  - name: "only_private_comments"
    type: "boolean"
    description: "If `true`, the user can only create private comments."

  - name: "permanently_deleted"
    type: "boolean"
    description: "If `true`, the user has been permanently deleted."

  - name: "phone"
    type: "string"
    description: "The user's phone number."

  - name: "photo"
    type: "object"
    description: "Details about the user's profile picture."
    subattributes:
      - name: "id"
        type: "integer"
        description: "The ID of the user's profile picture."

      - name: "height"
        type: "integer"
        description: "The pixel height of the user's photo."

      - name: "width"
        type: "integer"
        description: "The pixel width of the user's photo."

      - name: "url"
        type: "string"
        description: "The API URL associated with the user's photo."

      - name: "inline"
        type: "boolean"
        description: "If `true`, the attachment is excluded from the attachment list. Additionally, the attachment's URL can be referenced within the comment of a ticket."

      - name: "content_url"
        type: "string"
        description: "The full URL where the user's image file can be downloaded."

      - name: "content_type"
        type: "string"
        description: "The content type of the image file. For example: `image/png`"

      - name: "file_name"
        type: "string"
        description: "The file name of the user's photo."

      - name: "size"
        type: "integer"
        description: "The size of the user's image file, in bytes."

      # - name: "mapped_content_url"
      #   type: "string"
      #   description: 

      - name: "thumbnails"
        type: "object"
        description:
        subattributes:
          - name: "id"
            type: "integer"
            description: "The ID of the user's profile picture."

          - name: "height"
            type: "integer"
            description: "The pixel height of the user's photo."

          - name: "width"
            type: "integer"
            description: "The pixel width of the user's photo."

          - name: "url"
            type: "string"
            description: "The API URL associated with the user's photo."

          - name: "inline"
            type: "boolean"
            description: "If `true`, the attachment is excluded from the attachment list. Additionally, the attachment's URL can be referenced within the comment of a ticket."

          - name: "content_url"
            type: "string"
            description: "The full URL where the user's image file can be downloaded."

          - name: "content_type"
            type: "string"
            description: "The content type of the image file. For example: `image/png`"

          - name: "file_name"
            type: "string"
            description: "The file name of the user's photo."

          - name: "size"
            type: "integer"
            description: "The size of the user's image file, in bytes."

          # - name: "mapped_content_url"
          #   type: "string"
          #   description: 

  - name: "restricted_agents"
    type: "boolean"
    description: "If `true`, the user has restrictions. This will be `true` for agents and `false` for admins and unrestricted agents."

  - name: "role"
    type: "string"
    description: |
      The role of the user. Possible values are:

      - `agent`
      - `admin`
      - `end-user`

  - name: "role_type"
    type: "integer"
    description: |
      The user's role ID. Possible values are:

      - `0` - Custom agents
      - `1` - Light agents
      - `2` - Chat agents

  - name: "shared"
    type: "boolean"
    description: &shared "**For ticket sharing accounts.** If `true`, the user is a shared agent from a different Zendesk Support instance."

  - name: "shared_agent"
    type: "boolean"
    description: *shared

  - name: "shared_phone_number"
    type: "boolean"
    description: "If `true`, the phone number (`phone`) is a shared number."

  - name: "signature"
    type: "string"
    description: "The user's signature. Only `agent`s and `admin`s have signatures."

  - name: "suspended"
    type: "boolean"
    description: "If `true`, the user has been suspended. Tickets from suspended users are also suspended. Suspended users cannot sign into the end-user portal."

  - name: "tags"
    type: "array"
    description: "The IDs of the tags associated with the user."
    subattributes:
      - name: "value"
        type: "string"
        description: "The ID of the tag associated with the user."
        foreign-key-id: "tag-id"

  - name: "ticket_restriction"
    type: "string"
    description: |
      Indicates which tickets the user has access to. Possible values are:

      - `organization`
      - `groups`
      - `assigned`
      - `requested`
      - `null`

  - name: "time_zone"
    type: "string"
    description: "The user's timezone."

  - name: "two_factor_auth_enabled"
    type: "boolean"
    description: "If `true`, two factor authentication is enabled for the user."

  - name: "url"
    type: "string"
    description: "The API URL associated with the user."

  - name: "user_fields"
    type: "object"
    description: "The values of custom fields in the user's record. A column will be created for every custom field with at least one non-null value."
    subattributes:
      - name: "CUSTOM_FIELD_NAME"
        type: "varies"
        description: "The custom field. The name and data type of the custom field depend on the name and data type of the field in {{ integration.display_name }}."

  - name: "verified"
    type: "boolean"
    description: "If `true`, the user's primary identity has been verified."
---
