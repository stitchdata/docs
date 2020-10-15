---
tap: "looker"
version: "1"
key: "git-branch"

name: "git_branches"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-looker/blob/master/tap_looker/schemas/git_branches.json"
description: |
  The `{{ table.name }}` table contains info about the git branches associated with projects in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
  name: "Get all git branches"
  doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/project#get_all_git_branches"

attributes:
   name: "name"
    type: "string"
    primary-key: true
    description: ""

  - name: "project_id"
    type: "string"
    primary-key: true
    description: ""
    foreign-key-id: "project-id"

  - name: "ahead_count"
    type: "integer"
    description: ""

  - name: "behind_count"
    type: "integer"
    description: ""

  - name: "commit_at"
    type: "integer"
    description: ""

  - name: "error"
    type: "string"
    description: ""

  - name: "is_local"
    type: "boolean"
    description: ""

  - name: "is_production"
    type: "boolean"
    description: ""

  - name: "is_remote"
    type: "boolean"
    description: ""

  - name: "message"
    type: "string"
    description: ""

  - name: "owner_name"
    type: "string"
    description: ""

  - name: "personal"
    type: "boolean"
    description: ""

  - name: "readonly"
    type: "boolean"
    description: ""

  - name: "ref"
    type: "string"
    description: ""

  - name: "remote"
    type: "string"
    description: ""

  - name: "remote_name"
    type: "string"
    description: ""

  - name: "remote_ref"
    type: "string"
    description: ""
---