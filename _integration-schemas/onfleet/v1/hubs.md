---
tap: "onfleet"
version: "1.0"

name: "hubs"
doc-link: "http://docs.onfleet.com/docs/hubs"
singer-schema: "https://github.com/singer-io/tap-onfleet/blob/master/tap_onfleet/schemas/hubs.json"
description: |
  The `{{ table.name }}` table contains info about the hubs, or depots, for teams in your {{ integration.display_name }} account. A hub is the location from which all deliveries for a team's workers start.

replication-method: "Full Table"

api-method:
    name: "List hubs"
    doc-link: "http://docs.onfleet.com/docs/hubs#list-hubs"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The hub ID."
    foreign-key-id: "hub-id"

  - name: "address"
    type: "object"
    description: "The street address for the hub."
    subattributes:
      - name: "apartment"
        type: "string"
        description: "The apartment or unit for the address, if applicable."

      - name: "city"
        type: "string"
        description: "The city for the address."

      - name: "country"
        type: "string"
        description: "The country for the address."

      - name: "number"
        type: "string"
        description: "The street number for the address."

      - name: "postalCode"
        type: "string"
        description: "The postal code for the address."

      - name: "state"
        type: "string"
        description: "The state for the address."

      - name: "street"
        type: "string"
        description: "The street for the address."

  - name: "location"
    type: "array"
    description: "The coordinates of the hub's location."
    subattributes:
      - name: "value"
        type: "anything"
        description: ""

  - name: "name"
    type: "string"
    description: "The name of the hub."

  - name: "teams"
    type: "array"
    description: "A list of IDs for teams the hub is associated with."
    subattributes:
      - name: "value"
        type: "string"
        description: "The ID of the team the hub is associated with."
        foreign-key-id: "team-id"
---