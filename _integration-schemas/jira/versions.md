---
tap: "jira"
version: "1.0"

name: "versions"
doc-link: "https://developer.atlassian.com/cloud/jira/platform/rest/v2/#api-api-2-project-projectIdOrKey-versions-get"
singer-schema: "https://github.com/singer-io/tap-jira/blob/master/tap_jira/schemas/versions.json"
description: |
  The `{{ table.name }}` table contains info about versions in your {{ integration.display_name }} account.

  #### Replication requirements

  **Note**: To replicate this data:

     1. The [`projects`](#projects) table must also be set to replicate, and
     2. The `Browse Projects` [project {{ integration.display_name }} permission]({{ integration.project-permissions-doc }}){:target="new"} is required. Refer to [{{ integration.display_name }}'s API documentation]({{ table.doc-link }}){:target="new"} for more info.

replication-method: "Full Table"

api-method:
    name: "Get project versions"
    doc-link: "https://developer.atlassian.com/cloud/jira/platform/rest/v2/#api-api-2-project-projectIdOrKey-versions-get"
    
attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The project version ID."
    # foreign-key-id: "version-id"

  - name: "archived"
    type: "boolean"
    description: "Indicates whether the version is archived."

  - name: "description"
    type: "string"
    description: "The description of the vrsion."

  - name: "expand"
    type: "string"
    description: "Details about the expands available for the project version."

  - name: "moveUnfixedIssuesTo"
    type: "string"
    description: "The URL of the self link to the version to which all unfixed issues are moved when a version is released."

  - name: "name"
    type: "string"
    description: "The name of the project version."

  - name: "operations"
    type: "array"
    description: "The list of operations available in the version."
    subattributes:
      - name: "href"
        type: "string"
        description: ""

      - name: "iconClass"
        type: "string"
        description: "The icon class of the operation."

      - name: "id"
        type: "string"
        description: "The ID of the operation."

      - name: "label"
        type: "string"
        description: "The label of the operation."

      - name: "styleClass"
        type: "string"
        description: "The style class of the operation."

      - name: "title"
        type: "string"
        description: "The title of the operation."

      - name: "weight"
        type: "integer"
        description: "The weight of the operation."

  - name: "overdue"
    type: "boolean"
    description: "Indicates whether the project version is overdue."

  - name: "project"
    type: "string"
    description: "**This field has been deprecated by {{ integration.display_name }}.**"

  - name: "projectId"
    type: "integer"
    description: "The ID of the project this version is attached to."
    foreign-key-id: "project-id"

  - name: "releaseDate"
    type: "date-time"
    description: "The release date of the project version, expressed in ISO 8601 format."

  - name: "released"
    type: "boolean"
    description: "Indicates whether the project version has been released."

  - name: "remotelinks"
    type: "array"
    description: "The list of remote links stored against the project version."
    subattributes:
      - name: "link"
        type: "string"
        description: "The URL of the remote link."

      - name: "name"
        type: "string"
        description: "The name of the remote link."

      - name: "self"
        type: "uri"
        description: "The URL of the remote link details."

  - name: "self"
    type: "string"
    description: "The URL of the project version."

  - name: "startDate"
    type: "date-time"
    description: "The start date of the version, expressed in ISO 8601 format."

  - name: "userReleaseDate"
    type: "date-time"
    description: "The date on which work on this version is expected to finish, in `Day/Month/Year` format."

  - name: "userStartDate"
    type: "date-time"
    description: "The date on which work on this project version is expected to start, in `Day/Month/Year` format."
---