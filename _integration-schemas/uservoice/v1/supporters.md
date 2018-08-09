---
tap: "uservoice"
# version: "1.0"

name: "supporters"
doc-link: https://developer.uservoice.com/docs/api/v2/reference/#/Supporters
singer-schema: https://github.com/singer-io/tap-uservoice/blob/master/tap_uservoice/streams/supporters.py
description: |
  The `{{ table.name }}` table contains info about supporters, who are end users that are supporters of a suggestion.

replication-method: "Key-based Incremental"

api-method:
  name: List supporters
  doc-link: https://developer.uservoice.com/docs/api/v2/reference/#list-supporters

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The supporter ID."

  - name: "is_subscribed"
    type: "boolean"
    description: "If `true`, the supporter is subscribed to suggestion notifications."

  - name: "how"
    type: "string"
    description: ""

  - name: "channel"
    type: "string"
    description: ""

  - name: "requests_count"
    type: "integer"
    description: "The total number of requests on the suggestion associated with the supporter."

  - name: "comments_count"
    type: "integer"
    description: "The total number of comments on the suggestion made by the supporter."

  - name: "links"
    type: "object"
    description: ""
    object-attributes: 
      - name: "suggestion"
        type: "integer"
        description: "The ID of the suggestion associated with the supporter."
        foreign-key: true
        table: "suggestions"

      - name: "user"
        type: "integer"
        description: "The ID of the end user associated with the supporter."
        foreign-key: true
        table: "users"

      - name: "created_by"
        type: "integer"
        description: "The ID of the user who created the supporter."
        foreign-key: true
        table: "users"

      - name: "updated_by"
        type: "integer"
        description: "The ID of the user who last updated the supporter."
        foreign-key: true
        table: "users"
---