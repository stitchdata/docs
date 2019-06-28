---
tap: "asana"
version: "1.0"
key: "user"

name: "users"
doc-link: "https://asana.com/developers/api-reference/users"
singer-schema: "https://github.com/singer-io/tap-asana/blob/master/tap_asana/schemas/users.json"
description: |
  The `{{ table.name }}` table contains info about the users in your {{ integration.display_name }} account.

replication-method: "Full Table"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The user ID."
    foreign-key-id: "user-id"

  - name: "email"
    type: "string"
    description: "The user's email address."

  - name: "name"
    type: "string"
    description: "The name of the user."

  - name: "photo"
    type: "object"
    description: "A map of the user's profile photo in various sizes."
    subattributes:
      - name: "image_1024x1024"
        type: "string"
        description: "The URL of the user's profile photo at size 1024x1024."

      - name: "image_128x128"
        type: "string"
        description: "The URL of the user's profile photo at size 128x128."

      - name: "image_21x21"
        type: "string"
        description: "The URL of the user's profile photo at size 21x21."

      - name: "image_27x27"
        type: "string"
        description: "The URL of the user's profile photo at size 27x27."

      - name: "image_36x36"
        type: "string"
        description: "The URL of the user's profile photo at size 36x36."

      - name: "image_60x60"
        type: "string"
        description: "The URL of the user's profile photo at size 60x60."

  - name: "workspace"
    type: "object"
    description: |
      Details about the workspace or organization the user is associated with.

      **Note**: Only workspaces and organizations that contain the user that authorized the integration in Stitch will be returned by {{ integration.display_name }}'s API.
    subattributes:
      - name: "gid"
        type: "string"
        description: "The workspace's GID."

      - name: "id"
        type: "integer"
        description: "The workspace's ID."
        foreign-key-id: "workspace-id"

      - name: "resource_type"
        type: "string"
        description: "This will be `workspace`."
---