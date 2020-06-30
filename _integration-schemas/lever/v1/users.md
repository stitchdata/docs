---
tap: "lever"
version: "1"
key: "user"

name: "users"
doc-link: "https://hire.lever.co/developer/documentation#users"
singer-schema: "https://github.com/singer-io/tap-lever/blob/master/tap_lever/schemas/users.json"
description: |
  The `{{ table.name }}` table contains info about the users in your {{ integration.display_name }} account. A user includes anyone who has been invited to {{ integration.display_name }} to collaborate on recruiting efforts.

replication-method: "Full Table"

api-method:
  name: "List all users"
  doc-link: "https://hire.lever.co/developer/documentation#list-all-users"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The user ID."
    foreign-key-id: "user-id"

  - name: "accessRole"
    type: "string"
    description: |
      The user's access role. Possible values are:

      - `super admin`
      - `admin`
      - `team member`
      - `limited team member`
      - `interviewer`

  - name: "createdAt"
    type: "date-time"
    description: "The datetime when the user was created."

  - name: "deactivatedAt"
    type: "date-time"
    description: "The datetime when the user was deactivated."

  - name: "email"
    type: "string"
    description: "The user's email address."

  - name: "externalDirectoryId"
    type: "string"
    description: "The ID for the user in an external HR directory."

  - name: "name"
    type: "string"
    description: "The user's preferred name."

  - name: "photo"
    type: "string"
    description: "The URL for the user's Gravatar, if enabled."

  - name: "username"
    type: "string"
    description: "The user's username, extracted from their `email`."
---