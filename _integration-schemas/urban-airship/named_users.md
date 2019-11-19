---
tap: "urban-airship"
version:

name: "named_users"
doc-link: http://docs.urbanairship.com/api/ua.html#named-users
singer-schema: https://github.com/singer-io/tap-urban-airship/blob/master/tap_urban_airship/schemas/named_users.json
description: |
  The `named_users` table contains info about named users, or individual consumers. These identifiers can be used to map CRM data to channels.

replication-method: "Full Table"
api-method:
  name: namedUsersListing
  doc-link: https://docs.urbanairship.com/api/ua/#api-named-users-listing

attributes:
  - name: "named_user_id"
    type: "string"
    primary-key: true
    description: "The named user ID."
    foreign-key-id: "named-user-id"

  - name: "tags"
    type: "array"
    description: "The tags applied to the named user."
    subattributes:
      - name: "value"
        type: "string"
        description: "The tag applied to the named user."

  - name: "channels"
    type: "array"
    description: "The channels associated with the named user."
    subattributes:
      - name: "value"
        type: "string"
        primary-key: true
        description: "The ID of the channel associated with the named user."
        foreign-key-id: "channel-id"
---