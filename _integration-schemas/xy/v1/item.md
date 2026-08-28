---
tap: "x-y"
version: "1.0"
key: "item"

name: "item"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-x-y/blob/master/tap_x_y/schemas/item.json"
description: ""

replication-method: |
  The `{{ table.name }}` table contains information about items in your {{ integration.display_name }} account.

api-method:
    name: ""
    doc-link: ""

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The item ID."
    foreign-key-id: "item-id"

  - name: "last_modified"
    type: "integer"
    description: "The time the item was last modified."
    replication-key: true

  - name: "archived"
    type: "boolean"
    description: ""
  - name: "brand_uri"
    type: "string"
    description: ""
  - name: "color_uri"
    type: "string"
    description: ""
  - name: "cover_media"
    type: "string"
    description: ""
  
  - name: "media_folder"
    type: "string"
    description: ""
  - name: "name"
    type: "string"
    description: ""
  - name: "size"
    type: "string"
    description: ""
  - name: "style_uri"
    type: "string"
    description: ""
  - name: "upc"
    type: "string"
    description: ""
---
