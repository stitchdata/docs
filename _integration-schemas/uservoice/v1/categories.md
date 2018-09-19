---
tap: "uservoice"
# version: "1.0"

name: "categories"
doc-link: https://developer.uservoice.com/docs/api/v2/reference/#/categories
singer-schema: https://github.com/singer-io/tap-uservoice/blob/master/tap_uservoice/streams/categories.py
description: |
  The `{{ table.name }}` contains info about the various categories in your {{ integration.display_name }} account. Categories are used to organize suggestions in a forum.

replication-method: "Key-based Incremental"

api-method:
  name: List categories
  doc-link: https://developer.uservoice.com/docs/api/v2/reference/#list-categories
attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The category ID."
    foreign-key-id: "category-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the category was last updated."

  - name: "created_at"
    type: "date-time"
    description: "The time the category was created."

  - name: "name"
    type: "string"
    description: "The name of the category."

  - name: "suggestions_count"
    type: "integer"
    description: "The total number of suggestions associated with the category."

  - name: "open_suggestions_count"
    type: "integer"
    description: "The total number of open suggestions associated with the category."

  - name: "links"
    type: "object"
    description: "Details about the links associated with the category."
    object-attributes: 
      - name: "forum"
        type: "integer"
        description: "The ID of the forum associated with the category."
        foreign-key-id: "forum-id"
---