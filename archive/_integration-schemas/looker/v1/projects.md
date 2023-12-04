---
tap: "looker"
version: "1"
key: "project"

name: "projects"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-looker/blob/master/tap_looker/schemas/projects.json"
description: |
  The `{{ table.name }}` table contains info about the projects in your {{ integration.display_name }} instance.

replication-method: "Full Table"

api-method:
  name: "Get all projects"
  doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/project#get_all_projects"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The project ID."
    foreign-key-id: "project-id"

  - name: "allow_warnings"
    type: "boolean"
    description: ""

  - name: "deploy_secret"
    type: "string"
    description: ""

  - name: "folders_enabled"
    type: "boolean"
    description: ""

  - name: "git_password"
    type: "string"
    description: ""

  - name: "git_password_user_attribute"
    type: "string"
    description: ""

  - name: "git_remote_url"
    type: "string"
    description: ""

  - name: "git_service_name"
    type: "string"
    description: ""

  - name: "git_username"
    type: "string"
    description: ""

  - name: "git_username_user_attribute"
    type: "string"
    description: ""

  - name: "is_example"
    type: "boolean"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "pull_request_mode"
    type: "string"
    description: ""

  - name: "unset_deploy_secret"
    type: "boolean"
    description: ""

  - name: "uses_git"
    type: "boolean"
    description: ""

  - name: "validation_required"
    type: "boolean"
    description: ""
---