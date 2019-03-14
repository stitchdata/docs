---
tap: "gitlab"
# version: ""

name: "projects"
doc-link: https://gitlab.com/help/api/projects.md#list-all-projects
singer-schema: https://github.com/singer-io/tap-gitlab/blob/master/tap_gitlab/schemas/projects.json
description: |
  The `projects` table contains info about specific projects.

replication-method: "Key-based Incremental"
api-method:
  name: "listAllProjects"
  doc-link: https://gitlab.com/help/api/projects.md#list-all-projects

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The project ID."

  - name: "last_activity_at"
    type: "date-time"
    replication-key: true
    description: "The time of the last activity associated with the project."

  - name: "approvals_before_merge"
    type: "integer"
    description: "The number of users who should approve merge requests by default."

  - name: "archived"
    type: "boolean"
    description: "Indicates if the project has been archived."

  - name: "avatar_url"
    type: "string"
    description: "The URL of the avatar associated with the project."

  - name: "builds_enabled"
    type: "boolean"
    description: "Indicates if build are enabled for the project."

  - name: "container_registry_enabled"
    type: "boolean"
    description: "Indicates if the container registry is enabled for the project."

  - name: "created_at"
    type: "date-time"
    description: "The time the project was created."

  - name: "creator_id"
    type: "integer"
    description: "The ID of the user who created the project."

  - name: "default_branch"
    type: "string"
    description: "The name of the project's default branch."

  - name: "description"
    type: "string"
    description: "The project's description."

  - name: "forks_count"
    type: "integer"
    description: "The total number of forks associated with the project."

  - name: "http_url_to_repo"
    type: "string"
    description: "The `http` URL to the project's repository."

  - name: "issues_enabled"
    type: "boolean"
    description: "Indicates if issues are enabled for the project."

  - name: "lfs_enabled"
    type: "boolean"
    description: "Indicates if LFS is enabled for the project."

  - name: "merge_requests_enabled"
    type: "boolean"
    description: "Indicates if merge requests are enabled for the project."

  - name: "name"
    type: "string"
    description: "The name of the project."

  - name: "name_with_namespace"
    type: "string"
    description: "The namespace of the project and the project name, e.g. `namespace/project_name`"

  - name: "namespace"
    type: "object"
    description: "Details about the namespace the project is associated with."
    subattributes:
      - name: "id"
        type: "integer"
        description: "The namespace ID."

      - name: "kind"
        type: "string"
        description: "The kind of namespace. Ex: `group`"

      - name: "name"
        type: "string"
        description: "The name of the namespace."

      - name: "path"
        type: "string"
        description: "The path of the namespace."

  - name: "only_allow_merge_if_all_discussions_are_resolved"
    type: "boolean"
    description: "Indicates if merge requests can only be merged when all discussions are resolved."

  - name: "only_allow_merge_if_build_succeeds"
    type: "boolean"
    description: "Indicates if merges are allowed only if builds succeed."

  - name: "open_issues_count"
    type: "integer"
    description: "The total number of open issues."

  - name: "owner_id"
    type: "integer"
    description: "The ID of the project's owner."

  - name: "path"
    type: "string"
    description: "The path of the project."

  - name: "path_with_namespace"
    type: "string"
    description: "The project's path with the namespace, e.g. `project_path/project_namespace`"

  - name: "permissions"
    type: "object"
    description: "Details about the group and project-level permissions associated with the project."
    subattributes:
      - name: "group_access"
        type: "object"
        description: "Details about the group access permissions associated with the project."
        subattributes:
          - name: "access_level"
            type: "integer"
            description: "The group's access level."

          - name: "notification_level"
            type: "integer"
            description: "The group's notification level."

      - name: "project_access"
        type: "object"
        description: "Details about the access permissions associated with the project."
        subattributes:
          - name: "access_level"
            type: "integer"
            description: "The access level for the project."

          - name: "notification_level"
            type: "integer"
            description: "The notification level for the project."

  - name: "public"
    type: "boolean"
    description: "Indicates if the project is public."

  - name: "public_builds"
    type: "boolean"
    description: "Indicates if builds are public for the project."

  - name: "request_access_enabled"
    type: "boolean"
    description: "Indicates if request access is enabled."

  - name: "shared_runners_enabled"
    type: "boolean"
    description: "Indicates if shared runners are enabled for the project."

  - name: "shared_with_groups"
    type: "array"
    description: "Details about groups the project has been shared with."
    subattributes:
      - name: "group_id"
        type: "integer"
        description: "The ID of the group the project was shared with."

      - name: "group_name"
        type: "string"
        description: "The name of the group the project was shared with."

      - name: "group_access_level"
        type: "integer"
        description: "The access level of the group the project was shared with."

  - name: "snippets_enabled"
    type: "boolean"
    description: "Indicates if snippets are enabled for the project."

  - name: "ssh_url_to_repo"
    type: "string"
    description: "The SSH URL of the project's repository."

  - name: "star_count"
    type: "integer"
    description: "The total number of stars for the project."

  - name: "tag_list"
    type: "array"
    description: "A list of tags applied to the project."
    subattributes:
      - name: "value"
        type: "string"
        description: "The name of the tag."

  - name: "visibility_level"
    type: "integer"
    description: "The visibility level for the project."

  - name: "web_url"
    type: "string"
    description: "The URL of the project."

  - name: "wiki_enabled"
    type: "boolean"
    description: "Indicates if the wiki is enabled for the project."
---