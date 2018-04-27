---
tap: "jira"
version: "1.0"

name: "worklogs"
doc-link: https://developer.atlassian.com/cloud/jira/platform/rest/#api-api-2-worklog-list-post
singer-schema: https://github.com/singer-io/tap-jira/blob/master/tap_jira/schemas/worklogs.json
description: |
  The `worklogs` table contains the worklogs contained in issues.

  **Note**: As per [JIRA's documentation](https://developer.atlassian.com/cloud/jira/platform/rest/#api-api-2-worklog-list-post), the `worklogs` endpoint will only ever return 1,000 records at a time.

replication-method: "Incremental"
api-method:
  name: getWorklogsModifiedSince
  doc-link: https://developer.atlassian.com/cloud/jira/platform/rest/#api-api-2-worklog-list-post

user-attributes: &user-attributes
  - name: "self"
    type: "string"
    description: "The URL for the author's user profile."

  - name: "name"
    type: "string"
    description: "The name of the author."

  - name: "key"
    type: "string"
    description: "The author key."

  - name: "accountId"
    type: "string"
    description: "The ID of the author's account."

  - name: "emailAddress"
    type: "string"
    description: "The author's email address."

  - name: "displayName"
    type: "string"
    description: "The display name of the author."

  - name: "active"
    type: "boolean"
    description: "If `true`, the author is an active user."

  - name: "timeZone"
    type: "string"
    description: "The time zone the author resides in."

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The worklog event ID."

  - name: "updated"
    type: "date-time"
    replication-key: true
    description: "The time the worklog was last updated."

  - name: "self"
    type: "string"
    description: "The URL for the worklog."

  - name: "author"
    type: "object"
    description: "Details about the user who created the worklog."
    object-attributes: *user-attributes

  - name: "updateAuthor"
    type: "object"
    description: "Details about the user who created this worklog event."
    object-attributes: *user-attributes

  - name: "comment"
    type: "string"
    description: "The comment associated with the worklog event."

  - name: "created"
    type: "date-time"
    description: "The time the worklog was created."

  - name: "visibility"
    type: "object"
    description: "Details about the visibility of the worklog."
    object-attributes:
      - name: "type"
        type: "string"
        description: "The type of visibility. For example: `role`"

      - name: "value"
        type: "string"
        description: "The value. For example: `Vieweable to [...]"

  - name: "started"
    type: "date-time"
    description: "The time worklog was started."

  - name: "timeSpent"
    type: "string"
    description: "The amount of time the user logged. For example: `10m`"

  - name: "timeSpentSeconds"
    type: "integer"
    description: "The amount of time the user logged, in seconds. For example: `600`"

  - name: "issueId"
    type: "string"
    description: "The ID of the issue associated with the worklog."
    foreign-key: true
---