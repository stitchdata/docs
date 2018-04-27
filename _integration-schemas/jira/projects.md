---
tap: "jira"
version: "1.0"

name: "projects"
doc-link: https://docs.atlassian.com/jira/REST/ondemand/#api/2/project-getAllProjects
singer-schema: ## link to the JSON schema file in the integration's Singer repo
description: |
  The `projects` table contains info about individual projects in your JIRA account.

replication-method: "Full Table"

api-method:
  name: getAllProjects
  doc-link: https://docs.atlassian.com/jira/REST/ondemand/#api/2/project-getAllProjects


attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The project ID."

  - name: "key"
    type: "string"
    description: "The project key."

  - name: "assigneeType"
    type: "string"
    description: |
      Possible values are:
      - `PROJECT_LEAD`
      - `UNASSIGNED`

  - name: "name"
    type: "string"
    description: "The name of the project."

  - name: "projectTypeKey"
    type: "string"
    description: "The key of the project type applied to the project."
    foreign-key: true

  - name: "self"
    type: "string"
    description: "The API URL of the project in JIRA."

  - name: "simplified"
    type: "boolean"
    description: ""

  - name: "avatarUrls"
    type: "object"
    description: "The URLs of the avatars associated with the project."
    object-attributes:
      - name: "16x16"
        type: "string"
        description: "The URL of the 16x16 avatar associated with the project."

      - name: "24x24"
        type: "string"
        description: "The URL of the 24x24 avatar associated with the project."

      - name: "32x32"
        type: "string"
        description: "The URL of the 32x32 avatar associated with the project."

      - name: "48x48"
        type: "string"
        description: "The URL of the 48x48 avatar associated with the project."

# Start COMPONENTS

  - name: "components"
    type: "array"
    description: "Details about the components that make up the project."
    array-attributes:
      - name: "id"
        type: "string"
        description: "The project component ID."

      - name: "name"
        type: "string"
        description: "The name of the project component."

      - name: "description"
        type: "string"
        description: "The description of the project component."

      - name: "self"
        type: "string"
        description: "The API URL of the project component in JIRA."

      - name: "leadUserName"
        type: "string"
        description: "The username of the lead associated with the project component."

    # Start LEAD
      - name: "lead"
        type: "array"
        description: "Details about the lead associated with the project component."
        array-attributes: &component-user
          - name: "key"
            type: "string"
            description: "The key of the project component {{ subattribute.name }}."
            foreign-key: true
            table: "users"

          - name: "accountId"
            type: "string"
            description: "The account ID associated with the project component {{ subattribute.name }}."

          - name: "active"
            type: "boolean"
            description: "If `true`, the project component {{ subattribute.name }} is active."

          - name: "displayName"
            type: "string"
            description: "The display name of the project component {{ subattribute.name }}."

          - name: "name"
            type: "string"
            description: "The name of the project component {{ subattribute.name }}."

          - name: "self"
            type: "string"
            description: "The URL associated with the project component {{ subattribute.name }}."

        # Start AVATARURLS

          - name: "avatarUrls"
            type: "object"
            description: "The URLs associated with the avatars used by the project component {{ subattribute.name }}."
            object-attributes:
              - name: "16x16"
                type: "string"
                description: "The URL of the project component {{ subattribute.name }}'s 16x16 avatar."

              - name: "24x24"
                type: "string"
                description: "The URL of the project component {{ subattribute.name }}'s 24x24 avatar."

              - name: "32x32"
                type: "string"
                description: "The URL of the project component {{ subattribute.name }}'s 32x32 avatar."

              - name: "48x48"
                type: "string"
                description: "The URL of the project component {{ subattribute.name }}'s 48x48 avatar."

        # End AVATARURLS

    # End LEAD

      - name: "assigneeType"
        type: "string"
        description: |
          The type of assignee the project component can have. Possible values are:

          - `PROJECT_DEFAULT`
          - `COMPONENT_LEAD`
          - `PROJECT_LEAD`
          - `UNASSIGNED`

    # Start ASSIGNEE

      - name: "assignee"
        type: "object"
        description: "Details about the assignee assigned to the project component."
        object-attributes: *component-user

    # End ASSIGNEE

    # Start REALASSIGNEE

      - name: "realAssignee"
        type: "object"
        description: "Details about the real assignee assigned to the project component."
        object-attributes:
          - name: "key"
            type: "string"
            description: "The key of the real assignee."
            foreign-key: true
            table: "users"

          - name: "accountId"
            type: "string"
            description: "The account ID associated with the real assignee."

          - name: "active"
            type: "boolean"
            description: "If `true`, the real assignee is active."

          - name: "displayName"
            type: "string"
            description: "The display name of the real assignee."

          - name: "name"
            type: "string"
            description: "The name of the real assignee."

          - name: "self"
            type: "string"
            description: "The URL associated with the real assignee."

        # Start AVATARURLS

          - name: "avatarUrls"
            type: "object"
            description: "The URLs associated with the avatars used by the real assignee."
            object-attributes:
              - name: "16x16"
                type: "string"
                description: "The URL of the real assignee's 16x16 avatar."

              - name: "24x24"
                type: "string"
                description: "The URL of the real assignee's 24x24 avatar."

              - name: "32x32"
                type: "string"
                description: "The URL of the real assignee's 32x32 avatar."

              - name: "48x48"
                type: "string"
                description: "The URL of the real assignee's 48x48 avatar."

        # End AVATARURLS

    # End REALASSIGNEE

      - name: "realAssigneeType"
        type: "string"
        description: |
          The type of assignee the real assignee for the project component can have. Possible values are:

          - `PROJECT_DEFAULT`
          - `COMPONENT_LEAD`
          - `PROJECT_LEAD`
          - `UNASSIGNED`

      - name: "isAssigneeTypeValid"
        type: "boolean"
        description: ""

      - name: "project"
        type: "string"
        description: "The key of the project associated with the component."

      - name: "projectId"
        type: "integer"
        description: "The ID of the project associated with the component."

