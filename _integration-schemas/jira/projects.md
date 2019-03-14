---
tap: "jira"
version: "1.0"

name: "projects"
doc-link: "https://developer.atlassian.com/cloud/jira/platform/rest/v2/#api-api-2-project-get"
singer-schema: "https://github.com/singer-io/tap-jira/blob/master/tap_jira/schemas/projects.json"
description: |
  The `{{ table.name }}` table contains info about the projects in your {{ integration.display_name }} account.

  **Note**: Stitch will only replicate data from the projects that the user whose credentials are [authenticating the integration](#add-stitch-data-source) can access. If there are missing projects, verify that the authenticating user (found in the integration's {{ app.page-names.int-settings }} page) has access to the missing projects.

replication-method: "Full Table"

api-method:
    name: "Get all projects"
    doc-link: "https://developer.atlassian.com/cloud/jira/platform/rest/v2/#api-api-2-project-get"
    
attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The project ID."
    foreign-key-id: "project-id"

  - name: "assigneeType"
    type: "string"
    description: |
      The default assignee when creating issues for the project. Possible values are:

      - `PROJECT_LEAD`
      - `UNASSIGNED`

  - name: "avatarUrls"
    type: "object"
    description: "The URLs associated with the avatars used by the project."
    subattributes:
      - name: "16x16"
        type: "string"
        description: "The URL of the project's 16x16 avatar."

      - name: "24x24"
        type: "string"
        description: "The URL of the project's 24x24 avatar."

      - name: "32x32"
        type: "string"
        description: "The URL of the project's 32x32 avatar."

      - name: "48x48"
        type: "string"
        description: "The URL of the project's 48x48 avatar."

  - name: "components"
    type: "array"
    description: "A list of the components contained in the project."
    subattributes:
      - name: "id"
        type: "string"
        primary-key: true
        description: |
          The component ID.

          {% assign description-type = "assignee" %}

      - name: "assignee"
        type: "object"
        description: ""
        subattributes: &userDetails
          - name: "accountId"
            type: "string"
            description: "The {{ description-type }}'s account ID."

          - name: "active"
            type: "boolean"
            description: "Indicates if the {{ description-type }} is active."

          - name: "applicationRoles"
            type: "object"
            description: "Application roles associated with the {{ description-type }}."
            subattributes:
              - name: "items"
                type: "array"
                description: "A list of application roles associated with the {{ description-type }}."
                subattributes:
                  - name: "name"
                    type: "string"
                    description: "The name of the application role."

                  - name: "self"
                    type: "string"
                    description: "The URL of the application role."

              - name: "max-results"
                type: "integer"
                description: ""

              - name: "size"
                type: "integer"
                description: ""

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
            description: "The {{ description-type }}'s display name. Depending on the user's privacy setting, this may be returned as null."

          - name: "emailAddress"
            type: "string"
            description: "The {{ description-type }}'s email address. Depending on the user's privacy setting, this may be returned as null."

          - name: "expand"
            type: "string"
            description: "Details of expands available for the {{ description-type }} details."

          - name: "groups"
            type: "object"
            description: "Details about the groups the {{ description-type }} is associated with."
            subattributes:
              - name: "items"
                type: "array"
                description: "The groups the {{ description-type }} is associated with."
                subattributes:
                  - name: "name"
                    type: "string"
                    description: "The name of the group."

                  - name: "self"
                    type: "string"
                    description: "The URL for the group."

              - name: "max-results"
                type: "integer"
                description: ""

              - name: "size"
                type: "integer"
                description: ""

          - name: "key"
            type: "string"
            description: "The key of the {{ description-type }}."
            foreign-key-id: "user-key"

          - name: "locale"
            type: "string"
            description: "The locale of the {{ description-type }}. Depending on the user's privacy setting, this may be returned as null."

          - name: "name"
            type: "string"
            description: "The name of the {{ description-type }}."

          - name: "self"
            type: "string"
            description: "The URL for the {{ description-type }}."

          - name: "timeZone"
            type: "string"
            description: "The time zone specified in the {{ description-type }}'s profile. Depending on the user's privacy setting, this may be returned as null."

      - name: "assigneeType"
        type: "string"
        description: |
          The user type used to determine the assignee for issues created with this component. Possible values are:

          - `COMPONENT_LEAD` - The assignee to any issues created with this component is nominally the lead for the component.
          - `PROJECT_DEFAULT` - The assignee to any issues created with this component is nominally the default assignee for the project the component is in.
          - `PROJECT_LEAD` - The assignee to any issues created with this component is nominally the lead for the project the component is in.
          - `UNASSIGNED` - An assignee is not set for issues created with this component.

      - name: "description"
        type: "string"
        description: "A description of the component."

      - name: "isAssigneeTypeValid"
        type: "boolean"
        description: |
          Indicates if the `assigneeType` is valid.

          {% assign description-type = "lead user" %}

      - name: "lead"
        type: "object"
        description: |
          Details about the lead user associated with the project.
        subattributes: *userDetails

      - name: "leadUserName"
        type: "string"
        description: "The username of the component's lead user."

      - name: "name"
        type: "string"
        description: "The name of the component."

      - name: "project"
        type: "string"
        description: "The key of the project to which the component is assignee."

      - name: "projectId"
        type: "integer"
        description: |
          **Not used.**

          {% assign description-type = "assignee" %}

      - name: "realAssignee"
        type: "object"
        description: |
          Details about the real assignee associated with the component.
        subattributes: *userDetails

      - name: "realAssigneeType"
        type: "string"
        description: |
          The actual type of the assignee to issues created with this component, when an assignee cannot be set from the `assigneeType`. Possible values are:

          - `COMPONENT_LEAD` - When `assigneeType` is `COMPONENT_LEAD` and the component lead has permission to be assigned issues in the project that the component is in.
          - `PROJECT_LEAD` - When `assigneeType` is `PROJECT_LEAD` and the project lead has permission to be assigneed issues in the project that the component is in.
          - `UNASSIGNED` - When `assigneeType` is `UNASSIGNED` and {{ integration.display_name }} is configured to allow unassigned issues.
          - `PROJECT_DEFAULT` - When none of the preceeding cases are true.

      - name: "self"
        type: "string"
        description: "The URL of the component."

  - name: "description"
    type: "string"
    description: "A description of the project."

  - name: "email"
    type: "string"
    description: "The email address associated with the project."

  - name: "expand"
    type: "string"
    description: "Details of expands available for project details."

  - name: "issueTypes"
    type: "array"
    description: "A list of the issue types available in the project."
    subattributes:
      - name: "avatarId"
        type: "integer"
        description: "The ID of the issue type's avatar."

      - name: "description"
        type: "string"
        description: "The description of the issue type."

      - name: "iconUrl"
        type: "string"
        description: "The URL of the issue type's avatar."

      - name: "id"
        type: "string"
        description: "The ID of the issue type."

      - name: "name"
        type: "string"
        description: "The name of the issue type."

      - name: "self"
        type: "string"
        description: "The URL of the issue type."

      - name: "subtask"
        type: "boolean"
        description: "Indicates whether the issue type can be used to create subtasks."

  - name: "key"
    type: "string"
    description: |
      The project key.

      {% assign description-type = "lead user" %}

  - name: "lead"
    type: "object"
    description: "Details about the lead user associated with the project."
    subattributes: *userDetails

  - name: "name"
    type: "string"
    description: "The name of the project."

  - name: "projectCategory"
    type: "object"
    description: "The category associated with the project."
    subattributes:
      - name: "description"
        type: "string"
        description: "The description of the project category."

      - name: "id"
        type: "string"
        description: "The ID of the project category."
        foreign-key-id: "project-category-id"

      - name: "name"
        type: "string"
        description: "The name of the project category."

      - name: "self"
        type: "string"
        description: "The URL of the project category."

  - name: "projectKeys"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "projectTypeKey"
    type: "string"
    description: |
      The project type of the project. Possible values are:

      - `ops`
      - `software`
      - `service_desk`
      - `business`

  - name: "roles"
    type: "object"
    description: "The roles defined in the project."
    subattributes:
      - name: "varies"
        type: "string"
        description: "The role defined in the project."

  - name: "self"
    type: "string"
    description: "The URL of the project."

  - name: "simplified"
    type: "boolean"
    description: "Indicates whether the project is simplified."

  - name: "url"
    type: "string"
    description: "The URL of the project."
---