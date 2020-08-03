---
tap: "jira"
version: "2"
key: "issue-comment"

name: "issue_comments"
doc-link: "https://developer.atlassian.com/cloud/jira/platform/rest/v2/#api-api-2-issue-issueIdOrKey-comment-get"
singer-schema: "https://github.com/singer-io/tap-jira/blob/master/tap_jira/schemas/issue_comments.json"
description: |
  The `{{ table.name }}` table contains info about comments made on issues.

  #### Replication requirements {#replication-requirements-issue-comments}

  To replicate this data:

  1. The [`issues`](#issues) table must also be set to replicate. **Note**: When an issue is updated, all the comments for that issue will also be replicated.
  2. The `Browse Projects` [project {{ integration.display_name }} permission]({{ integration.project-permissions-doc }}){:target="new"} is required. Refer to [{{ integration.display_name }}'s API documentation]({{ table.doc-link }}){:target="new"} for more info.

replication-method: "Key-based Incremental"

replication-key:
  name: "issues.updated"

api-method:
    name: "Get issue comments"
    doc-link: "https://developer.atlassian.com/cloud/jira/platform/rest/v2/#api-api-2-issue-issueIdOrKey-comment-get"
    
attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The issue comment ID."
    # foreign-key-id: "issue-comment-id"

  - name: "author"
    type: "object"
    description: "Details about the author of the issue comment."
    subattributes:
      - name: "accountId"
        type: "string"
        description: "The account ID of the user, which uniquely identifies the user across all Atlassian products."
        foreign-key-id: "user-id"

      - name: "active"
        type: "boolean"
        description: "Indicates whether the user is active."

      - name: "avatarUrls"
        type: "object"
        description: "The URLs associated with the avatars used by the user."
        subattributes:
          - name: "16x16"
            type: "string"
            description: "The URL of the user's 16x16 avatar."

          - name: "24x24"
            type: "string"
            description: "The URL of the user's 24x24 avatar."

          - name: "32x32"
            type: "string"
            description: "The URL of the user's 32x32 avatar."

          - name: "48x48"
            type: "string"
            description: "The URL of the user's 48x48 avatar."
        anchor-id: 1

      - name: "displayName"
        type: "string"
        description: "The display name of the user. Depending on the user's privacy settings, this may be returned an alternative value."

      - name: "emailAddress"
        type: "string"
        description: "The email address of the user. Depending on the user's privacy settings, this may be returned as null."

      - name: "key"
        type: "string"
        description: "The user's key."

      - name: "name"
        type: "string"
        description: "The username of the user. Depending on the user's privacy settings, this may be returned as null."

      - name: "self"
        type: "string"
        description: "The URL of the user."

      - name: "timeZone"
        type: "string"
        description: "The timezone specified in the user's profile. Depending on the user's privacy settings, this may be returned as null."

  - name: "body"
    type: "string"
    description: "The issue comment text in Atlassian Document Format."

  - name: "created"
    type: "date-time"
    description: "The date and time when the issue comment was created."

  - name: "issueId"
    type: "string"
    description: "The ID of the issue associated with the issue comment."
    foreign-key-id: "issue-id"

  - name: "jsdPublic"
    type: "boolean"
    description: "Indicates whether the issue comment is visible in {{ integration.display_name }} service desk."

  - name: "properties"
    type: "array"
    description: "A list of issue comment properties."
    subattributes:
      - name: "key"
        type: "string"
        description: "The key of the property."

      - name: "value"
        type: "anything"
        description: "The value of the property."

  - name: "renderedBody"
    type: "string"
    description: "The rendered version of the issue comment."

  - name: "self"
    type: "string"
    description: "The URL of the issue comment."

  - name: "updateAuthor"
    type: "object"
    description: "Details about the user who updated the issue comment."
    subattributes:
      - name: "accountId"
        type: "string"
        description: "The account ID of the user, which uniquely identifies the user across all Atlassian products."
        foreign-key-id: "user-id"

      - name: "active"
        type: "boolean"
        description: "Indicates whether the user is active."

      - name: "avatarUrls"
        type: "object"
        description: "The URLs associated with the avatars used by the user."
        subattributes:
          - name: "16x16"
            type: "string"
            description: "The URL of the user's 16x16 avatar."

          - name: "24x24"
            type: "string"
            description: "The URL of the user's 24x24 avatar."

          - name: "32x32"
            type: "string"
            description: "The URL of the user's 32x32 avatar."

          - name: "48x48"
            type: "string"
            description: "The URL of the user's 48x48 avatar."
        anchor-id: 2

  - name: "updated"
    type: "date-time"
    description: "The date and time the issue comment was last updated."

  - name: "visibility"
    type: "object"
    description: "The group or role to which this issue comment is visible."
    subattributes:
      - name: "type"
        type: "string"
        description: |
          Indicates whether the issue comment is restricted to a group or role. Possible values are `group` and `role`.

      - name: "value"
        type: "string"
        description: "The name of the grou or role to which visibility of the issue comment is restricted."
---