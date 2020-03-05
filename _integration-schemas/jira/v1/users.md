---
tap: "jira"
version: "1"
key: "user"

name: "users"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-jira/tree/77206190933146b7cf51f14bfc7aaf670539ca5f/tap_jira/schemas/users.json"
description: |
  The `{{ table.name }}` table contains info about the users in your {{ integration.display_name }} account.

  **Note**: To replicate this data, the `Administer {{ integration.display_name }}` [global {{ integration.display_name }} permission]({{ integration.global-permissions-doc }}){:target="new"} is required. Refer to [{{ integration.display_name }}'s API documentation]({{ table.doc-link }}){:target="new"} for more info.

replication-method: "Full Table"

api-method:
    name: "Find users"
    doc-link: "https://developer.atlassian.com/cloud/jira/platform/rest/v2/#api-api-2-user-search-get"
    
attributes:
  - name: "key"
    type: "string"
    primary-key: true
    description: "The user key."
    foreign-key-id: "user-key"

  - name: "accountId"
    type: "string"
    description: "The user's account ID."

  - name: "active"
    type: "boolean"
    description: "Indicates if the user is active."
    subattributes:
      - name: "max-results"
        type: "integer"
        description: ""

      - name: "size"
        type: "integer"
        description: ""

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

  - name: "displayName"
    type: "string"
    description: "The user's display name."

  - name: "emailAddress"
    type: "string"
    description: "The user's email address. Depending on the user's privacy settings, this may be returned as null."
    subattributes:
      - name: "max-results"
        type: "integer"
        description: ""

      - name: "size"
        type: "integer"
        description: ""

  - name: "key"
    type: "string"
    description: "The key of the user."

  - name: "name"
    type: "string"
    description: "The name of the user."

  - name: "self"
    type: "string"
    description: "The URL for the user."

  - name: "timeZone"
    type: "string"
    description: "The time zone specified in the user's profile. Depending on the user's privacy setting, this may be returned as null."
---
