---
tap: "shopify"
version: "1"

name: "events"
doc-link: "https://shopify.dev/api/admin-rest/2022-01/resources/event#top"
singer-schema: "https://github.com/singer-io/tap-shopify/blob/master/tap_shopify/schemas/events.json"
description: |
  The `{{ table.name }}` table contains info about events in the shop.

replication-method: "Key-based Incremental"

api-method:
    name: "Retrieve a list of events"
    doc-link: "https://shopify.dev/api/admin-rest/2022-01/resources/event#get-events"

date-time: |
  The date and time in [ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601){:target="new"} when the [ITEM] was [ACTION].

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The event ID."

  - name: "created_at"
    type: "date-time"
    replication-key: true
    description: |
      {{ table.date-time | replace: "[ITEM]","event" | replace: "[ACTION]","created" }}

  - name: "body"
    type: "string"
    description: "A text field containing information about the event."

  - name: "path"
    type: "string"
    description: "The relative URL to the resource the event is for."

  - name: "message"
    type: "string"
    description: "The description of the event. It can contain HTML formatting."

  - name: "subject_id"
    type: "integer"
    description: "The ID of the resource that generated the event."

  - name: "subject_type"
    type: "string"
    description: "The type of the resource that generated the event"

  - name: "verb"
    type: "string"
    description: "The type of event that occurred."

  - name: "author"
    type: "string"
    description: "The author of the event."

  - name: "description"
    type: "string"
    description: "The description of the event."

  - name: "arguments"
    type: "string, array"
    description: "A certain event and its resources."
    subattributes:
        - name: "argument"
          type: "string"
---