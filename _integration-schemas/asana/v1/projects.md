---
tap: "asana"
version: "1"
key: "project"

name: "projects"
doc-link: "https://asana.com/developers/api-reference/projects"
singer-schema: "https://github.com/singer-io/tap-asana/blob/master/tap_asana/schemas/projects.json"
description: |
  The `{{ table.name }}` table contains info about the projects the user who authorized the {{ integration.display_name }} integration in Stitch has access to.

replication-method: "Key-based Incremental"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The project ID."
    foreign-key-id: "project-id"

  - name: "modified_at"
    type: "date-time"
    replication-key: true
    description: "The time the project was last modified."

  - name: "archived"
    type: "boolean"
    description: "Indicates if the project has been archived or not."

  - name: "color"
    type: "string"
    description: |
      The color of the project. Possible values are:

      - `dark-pink`
      - `dark-green` 
      - `dark-blue`
      - `dark-red`
      - `dark-teal` 
      - `dark-brown` 
      - `dark-orange` 
      - `dark-purple`
      - `dark-warm-gray` 
      - `light-pink`
      - `light-green` 
      - `light-blue`
      - `light-red`
      - `light-teal` 
      - `light-yellow` 
      - `light-orange`
      - `light-purple`
      - `light-warm-gray`

  - name: "created_at"
    type: "date-time"
    description: "The time the project was created."

  - name: "current_status"
    type: "string"
    description: "The most recently created status update for the project."

  - name: "due_date"
    type: "date-time"
    description: "The day on which the project is due."

  - name: "followers"
    type: "array"
    description: "A list of users following the project."
    subattributes:
      - name: "gid"
        type: "string"
        description: "The follower's GID."

      - name: "id"
        type: "integer"
        description: "The follower's ID."
        foreign-key-id: "user-id"

      - name: "resource_type"
        type: "string"
        description: "This will be `user`."

  - name: "gid"
    type: "string"
    description: "The project's GID."

  - name: "members"
    type: "array"
    description: "A list of users who are members of the project."
    subattributes:
      - name: "gid"
        type: "string"
        description: "The user's GID."

      - name: "id"
        type: "integer"
        description: "The user's ID."
        foreign-key-id: "user-id"

      - name: "resource_type"
        type: "string"
        description: "This will be `user`."

  - name: "name"
    type: "string"
    description: "The name of the project."

  - name: "notes"
    type: "string"
    description: "Any notes associated with the project."

  - name: "owner"
    type: "object"
    description: "Details about the current owner of the project."
    subattributes:
      - name: "gid"
        type: "string"
        description: "The owner's GID."

      - name: "id"
        type: "integer"
        description: "The owner's ID."
        foreign-key-id: "user-id"

      - name: "resource_type"
        type: "string"
        description: "This will be `user`."

  - name: "public"
    type: "boolean"
    description: "Indicates if the project is public to the organization."

  - name: "team"
    type: "object"
    description: "Details about the team the project is associated with."
    subattributes:
      - name: "gid"
        type: "string"
        description: "The team's GID."

      - name: "id"
        type: "integer"
        description: "The team's ID."

      - name: "resource_type"
        type: "string"
        description: "This will be `team`."

  - name: "workspace"
    type: "object"
    description: "Details about the workspace or organization the project is associated with."
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