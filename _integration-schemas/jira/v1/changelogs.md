---
tap: "jira"
version: "1"
key: "changelog"

name: "changelogs"
doc-link: "https://developer.atlassian.com/cloud/jira/platform/rest/v2/#api-api-2-issue-issueIdOrKey-changelog-get"
singer-schema: "https://github.com/singer-io/tap-jira/tree/77206190933146b7cf51f14bfc7aaf670539ca5f/tap_jira/schemas/changelogs.json"
description: |
  The `{{ table.name }}` table contains info about the changelogs associated with an issue.

  #### Replication requirements {#replication-requirements-changelogs}

  To replicate this data:

  1. The [`issues`](#issues) table must also be set to replicate. **Note**: When an issue is updated, all the changelogs for that issue will also be replicated.

  2. The `Browse Projects` [project {{ integration.display_name }} permission]({{ integration.project-permissions-doc }}){:target="new"} is required. Refer to [{{ integration.display_name }}'s API documentation]({{ table.doc-link }}){:target="new"} for more info.

replication-method: "Key-based Incremental"

replication-key:
  name: "issues.updated"

api-method:
    name: "Get issue change logs"
    doc-link: "https://developer.atlassian.com/cloud/jira/platform/rest/v2/#api-api-2-issue-issueIdOrKey-changelog-get"
    
attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The changelog ID."
    # foreign-key-id: "changelog-id"

  - name: "author"
    type: "object"
    description: "Details about the change log author."
    subattributes:
      - name: "accountId"
        type: "string"
        description: "The author's account ID."

      - name: "active"
        type: "boolean"
        description: "Indicates if the author is an active user."

      - name: "avatarUrls"
        type: "object"
        description: "The URLs associated with the avatars used by the {{ attribute.name }}."
        subattributes:
          - name: "16x16"
            type: "string"
            description: "The URL of the {{ attribute.name }}'s 16x16 avatar."

          - name: "24x24"
            type: "string"
            description: "The URL of the {{ attribute.name }}'s 24x24 avatar."

          - name: "32x32"
            type: "string"
            description: "The URL of the {{ attribute.name }}'s 32x32 avatar."

          - name: "48x48"
            type: "string"
            description: "The URL of the {{ attribute.name }}'s 48x48 avatar."

      - name: "displayName"
        type: "string"
        description: "The {{ attribute.name }}'s display name."

      - name: "emailAddress"
        type: "string"
        description: "The {{ attribute.name }}'s email address."

      - name: "key"
        type: "string"
        description: "The {{ attribute.name }} ID."
        foreign-key-id: "user-key"

      - name: "name"
        type: "string"
        description: "The {{ attribute.name }}'s name."

      - name: "self"
        type: "string"
        description: "The URL of the {{ attribute.name }} in {{ integration.display_name }}."

      - name: "timeZone"
        type: "string"
        description: "The {{ attribute.name }}'s time zone."

  - name: "created"
    type: "date-time"
    description: "The date and time the change log was created."

  - name: "historyMetadata"
    type: "object"
    description: "Details about issue history metadata."
    subattributes:
      - name: "activityDescription"
        type: "string"
        description: "The activity described in the history record."

      - name: "activityDescriptionKey"
        type: "string"
        description: &deprecated "**This field has been deprecated by {{ integration.display_name }}.**"

      - name: "actor"
        type: "object"
        description: "Details about the user whose action created the history record."
        action: "generated"
        subattributes: &historyMetadataParticipant
          - name: "avatarUrl"
            type: "string"
            description: "The URL to an avatar for the user or system that {{ subattribute.action }} the history record."

          - name: "displayName"
            type: "string"
            description: "The display name of the user or system that {{ subattribute.action }} the history record."

          - name: "displayNameKey"
            type: "string"
            description: *deprecated

          - name: "id"
            type: "string"
            description: "The ID of the user or system that {{ subattribute.action }} the history record."

          - name: "type"
            type: "string"
            description: "The type of the user or system that {{ subattribute.action }} the history record."

          - name: "url"
            type: "string"
            description: "The URL of the user or system that {{ subattribute.action }} the history record."

      - name: "cause"
        type: "object"
        description: "Details about the caused that triggered the creation of the history record."
        action: "caused"
        subattributes: *historyMetadataParticipant

      - name: "description"
        type: "string"
        description: "The description of the history record."

      - name: "descriptionKey"
        type: "string"
        description: *deprecated

      - name: "emailDescription"
        type: "string"
        description: "The description of the email address associated with the history record."

      - name: "emailDescriptionKey"
        type: "string"
        description: *deprecated

      - name: "extraData"
        type: "object"
        description: "Additional arbitrary information about the history record."
        subattributes:
          - name: "fieldName"
            type: "string"
            description: "The arbitrary information about the history record."

      - name: "generator"
        type: "object"
        description: "Details about the user or system that generated the history record."
        action: "generated"
        subattributes: *historyMetadataParticipant

      - name: "type"
        type: "string"
        description: "The type of the history record."

  - name: "issueId"
    type: "string"
    description: "The ID of the issue associated with the changelog."
    foreign-key-id: "issue-id"

  - name: "items"
    type: "array"
    description: "A list of change items associated with the changelog."
    subattributes:
      - name: "field"
        type: "string"
        description: "The name of the field that changed."

      - name: "fieldId"
        type: "string"
        description: "The ID of the field that changed."

      - name: "fieldtype"
        type: "string"
        description: "The type of the field that changed."

      - name: "from"
        type: "string"
        description: "The details of the original field value."

      - name: "fromString"
        type: "string"
        description: "The details of the original value as a string."

      - name: "to"
        type: "string"
        description: "The details of the new value."

      - name: "toString"
        type: "string"
        description: "The details of the new value as a string."
---