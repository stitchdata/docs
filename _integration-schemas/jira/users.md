---
tap: "jira"
version: "1.0"

name: "users"
doc-link: https://docs.atlassian.com/jira/REST/ondemand/#api/2/user-findUsers
singer-schema: ## link to the JSON schema file in the integration's Singer repo
description: |
  The `users` table contains info about the users in your JIRA account.

replication-method: "Full Table"

api-method:
  name: findUsers(username=%, includeInactive=true)
  doc-link: https://docs.atlassian.com/jira/REST/ondemand/#api/2/user-findUsers

attributes:
  - name: "key"
    type: "string"
    primary-key: true
    description: "The unique identifier for the user."

  - name: "self"
    type: "string"
    description: "The URL associated with the user."

  - name: "accountId"
    type: "string"
    description: "The user's account ID."

  - name: "name"
    type: "string"
    description: "The name of the user."

  - name: "emailAddress"
    type: "string"
    description: "The email address of the user."

  - name: "avatarUrls"
    type: "object"
    description: "The URLs of the avatars associated with the user."
    object-attributes:
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

  - name: "displayName"
    type: "string"
    description: "The display name of the user."

  - name: "active"
    type: "boolean"
    description: "If `true`, the user is active."

  - name: "timeZone"
    type: "string"
    description: "The time zone the user resides in."

  - name: "locale"
    type: "string"
    description: "The locale the user resides in."

  - name: "groups"
    type: "object"
    description: "Details about the groups the user belongs to."
    object-attributes:
      - name: "size"
        type: "integer"
        description: "The total number of groups the user is a member of."

      - name: "items"
        type: "array"
        description: "Name and URLs of the groups the user belongs to."
        array-attributes:
          - name: "name"
            type: "string"
            description: "The name of the group."

          - name: "self"
            type: "string"
            description: "The URL associated with the group."

  - name: "applicationRoles"
    type: "object"
    description: "Details about the application roles the user has."
    object-attributes:
      - name: "size"
        type: "integer"
        description: "The total number of application roles the user has."

      - name: "items"
        type: "array"
        description: "Names and URLs of the application roles the user has."
        array-attributes:
          - name: "name"
            type: "string"
            description: "The name of the application role."

          - name: "self"
            type: "string"
            description: "The URL associated with the application role."

  - name: "expand"
    type: "string"
    description: "This is a field used by Stitch to replicate data for this endpoint from JIRA's API."
---