# End COMPONENTS

# Start LEAD

  - name: "lead"
    type: "object"
    description: "Details about the project lead."
    object-attributes:
      - name: "key"
        type: "string"
        description: "The key of the project {{ attribute.name }}."
        foreign-key: true
        table: "users"

      - name: "accountId"
        type: "string"
        description: "The account ID associated with the project {{ attribute.name }}."

      - name: "active"
        type: "boolean"
        description: "If `true`, the project {{ attribute.name }} is active."

      - name: "displayName"
        type: "string"
        description: "The display name of the project {{ attribute.name }}."

      - name: "name"
        type: "string"
        description: "The name of the project {{ attribute.name }}."

      - name: "self"
        type: "string"
        description: "The URL associated with the project {{ attribute.name }}."

    # Start AVATARURLS

      - name: "avatarUrls"
        type: "object"
        description: "The URLs associated with the avatars used by the project {{ attribute.name }}."
        object-attributes:
          - name: "16x16"
            type: "string"
            description: "The URL of the project {{ attribute.name }}'s 16x16 avatar."

          - name: "24x24"
            type: "string"
            description: "The URL of the project {{ attribute.name }}'s 24x24 avatar."

          - name: "32x32"
            type: "string"
            description: "The URL of the project {{ attribute.name }}'s 32x32 avatar."

          - name: "48x48"
            type: "string"
            description: "The URL of the project {{ attribute.name }}'s 48x48 avatar."

    # End AVATARURLS

  # End LEAD

# Start PROJECTCATEGORY

  - name: "projectCategory"
    type: "object"
    description: "Details about the project's category."
    object-attributes:
      - name: "id"
        type: "string"
        description: "The project category ID."
        foreign-key: true
        table: "project_categories"

      - name: "name"
        type: "string"
        description: "The name of the project category."

      - name: "description"
        type: "string"
        description: "The description of the project category."

      - name: "self"
        type: "string"
        description: "The API URL for the project category in JIRA."

# End PROJECTCATEGORY

  - name: "projectKeys"
    type: "array"
    description: "The key(s) associated with the project."
    array-attributes:
      - name: "value"
        type: "string"
        description: "The project key."

  - name: "expand"
    type: "string"
    description: "This is a field used by Stitch to replicate data for this endpoint from JIRA's API."
---