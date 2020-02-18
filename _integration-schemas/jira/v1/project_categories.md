---
tap: "jira"
version: "1"
key: "project-category"

name: "project_categories"
doc-link: "https://developer.atlassian.com/cloud/jira/platform/rest/v2/#api-api-2-projectCategory-get"
singer-schema: "https://github.com/singer-io/tap-jira/tree/77206190933146b7cf51f14bfc7aaf670539ca5f/tap_jira/schemas/project_categories.json"
description: |
  The `{{ table.name }}` table contains info about project categories.

replication-method: "Full Table"

api-method:
    name: "Get all project categories"
    doc-link: "https://developer.atlassian.com/cloud/jira/platform/rest/v2/#api-api-2-projectCategory-get"
    
attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The project category ID."
    foreign-key-id: "project-category-id"

  - name: "description"
    type: "string"
    description: "The description of the project category."

  - name: "name"
    type: "string"
    description: "The name of the project category."

  - name: "self"
    type: "uri"
    description: "The URL of the project category."
---