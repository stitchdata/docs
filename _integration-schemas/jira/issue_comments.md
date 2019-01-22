---
tap: "jira"
version: "1.0"

name: "issue_comments"
doc-link: https://docs.atlassian.com/jira/REST/cloud/#api/2/search-search
singer-schema: https://github.com/singer-io/tap-jira/blob/master/tap_jira/schemas/issue_comments.json
description: |
  The `issue_comments` table contains the individual comments made on issues.

  **To replicate data for this table**, the `issues` table must be selected. 

replication-method: "Incremental"

api-method:
  name: search(fields=id,comment)
  doc-link: https://docs.atlassian.com/jira/REST/cloud/#api/2/search-search

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The issue comment ID."

  - name: "updated"
    type: "date-time"
    replication-key: true
    description: "The last time the issue was updated."

  - name: "self"
    type: "string"
    description: "The URL associated with the issue comment."

  - name: "issueId"
    type: "string"
    description: "The ID of the issue the comment is a part of."
    foreign-key: true

  - name: "author"
    type: "object"
    description: "Details about the user who created the issue."
    object-attributes:
      - name: "key"
        type: "string"
        description: "The author key."
        foreign-key: true
        table: "users"

      - name: "self"
        type: "string"
        description: "The URL for the author's user profile."

      - name: "name"
        type: "string"
        description: "The name of the author."

      - name: "accountId"
        type: "string"
        description: "The ID of the account associated with the author."

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

  - name: "body"
    type: "string"
    description: "The plaintext body of the comment."

  - name: "renderedBody"
    type: "string"
    description: "The HTML body of the comment."

  - name: "updateAuthor"
    type: "object"
    description: "Details about the user who added the issue comment."
    object-attributes:
      - name: "key"
        type: "string"
        description: "The author key."
        foreign-key: true
        table: "users"

      - name: "self"
        type: "string"
        description: "The URL for the author's user profile."

      - name: "name"
        type: "string"
        description: "The name of the author."

      - name: "accountId"
        type: "string"
        description: "The ID of the account associated with the author."

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

  - name: "created"
    type: "date-time"
    description: "The time the comment was created."

  - name: "visibility"
    type: "object"
    description: "Details about the visibility of the [PLACEHOLDER]"
    object-attributes:
      - name: "type"
        type: "string"
        description: "The type of visibility. For example: `role`"

      - name: "value"
        type: "string"
        description: ""
---