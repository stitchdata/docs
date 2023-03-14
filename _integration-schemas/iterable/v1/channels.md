---
tap: "iterable"
version: "1"
key: ""

name: "channels"
doc-link: https://api.iterable.com/api/docs#channels_channels
singer-schema: https://github.com/singer-io/tap-iterable/tree/master/tap_iterable/schemas/channels.json
description: |
  The **{{ table.name }}** table contains information about all channels within your {{ integration.display_name }} project.

replication-method: "Full Table"

api-method:
  name: "Get channels"
  doc-link: "https://api.iterable.com/api/docs#channels_channels"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The channel ID."
    foreign-key-id: "channel-id"

  - name: "channelType"
    type: "string"
    description: ""

  - name: "messageMedium"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: ""

---
