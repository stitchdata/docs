---
tap: "urban-airship"
# version: "1.0"

name: "channels"
doc-link: http://docs.urbanairship.com/api/ua.html#channels
singer-schema: https://github.com/singer-io/tap-urban-airship/blob/master/tap_urban_airship/schemas/channels.json
description: |
  The `{{ table.name }}` table contains info about the channels - or unique identifiers - used to address applications on iOS, Android, and Amazon devices.

replication-method: "Key-based Incremental"
api-method:
  name: channelListing
  doc-link: https://docs.urbanairship.com/api/ua/#channel-list-api

attributes:
  - name: "channel_id"
    type: "integer"
    primary-key: true
    description: "The channel ID."
    foreign-key-id: "channel-id"

  - name: "created"
    type: "date-time"
    replication-key: true
    description: "The date the channel was created."

  - name: "last_registration"
    type: "date-time"
    replication-key: true
    description: "The last registration date of the channel, if known."

  - name: "device_type"
    type: "string"
    description: |
      The platform type of the channel. Possible values:

      - `ios`
      - `android`
      - `amazon`
      - `web`

  - name: "installed"
    type: "boolean"
    description: "Indicates if the channel is installed."

  - name: "background"
    type: "boolean"
    description: "Indicates if the device associated with the channel has background app refresh enabled."

  - name: "opt_in"
    type: "boolean"
    description: "Indicates if the channel is opted-in to push."

  - name: "push_addresses"
    type: "string"
    description: "The address to send the push."

  - name: "named_user_id"
    type: "string"
    description: "A customer-chosen ID that represents the device user."
    foreign-key-id: "named-user-id"

  - name: "alias"
    type: "string"
    description: "The alias associated with the channel. This field has been deprecated by Urban Airship."

  - name: "tags"
    type: "array"
    description: "A list of tags associated with the channel."
    subattributes:
      - name: "value"
        type: "string"
        description: "The tag associated with the channel."

  - name: "tag_groups"
    type: "array"
    description: "Details about the customer-created tag groups and device property tags associated with the channel."
    subattributes:
      - name: "name"
        type: "string"
        description: "The name of the tag group."

      - name: "tags"
        type: "array"
        description: "Details about the tags associated with the tag group."
        subattributes:
          - name: "value"
            type: "string"
            description: "The tag associated with the tag group."

  - name: "ios"
    type: "object"
    description: "Details about iOs-specific parameters."
    subattributes:
      - name: "badge"
        type: "string"
        description: "The current badge value."

      - name: "quiettime"
        type:  "object"
        description: "Details about quiet time iOS parameters."
        subattributes:
          - name: "start"
            type: "string"
            description: "The start of quiet time."

          - name: "end"
            type: "string"
            description: "The end of quiet time."

      - name: "tz"
        type: "string"
        description: "The timezone associated with the iOS device."
---