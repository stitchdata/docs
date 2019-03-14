---
tap: "jira"
version: "1.0"

name: "worklogs"
doc-link: "https://developer.atlassian.com/cloud/jira/platform/rest/v2/#api-api-2-worklog-updated-get"
singer-schema: "https://github.com/singer-io/tap-jira/blob/master/tap_jira/schemas/worklogs.json"
description: |
  The `{{ table.name }}` table contains info about the worklogs in your {{ integration.display_name }} account.

  **Note**: For a worklog to be replicated, it must be set as `Viewable by All Users`, or the integration [authenticating user]() (visible in the integration's {{ app.page-names.int-settings }} page), must be a member of the project role/group with permission to view the worklog.

  If you're missing worklogs, verify that you have the required permissions to access the worklog.

replication-method: "Key-based Incremental"

#"Worklogs bookmark can't safely advance."
#"Every `updated` field is `{}`"

api-method:
    name: "Get IDs of updated worklogs"
    doc-link: "https://developer.atlassian.com/cloud/jira/platform/rest/v2/#api-api-2-worklog-updated-get"

## There are two different endpoints we use to get worklogs:

## 1. Get IDs of updated worklogs - only returns (you guessed it!) IDs of modified worklogs. As it returns only the worklog ID, we need to get the body details elsewhere. So we use:

## 2. Get worklogs (https://developer.atlassian.com/cloud/jira/platform/rest/v2/#api-api-2-worklog-list-post) - We request the data for the worklog IDs we retrieved in Step 1.
    
attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The worklog ID."
    # foreign-key-id: "worklog-id"

  - name: "updated"
    type: "date-time"
    replication-key: true
    description: |
      The date and time the worklog was last updated.

      {% assign description-type = "worklog author" %}

  - name: "author"
    type: "object"
    description: "Details about the worklog's author."
    subattributes: &userDetails
      - name: "accountId"
        type: "string"
        description: "The {{ description-type }}'s account ID."

      - name: "active"
        type: "boolean"
        description: "Indicates if the {{ description-type }} is active."

      - name: "avatarUrls"
        type: "object"
        description: "The URLs associated with the avatars used by the {{ description-type }}."
        subattributes:
          - name: "16x16"
            type: "string"
            description: "The URL of the {{ description-type }}'s 16x16 avatar."

          - name: "24x24"
            type: "string"
            description: "The URL of the {{ description-type }}'s 24x24 avatar."

          - name: "32x32"
            type: "string"
            description: "The URL of the {{ description-type }}'s 32x32 avatar."

          - name: "48x48"
            type: "string"
            description: "The URL of the {{ description-type }}'s 48x48 avatar."

      - name: "displayName"
        type: "string"
        description: "The {{ description-type }}'s display name. Depending on the {{ description-type }}'s privacy setting, this may be returned as an alternative value."

      - name: "emailAddress"
        type: "string"
        description: "The {{ description-type }}'s email address. Depending on the {{ description-type }}'s privacy settings, this may be returned as null."

      - name: "key"
        type: "string"
        description: "The key of the {{ description-type }}."
        foreign-key-id: "user-key"

      - name: "locale"
        type: "string"
        description: "The locale of the {{ description-type }}. Depending on the {{ description-type }}'s privacy setting, this may be returned as null."

      - name: "name"
        type: "string"
        description: "The name of the {{ description-type }}."

      - name: "self"
        type: "string"
        description: "The URL for the {{ description-type }}."

      - name: "timeZone"
        type: "string"
        description: "The time zone specified in the user's profile. Depending on the user's privacy setting, this may be returned as null."

  - name: "comment"
    type: "string"
    description: "A comment about the worklog."

  - name: "created"
    type: "date-time"
    description: "The date and time the worklog was created."

  - name: "issueId"
    type: "string"
    description: "The ID of the issue associated with the worklog."
    foreign-key-id: "issue-id"

  - name: "properties"
    type: "array"
    description: "Details of properties for the worklog."
    subattributes:
      - name: "key"
        type: "string"
        description: "The key of the property."

      - name: "value"
        type: "anything"
        description: "The value of the property."

  - name: "self"
    type: "string"
    description: "The URL of the worklog."

  - name: "started"
    type: "date-time"
    description: "The date and time on which the worklog was started."

  - name: "timeSpent"
    type: "string"
    description: "The time spent working on the issue as days (`#d`), hours (`#h`), or minutes (`#m` or `#`)."

  - name: "timeSpentSeconds"
    type: "integer"
    description: |
      The time spent working on the issue, in seconds.

      {% assign description-type = "update author" %}

  - name: "updateAuthor"
    type: "object"
    description: "Details about the worklog's update author."
    subattributes: *userDetails

  - name: "visibility"
    type: "object"
    description: "The group or role to which the worklog is visible."
    subattributes:
      - name: "type"
        type: "string"
        description: |
         Indicates whether visibility of the worklog is restricted to a group or role. Possible values are:

         - `group`
         - `role`

      - name: "value"
        type: "string"
        description: "The name of the group or role to which invisibility of the worklog is restricted."
---