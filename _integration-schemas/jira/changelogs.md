---
tap: "jira"
version: "1.0"

name: "changelogs"
doc-link: https://docs.atlassian.com/jira/REST/cloud/#api/2/project-getProjectVersionsPaginated
singer-schema: https://github.com/singer-io/tap-jira/blob/master/tap_jira/schemas/changelogs.json
description: |
  The `changelogs` table contains info about updates made to issues.

replication-method: "Full Table"

api-method:
  name: 
  doc-link: 

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The changelog ID."

  - name: "issueId"
    type: "string"
    description: "The ID of the issue the changelog is associated with."
    foreign-key: true

  - name: "author"
    type: "object"
    description: "Details about the user who authored the changelog."
    object-attributes:
      - name: "key"
        type: "string"
        description: "The changelog author's key."
        foreign-key: true
        table: "users"

      - name: "self"
        type: "string"
        description: "The URL associated with the changelog author."

      - name: "name"
        type: "string"
        description: "The name of the changelog author."

      - name: "accountId"
        type: "string"
        description: "The changelog author's account ID."

      - name: "emailAddress"
        type: "string"
        description: "The email address associated with the changelog author."

      - name: "displayName"
        type: "string"
        description: "The display name of the changelog author."

      - name: "active"
        type: "boolean"
        description: "If `true`, the changelog author is an active user."

      - name: "timeZone"
        type: "string"
        description: "The time zone the changelog author utilizes."

      - name: "avatarUrls"
        type: "object"
        description: "The URLs of the avatars associated with the changelog author."
        object-attributes:
          - name: "48x48"
            type: "string"
            description: "The URL of the changelog author's 48x48 avatar."

          - name: "24x24"
            type: "string"
            description: "The URL of the changelog author's 24x24 avatar."

          - name: "16x16"
            type: "string"
            description: "The URL of the changelog author's 16x16 avatar."

          - name: "32x32"
            type: "string"
            description: "The URL of the changelog author's 32x32 avatar."

  - name: "created"
    type: "date-time"
    description: "The time the changelog was created."

  - name: "items"
    type: "array"
    description: "Details about the changes to fields that occurred in the updated."
    array-attributes:
      - name: "fieldId"
        type: "string"
        primary-key: true
        description: "The field ID."

      - name: "field"
        type: "string"
        description: "The name of the field that was updated."

      - name: "fieldtype"
        type: "string"
        description: ""

      - name: "from"
        type: "string"
        description: "The original value of the field, if applicable."

      - name: "fromString"
        type: "string"
        description: "The original value of the field as a string."

      - name: "to"
        type: "string"
        description: "The updated value of the field, if applicable."

      - name: "toString"
        type: "string"
        description: "The updated value of the field as a string."

  - name: "historyMetadata"
    type: "object"
    description: "Details about activities, emails, and activities."
    object-attributes:
      - name: "description"
        type: "string"
        description: "The description of the event."

      - name: "descriptionKey"
        type: "string"
        description: "The event description key."

      - name: "activityDescription"
        type: "string"
        description: "The description of the activity."

      - name: "activityDescriptionKey"
        type: "string"
        description: "The activity description key."

      - name: "emailDescription"
        type: "string"
        description: "The description of the email."

      - name: "emailDescriptionKey"
        type: "string"
        description: "The email description key."

      - name: "actor"
        type: "object"
        description: ""
        object-attributes: &user-attributes
          - name: "id"
            type: "string"
            description: "The {{ attribute.name }} ID."

          - name: "displayName"
            type: "string"
            description: "The display name of the {{ subattribute.name }}."

          - name: "displayNameKey"
            type: "string"
            description: "The {{ subattribute.name }}'s display name key."

          - name: "type"
            type: "string"
            description: "The {{ subattribute.name }} type."

          - name: "avatarUrl"
            type: "string"
            description: "The URL of the {{ subattribute.name }}'s avatar."

          - name: "url"
            type: "string"
            description: "The URL associated with the {{ subattribute.name }}."

      - name: "generator"
        type: "object"
        description: "Details about the event generator."
        object-attributes: *user-attributes

      - name: "cause"
        type: "object"
        description: "Details about the event cause."
        object-attributes: *user-attributes

---