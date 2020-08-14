---
tap: "intercom"
version: "1"
key: "admin"

name: "admins"
doc-link: "https://developers.intercom.com/intercom-api-reference/reference#admin-model"
singer-schema: "https://github.com/singer-io/tap-intercom/blob/master/tap_intercom/schemas/admins.json"
description: |
  The `{{ table.name }}` table lists info about the admins in your {{ integration.display_name }} account. An admin is a user, or teammate, in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
  name: "List all admins"
  doc-link: "https://developers.intercom.com/intercom-api-reference/reference#list-admins"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The admin ID."
    foreign-key-id: "admin-id"

  - name: "admin_ids"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "integer"
        description: ""

  - name: "avatar"
    type: "object"
    description: "The admin's avatar."
    subattributes:
      - name: "image_url"
        type: "string"
        description: "The URL to the admin's avatar."
  
  - name: "away_mode_enabled"
    type: "boolean"
    description: "Indicates if the admin is currently set in away mode."
  
  - name: "away_mode_reassign"
    type: "boolean"
    description: "Indicates if the admin is set to automatically reassign new conversations to the app's default inbox."
  
  - name: "email"
    type: "string"
    description: "The email address of the admin."
  
  - name: "has_inbox_seat"
    type: "boolean"
    description: "Indicates if the admin has a paid inbox seat to restrict/allow features."
  
  - name: "job_title"
    type: "string"
    description: "The job title of the admin."
  
  - name: "name"
    type: "string"
    description: "The name of the admin."
  
  - name: "team_ids"
    type: "array"
    description: "The IDs of the teams the admin is a member of."
    subattributes:
      - name: "value"
        type: "integer"
        description: ""
        foreign-key-id: "team-id"
  
  - name: "type"
    type: "string"
    description: "This will be `admin`."
---