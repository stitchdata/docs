---
tap: "jira"
version: "1.0"

name: "versions"
doc-link: https://docs.atlassian.com/jira/REST/cloud/#api/2/project-getProjectVersionsPaginated
singer-schema: https://github.com/singer-io/tap-jira/blob/master/tap_jira/schemas/versions.json
description: |
  The `versions` table contains info about the versions in your JIRA account.

replication-method: "Full Table"

api-method:
  name: getAllProjectVersionsPaginated
  doc-link: https://docs.atlassian.com/jira/REST/cloud/#api/2/project-getProjectVersionsPaginated

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The version ID."

  - name: "self"
    type: "string"
    description: "The API URL of the version in JIRA."

  - name: "description"
    type: "string"
    description: "The description of the version."

  - name: "name"
    type: "string"
    description: "The name of the version."

  - name: "archived"
    type: "boolean"
    description: "If `true`, the version has been archived."

  - name: "released"
    type: "boolean"
    description: "If `true`, the version has been released."

  - name: "releaseDate"
    type: "date-time"
    description: "The date of the version's release."

  - name: "overdue"
    type: "boolean"
    description: "If `true`, the version is overdue."

  - name: "userStartDate"
    type: "date-time"
    description: ""

  - name: "startDate"
    type: "date-time"
    description: "The version's start date."

  - name: "userReleaseDate"
    type: "date-time"
    description:

  - name: "project"
    type: "string"
    description:

  - name: "projectId"
    type: "string"
    description: "The ID of the project associated with the version."
    foreign-key: true

  - name: "moveUnfixedIssuesTo"
    type: "string"
    description:

  - name: "operations"
    type: "array"
    description:
    array-attributes:
      - name: "id"
        type: "string"
        description:

      - name: "styleClass"
        type: "string"
        description:

      - name: "iconClass"
        type: "string"
        description:

      - name: "label"
        type: "string"
        description:

      - name: "title"
        type: "string"
        description:

      - name: "href"
        type: "string"
        description:

      - name: "weight"
        type: "integer" 
        description:

  - name: "remoteLinks"
    type: "array"
    description:
    array-attributes:
      - name: "self"
        type: "string"
        description:

      - name: "name"
        type: "string"
        description:

  - name: "expand"
    type: "string"
    description: "This is a field used by Stitch to replicate data for this endpoint from JIRA's API."

---