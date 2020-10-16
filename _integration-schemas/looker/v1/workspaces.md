---
tap: "looker"
version: "1"
key: "workspace"

name: "workspaces"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-looker/blob/master/tap_looker/schemas/workspaces.json"
description: |
  The `{{ table.name }}` table contains info about the workspaces available to the user who authorized the {{ integration.display_name }} integration in Stitch.

replication-method: "Full Table"

api-method:
  name: "Get all workspaces"
  doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/workspace#get_all_workspaces"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The workspace ID."
    foreign-key-id: "workspace-id"

  - name: "projects"
    type: "array"
    description: ""
    subattributes:
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

      - name: "id"
        type: "string"
        description: ""
        foreign-key-id: "project-id"

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