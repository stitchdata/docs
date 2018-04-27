---
tap: "jira"
version: "1.0"

name: "issues"
doc-link: https://docs.atlassian.com/jira/REST/ondemand/#api/2/issue-getIssue
singer-schema: ## link to the JSON schema file in the integration's Singer repo
description: |
  The `issues` table contains info about the issues in your JIRA instance.

  **Note**: Some issue data is located in other tables:

  - [`changelogs`](#changelogs) 
  - [`issue_comments`](#issue_comments)
  - [`issue_transitions`](#issue_transitions)

  #### Deleted issues

  When an issue is hard-deleted in JIRA, the record for the issue will remain in your data warehouse. This is due to the nature of Stitch [Replication Keys]() and the design of JIRA's API:

  - **Replication Keys**: This table uses the values in the `{{ replication-keys | strip }}` column to identify new and updated data for replication. If a record is hard-deleted, there won't be a value for Stitch to check and thus no way to identify the change, meaning the record will remain in the destination.
  - **JIRA's API**: Currently, JIRA's API doesn't include a way to identify deleted issues.

  To identify deleted issues, [Atlassian's suggested workaround](https://answers.atlassian.com/questions/75537/how-do-i-find-if-an-issue-has-been-deleted) is:

  1. Create a status in JIRA that will be applied to issues you want to delete.
  2. Before deleting the issue, apply the status.
  3. Delete the issue.
  4. Allow Stitch to extract and load the updated data into your destination.
  5. After Stitch finishes loading the data, use the `fields__status__name` field in your queries to filter issues with the deleted status you applied in step 2. For example, the following query would return any issues that had been marked with a `Deleted` status:

     ```sql
     SELECT *
     FROM stitch_jira.issues
     WHERE fields__status__name = 'Deleted'
     ```

replication-method: "Incremental"

api-method:
  name: search(fields=*all,-comment, expand=changelog)
  doc-link: https://docs.atlassian.com/jira/REST/cloud/#api/2/search-search


user-attributes: &user-attributes
  - name: "key"
    type: "string"
    description: "The key of the {{ subattribute.name }}."
    foreign-key: true
    table: "users"

  - name: "accountId"
    type: "string"
    description: "The account ID associated with the {{ attribute.name }}."

  - name: "active"
    type: "boolean"
    description: "If `true`, the {{ subattribute.name }} is active."

  - name: "displayName"
    type: "string"
    description: "The display name of the {{ subattribute.name }}."

  - name: "name"
    type: "string"
    description: "The name of the {{ subattribute.name }}."

  - name: "self"
    type: "string"
    description: "The URL associated with the {{ subattribute.name }}."

  - name: "avatarUrls"
    type: "object"
    description: "The URLs associated with the avatars used by the {{ subattribute.name }}."
    object-attributes:
      - name: "16x16"
        type: "string"
        description: "The URL of the {{ subattribute.name }}'s 16x16 avatar."

      - name: "24x24"
        type: "string"
        description: "The URL of the {{ subattribute.name }}'s 24x24 avatar."

      - name: "32x32"
        type: "string"
        description: "The URL of the {{ subattribute.name }}'s 32x32 avatar."

      - name: "48x48"
        type: "string"
        description: "The URL of the {{ subattribute.name }}'s 48x48 avatar."

avatarurls-attributes: &avatarUrls-attributes
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

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The issue ID."

  - name: "updated"
    type: "date-time"
    replication-key: true
    description: "The date the issue was last updated."

  - name: "self"
    type: "string"
    description: "The API URL of the issue in JIRA."

  - name: "key"
    type: "string"
    description: "The issue key."

  - name: "fields"
    type: "object"
    description: "Details about the state of the issue."
    object-attributes:
      - name: "aggregateProgress"
        type: "object"
        description: "Details about the aggregate progress of the issue."
        object-attributes:
          - name: "percent"
            type: "integer"
            description: ""

          - name: "progress"
            type: "integer"
            description: ""

          - name: "total"
            type: "integer"
            description: ""

      - name: "aggregateTimeEstimate"
        type: "integer"
        description: "The aggregate time estimate for the issue, in seconds."

      - name: "aggregateTimeOriginalEstimate"
        type: "integer"
        description: "The aggregate time estimate for the issue, in seconds."

      - name: "aggregateTimeSpent"
        type: "integer"
        description: "The aggregate amount of time tracked against the issue, in seconds."

      - name: "assignee"
        type: "object"
        description: "Details about the user assigned to the issue."
        object-attributes: *user-attributes

      - name: "created"
        type: "date-time"
        description: "The date the issue was created."

      - name: "description"
        type: "string"
        description: "The description of the issue. For example: `Bug report for user logins`"

      - name: "summary"
        type: "string"
        description: "The issue summary."

      - name: "timeEstimate"
        type: "integer"
        description: "The time estimate for the issue, in seconds. For example: `600`"

      - name: "timeOriginalEstimate"
        type: "integer"
        description: "The original time estimate for the issue, in seconds. For example: `600`"

      - name: "timeSpent"
        type: "integer"
        description: "The total amount of time tracked against the issue, in seconds. For example: `300`"

      - name: "workratio"
        type: "integer"
        description: ""

  # Start CREATOR

      - name: "creator"
        type: "object"
        description: "Details about the user who created the issue."
        object-attributes: *user-attributes

  # End CREATOR

  # Start ATTACHMENT
      - name: "attachment"
        type: "array"
        description: "Details about the issue's attachments."
        array-attributes:
          - name: "id"
            type: "string"
            primary-key: true
            description: "The attachment ID."

          - name: "created"
            type: "date-time"
            description: "The date the attachment was created."

          - name: "author"
            type: "object"
            description: "Details about the user who created the attachment."
            object-attributes: *user-attributes

          - name: "avatarUrls"
            type: "object"
            description: "The URLs of the avatars associated with the attachment."
            object-attributes: *avatarUrls-attributes

          - name: "content"
            type: "string"
            description: "The URL of the content in JIRA."

          - name: "filename"
            type: "string"
            description: "The file name of the attachment."

          - name: "mimeType"
            type: "string"
            description: "The content type of the attachment. For example: `image/jpeg`"

          - name: "self"
            type: "string"
            description: "The API URL of the attachment in JIRA."

          - name: "size"
            type: "integer"
            description: "The size of the attachment file."

          - name: "thumbnail"
            type: "string"
            description: "The URL of the attachment's thumbnail."

  # End ATTACHMENT

  # Start ISSUELINKS

      - name: "issueLinks"
        type: "array"
        description: "Details about the issues linked to the issue."
        array-attributes: &issue-attributes
          - name: "id"
            type: "string"
            primary-key: true
            description: "The issue link ID."

          - name: "self"
            type: "string"
            description: "The API URL of the issue link in JIRA."

      # Start ISSUELINKS__INWARDISSUE

          - name: "inwardIssue"
            type: "object"
            description: ""
            object-attributes:
              - name: "id"
                type: "string"
                description: 

              - name: "key"
                type: "string"
                description: 

              - name: "self"
                type: "string"
                description: 

          # Start ISSUELINKS__INWARDISSUE__FIELDS

              - name: "fields"
                type: "object"
                description: ""
                object-attributes:
                  - name: "summary"
                    type: "string"
                    description: 

              # Start ISSUELINKS__INWARDISSUE__FIELDS__ISSUETYPE

                  - name: "issueType"
                    type: "object"
                    description: 
                    object-attributes:
                      - name: "id"
                        type: "string"
                        description: 

                      - name: "avatarId"
                        type: "integer"
                        description: ""

                      - name: "description"
                        type: "string"
                        description: 

                      - name: "iconUrl"
                        type: "string"
                        description: 

                      - name: "name"
                        type: "string"
                        description: 

                      - name: "self"
                        type: "string"
                        description: 

                      - name: "subtask"
                        type: "boolean"
                        description: 

              # End ISSUELINKS__INWARDISSUE__FIELDS__ISSUETYPE

              # Start ISSUELINKS__INWARDISSUE__FIELDS__PRIORITY

                  - name: "priority"
                    type: "object"
                    description: 
                    object-attributes:
                      - name: "id"
                        type: "string"
                        description: 

                      - name: "name"
                        type: "string"
                        description: 

                      - name: "self"
                        type: "string"
                        description: 

              # End ISSUELINKS__INWARDISSUE__FIELDS__PRIORITY

              # Start ISSUELINKS__INWARDISSUE__FIELDS__STATUS

                  - name: "status"
                    type: "object"
                    description: 
                    object-attributes:
                      - name: "id"
                        type: "string"
                        description: 

                      - name: "description"
                        type: "string"
                        description: 

                      - name: "iconUrl"
                        type: "string"
                        description: 

                      - name: "name"
                        type: "string"
                        description: 

                      - name: "self"
                        type: "string"
                        description: 

                  # Start ISSUELINKS__INWARDISSUE__FIELDS__STATUS__STATUSCATEGORY

                      - name: "statusCategory"
                        type: "object"
                        description: 
                        object-attributes:
                          - name: "colorName"
                            type: "string"
                            description: 

                          - name: "id"
                            type: "string"
                            description: 

                          - name: "key"
                            type: "string"
                            description: 

                          - name: "name"
                            type: "string"
                            description: 

                          - name: "self"
                            type: "string"
                            description: 

                  # End ISSUELINKS__INWARDISSUE__FIELDS__STATUS__STATUSCATEGORY

              # End ISSUELINKS__INWARDISSUE__FIELDS__STATUS

      # End ISSUELINKS__INWARDISSUE

          - name: "outwardIssue"
            type: "object"
            description: ""
            object-attributes: *issue-attributes

          - name: "type"
            type: "object"
            description: 
            object-attributes:
              - name: "id"
                type: "string"
                description: 

              - name: "inward"
                type: "string"
                description: 

              - name: "name"
                type: "string"
                description: 

              - name: "outward"
                type: "string"
                description: 

              - name: "self"
                type: "string"
                description: 

          - name: "displayName"
            type: "string"
            description: ""

          - name: "emailAddress"
            type: "string"
            description: ""

          - name: "key"
            type: "string"
            description: ""

          - name: "name"
            type: "string"
            description: ""

          - name: "self"
            type: "string"
            description: ""

          - name: "timeZone"
            type: "string"
            description: ""

  # End ISSUELINKS

  # Start ISSUETYPE

      - name: "issueType"
        type: "object"
        description: "Details about the issue's type."
        object-attributes:
          - name: "id"
            type: "string"
            description: "The issue type ID."

          - name: "avatarId"
            type: "integer"
            description: "The ID of the issue type's avatar."

          - name: "description"
            type: "string"
            description: "The description of the issue type."

          - name: "iconUrl"
            type: "string"
            description: "The URL of the icon associated with the issue type."

          - name: "name"
            type: "string"
            description: "The name of the issue type."

          - name: "self"
            type: "string"
            description: "The API URL of the issue type in JIRA."

          - name: "subtask"
            type: "boolean"
            description: "If `true`, this issue type contains subtasks."

  # End ISSUETYPE

      - name: "labels"
        type: "array"
        description: "The labels that have been applied to the issue."
        array-attributes:
          - name: "value"
            type: "string"
            description: "The tag applied to the issue. For example: `Addition`"

      - name: "lastViewed"
        type: "date-time"
        description: "The date the issue was last viewed."

  # Start PRIORITY

      - name: "priority"
        type: "object"
        description: "Details about the issue's current priority settings."
        object-attributes:
          - name: "id"
            type: "string"
            description: "The priority ID."

          - name: "iconUrl"
            type: "string"
            description: "The URL of the icon associated with the priority setting."

          - name: "name"
            type: "string"
            description: "The name of the priority setting. For example: `Highest`"

          - name: "self"
            type: "string"
            description: "The API URL for the priority setting in JIRA."

  # End PRIORITY

  # Start PROGRESS

      - name: "progress"
        type: "object"
        description: "Details about the progress made on the issue."
        object-attributes:
          - name: "percent"
            type: "integer"
            description: "The percentage of the issue that has been ."

          - name: "progress"
            type: "integer"
            description: ""

          - name: "total"
            type: "integer"
            description: ""

  # End PROGRESS

  # Start PROJECT

      - name: "project"
        type: "object"
        description: "Details about the project attached to the issue."
        object-attributes:
          - name: "id"
            type: "string"
            description: "The project ID."
            foreign-key: true
            table: "projects"

          - name: "key"
            type: "string"
            description: "The project key."

          - name: "name"
            type: "string"
            description: "The name of the project."

          - name: "projectTypeKey"
            type: "string"
            description: "The project type key."
            foreign-key: true
            table: "project_types"

          - name: "self"
            type: "string"
            description: "The API URL for the project in JIRA."

          - name: "avatarUrls"
            type: "object"
            description: "The URLs of the avatars associated with the project."
            object-attributes: *avatarUrls-attributes

  # End PROJECT

  # Start REPORTER

      - name: "reporter"
        type: "object"
        description: ""
        object-attributes: *user-attributes

    # Start STATUS

      - name: "status"
        type: "object"
        description: "Details about the current status of the issue."
        object-attributes:
          - name: "id"
            type: "string"
            description: "The status ID."

          - name: "iconUrl"
            type: "string"
            description: "The URL of the icon associated with the status."

          - name: "name"
            type: "string"
            description: "The name of the status. For example: `In Progress`"

          - name: "self"
            type: "string"
            description: "The API URL for the status in JIRA."

      # Start STATUS__STATUSCATEGORY

          - name: "statusCategory"
            type: "object"
            description: "Details about the category of the issue's current status."
            object-attributes:
              - name: "id"
                type: "integer"
                description: "The status category ID."

              - name: "colorName"
                type: "string"
                description: "The name of the color associated with the issue's current status. For example: `yellow`"

              - name: "key"
                type: "string"
                description: "The status category key."

              - name: "name"
                type: "string"
                description: "The name of the status category. For example: `In Progress`"

              - name: "self"
                type: "string"
                description: "The API URL for the status category in JIRA."

      # End STATUS__STATUSCATEGORY

    # End STATUS

    # Start TIMETRACKING

      - name: "timeTracking"
        type: "object"
        description: "Details about the time tracking estimates for the issue."
        object-attributes:
          - name: "originalEstimate"
            type: "string"
            description: "The original time estimate for the issue. For example: `10m`"

          - name: "originalEstimateSeconds"
            type: "integer"
            description: "The original time estimate for the issue, in seconds. For example: `600`"

          - name: "remainingEstimate"
            type: "string"
            description: "The remaining amount of time left in the estimate for the issue. For example: `4m`"

          - name: "remainingEstimateSeconds"
            type: "integer"
            description: "The remaining amount of time left in the estimate for the issue, in seconds. For example: `240`"

          - name: "timeSpent"
            type: "string"
            description: "The total amount of time tracked against the issue. For example: `6m`"

          - name: "timeSpentSeconds"
            type: "integer"
            description: "The total amount of time tracked against the issue, in seconds. For example: `360`"

    # End TIMETRACKING

    # Start VOTES

      - name: "votes"
        type: "object"
        description: ""
        object-attributes:
          - name: "hasVoted"
            type: "boolean"
            description: "If `true`, votes have been cast for the issue."

          - name: "self"
            type: "string"
            description: "The API URL for the votes in JIRA."

          - name: "votes"
            type: "integer"
            description: "The total number of votes for the issue."

    # End VOTES

    # Start WATCHES

      - name: "watches"
        type: "object"
        description: "Details about the number of users watching the issue."
        object-attributes:
          - name: "isWatching"
            type: "boolean"
            description: "If `true`, the issue is being watched."

          - name: "self"
            type: "string"
            description: "The API URL for the watches in JIRA."

          - name: "watchCount"
            type: "integer"
            description: "The total number of people watching the issue."

    # End WATCHES

  - name: "expand"
    type: "string"
    description: "This is a field used by Stitch to replicate data for this endpoint from JIRA's API."
---