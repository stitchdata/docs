---
# -------------------------- #
#        Table Details       #
# -------------------------- #

tap: "github"
version: "2"
key: "issue-event"

name: "issue_events"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-github/blob/master/tap_github/schemas/issue_events.json"
description: |
  The `{{ table.name }}` table contains info about issue events in the repositories specified for the integration.


# -------------------------- #
#    Replication Details     #
# -------------------------- #

api-method:
  name: "List issue events for a repository"
  doc-link: "https://docs.github.com/en/rest/reference/issues#list-issue-events-for-a-repository"

replication-method: "Key-based Incremental"
replication-key:
  name: "since"
  based-on: "`updated_at` if non-NULL; otherwise `created_at`"
  tooltip: "This is a query parameter used to extract new/updated data from GitHub. It will not be included in the table's fields."


# -------------------------- #
#       Table Attributes     #
# -------------------------- #

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The issue event ID."
    # foreign-key-id: "issue-event-id"

  - name: "_sdc_repository"
    type: "string"
    description: ""

  - name: "actor"
    type: "object"
    description: ""
    subattributes: &user-attributes
      - name: "name"
        type: "string"
        description: "The name of the user."
        
      - name: "email"
        type: "string"
        description: "The email address of the user."

      - name: "login"
        type: "string"
        description: "The login name of the user."

      - name: "id"
        type: "string"
        description: "The ID of the user."

      - name: "node_id"
        type: "string"
        description: "The node ID of the user."

      - name: "avatar_url"
        type: "string"
        description: "The URL of the avatar of the user."

      - name: "gravatar_id"
        type: "string"
        description: "The URL of the Gravatar of the user."

      - name: "url"
        type: "string"
        description: "The API URL of the user."

      - name: "html_url"
        type: "string"
        description: "The GitHub URL of the user."

      - name: "followers_url"
        type: "string"
        description: "The URL to the user's followers page."

      - name: "following_url"
        type: "string"
        description: "The URL to the user's following page."

      - name: "gists_url"
        type: "string"
        description: "The URL to the user's gists page."

      - name: "starred_url"
        type: "string"
        description: "The URL to the user's starred page."

      - name: "subscriptions_url"
        type: "string"
        description: "The URL to the user's subscriptions page."

      - name: "organizations_url"
        type: "string"
        description: "The URL to the user's organizations page."

      - name: "repos_url"
        type: "string"
        description: "The URL to the user's repositories page."

      - name: "events_url"
        type: "string"
        description: "The URL to the user's events page."

      - name: "received_events_url"
        type: "string"
        description: "The URL to the user's received events page."

      - name: "type"
        type: "string"
        description: "The type of the user."

      - name: "site_admin"
        type: "string"
        description: "Indicates if the user is a site administrator."
        
      - name: "starred_at"
        type: "string"
        description: ""

  - name: "assignee"
    type: "object"
    description: ""
    subattributes: *user-attributes

  - name: "assigner"
    type: "object"
    description: ""
    subattributes: *user-attributes

  - name: "commit_id"
    type: "string"
    description: ""
    foreign-key-id: "commit-id"

  - name: "commit_url"
    type: "string"
    description: ""

  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "event"
    type: "string"
    description: ""

  - name: "issue"
    type: "object"
    description: ""
    subattributes:
      - name: "active_lock_reason"
        type: "string"
        description: ""

      - name: "assignee"
        type: "object"
        description: ""
        subattributes: *user-attributes

      - name: "assignees"
        type: "array"
        description: ""
        subattributes: *user-attributes

      - name: "author_association"
        type: "string"
        description: ""

      - name: "body"
        type: "string"
        description: ""

      - name: "closed_at"
        type: "date-time"
        description: ""

      - name: "closed_by"
        type: "object"
        description: ""
        subattributes: *user-attributes

      - name: "comments"
        type: "integer"
        description: ""

      - name: "comments_url"
        type: "string"
        description: ""

      - name: "created_at"
        type: "date-time"
        description: ""

      - name: "events_url"
        type: "string"
        description: ""

      - name: "html_url"
        type: "string"
        description: ""

      - name: "id"
        type: "integer"
        description: ""
        foreign-key-id: "issue-id"

      - name: "labels"
        type: "array"
        description: ""
        subattributes:
          - name: "color"
            type: "string"
            description: ""

          - name: "default"
            type: "boolean"
            description: ""

          - name: "description"
            type: "string"
            description: ""

          - name: "id"
            type: "integer"
            description: ""
            foreign-key-id: "label-id"

          - name: "name"
            type: "string"
            description: ""

          - name: "node_id"
            type: "string"
            description: ""

          - name: "url"
            type: "string"
            description: ""

      - name: "labels_url"
        type: "string"
        description: ""

      - name: "locked"
        type: "boolean"
        description: ""

      - name: "milestone"
        type: "object"
        description: ""
        subattributes:
          - name: "closed_at"
            type: "date-time"
            description: ""

          - name: "closed_issues"
            type: "integer"
            description: ""

          - name: "created_at"
            type: "date-time"
            description: ""

          - name: "creator"
            type: "object"
            description: ""
            subattributes: *user-attributes

          - name: "description"
            type: "string"
            description: ""

          - name: "due_on"
            type: "date-time"
            description: ""

          - name: "html_url"
            type: "string"
            description: ""

          - name: "id"
            type: "integer"
            description: ""
            foreign-key-id: "milestone-id"

          - name: "labels_url"
            type: "string"
            description: ""

          - name: "node_id"
            type: "string"
            description: ""

          - name: "number"
            type: "integer"
            description: ""

          - name: "open_issues"
            type: "integer"
            description: ""

          - name: "state"
            type: "string"
            description: ""

          - name: "title"
            type: "string"
            description: ""

          - name: "updated_at"
            type: "date-time"
            description: ""

          - name: "url"
            type: "string"
            description: ""

      - name: "node_id"
        type: "string"
        description: ""

      - name: "number"
        type: "integer"
        description: ""

      - name: "performed_via_github_app"
        type: "object, string"
        description: ""
        subattributes: &performed-via-github-app
          - name: "id"
            type: "integer"
            description: ""
            
          - name: "slug"
            type: "string"
            description: ""
            
          - name: "node_id"
            type: "string"
            description: ""
            
          - name: "owner"
            type: "object"
            description: ""
            subattributes: *user-attributes
            
          - name: "name"
            type: "string"
            description: ""
            
          - name: "description"
            type: "string"
            description: ""
            
          - name: "external_url"
            type: "string"
            description: ""
            
          - name: "html_url"
            type: "string"
            description: ""
            
          - name: "created_at"
            type: "date-time"
            description: ""
            
          - name: "updated_at"
            type: "date-time"
            description: ""
            
          - name: "permissions"
            type: "object"
            description: ""
            subattributes:
              - name: "issues"
                type: "string"
                description: ""
            
              - name: "checks"
                type: "string"
                description: ""
            
              - name: "metadata"
                type: "string"
                description: ""
            
              - name: "contents"
                type: "string"
                description: ""
            
              - name: "deployments"
                type: "string"
                description: ""
            
          - name: "events"
            type: "array"
            description: ""
            subattributes:
              - name: "item"
                type: "string"
                description: ""
            
          - name: "installations_count"
            type: "integer"
            description: ""
            
          - name: "client_id"
            type: "string"
            description: ""
            
          - name: "client_secret"
            type: "string"
            description: ""
            
          - name: "webhook_secret"
            type: "string"
            description: ""
            
          - name: "pem"
            type: "string"
            description: ""

      - name: "pull_request"
        type: "object"
        description: ""
        subattributes:
          - name: "diff_url"
            type: "string"
            description: ""

          - name: "html_url"
            type: "string"
            description: ""

          - name: "patch_url"
            type: "string"
            description: ""

          - name: "url"
            type: "string"
            description: ""

          - name: "merged_at"
            type: "string"
            description: ""

      - name: "reactions"
        type: "object"
        description: ""
        subattributes:
         - name: "url"
           type: "string"
           description: ""
           
         - name: "total_count"
           type: "integer"
           description: ""
           
         - name: "+1"
           type: "integer"
           description: ""
           
         - name: "-1"
           type: "integer"
           description: ""
           
         - name: "laugh"
           type: "integer"
           description: ""
           
         - name: "confused"
           type: "integer"
           description: ""
           
         - name: "heart"
           type: "integer"
           description: ""
           
         - name: "hooray"
           type: "integer"
           description: ""
           
         - name: "eyes"
           type: "integer"
           description: ""
           
         - name: "rocket"
           type: "integer"
           description: ""

      - name: "repository"
        type: "object"
        description: ""
        subattributes:
          - name: "id"
            type: "integer"
            description: ""
          
          - name: "node_id"
            type: "string"
            description: ""
          
          - name: "name"
            type: "string"
            description: ""
          
          - name: "full_name"
            type: "string"
            description: ""
          
          - name: "license"
            type: "object"
            description: ""
            subattributes:
              - name: "key"
                type: "string"
                description: ""
              
              - name: "name"
                type: "string"
                description: ""
              
              - name: "url"
                type: "string"
                description: ""
              
              - name: "spdx_id"
                type: "string"
                description: ""
              
              - name: "node_id"
                type: "string"
                description: ""
              
              - name: "html_url"
                type: "string"
                description: ""
              
          - name: "organization"
            type: "object"
            description: ""
            subattributes: *user-attributes
          
          - name: "forks"
            type: "integer"
            description: ""
          
          - name: "permissions"
            type: "object"
            description: ""
            subattributes: &pull-permissions
              - name: "pull"
                type: "boolean"
                description: ""
              - name: "triage"
                type: "boolean"
                description: ""

              - name: "push"
                type: "boolean"
                description: ""

              - name: "maintain"
                type: "boolean"
                description: ""

              - name: "admin"
                type: "boolean"
                description: ""
          
          - name: "owner"
            type: "object"
            description: ""
            subattributes: *user-attributes
          
          - name: "private"
            type: "boolean"
            description: ""
          
          - name: "html_url"
            type: "string"
            description: ""
          
          - name: "description"
            type: "string"
            description: ""
          
          - name: "fork"
            type: "boolean"
            description: ""
          
          - name: "url"
            type: "string"
            description: ""
          
          - name: "archive_url"
            type: "string"
            description: ""
          
          - name: "assignees_url"
            type: "string"
            description: ""
          
          - name: "blobs_url"
            type: "string"
            description: ""
          
          - name: "branches_url"
            type: "string"
            description: ""
          
          - name: "collaborators_url"
            type: "string"
            description: ""
          
          - name: "comments_url"
            type: "string"
            description: ""
          
          - name: "commits_url"
            type: "string"
            description: ""
          
          - name: "compare_url"
            type: "string"
            description: ""
          
          - name: "contents_url"
            type: "string"
            description: ""
          
          - name: "contributors_url"
            type: "string"
            description: ""
          
          - name: "deployments_url"
            type: "string"
            description: ""
          
          - name: "downloads_url"
            type: "string"
            description: ""
          
          - name: "events_url"
            type: "string"
            description: ""
          
          - name: "forks_url"
            type: "string"
            description: ""
          
          - name: "git_commits_url"
            type: "string"
            description: ""
          
          - name: "git_refs_url"
            type: "string"
            description: ""
          
          - name: "git_tags_url"
            type: "string"
            description: ""
          
          - name: "git_url"
            type: "string"
            description: ""
          
          - name: "issue_comment_url"
            type: "string"
            description: ""
          
          - name: "issue_events_url"
            type: "string"
            description: ""
          
          - name: "issues_url"
            type: "string"
            description: ""
          
          - name: "keys_url"
            type: "string"
            description: ""
          
          - name: "labels_url"
            type: "string"
            description: ""
          
          - name: "languages_url"
            type: "string"
            description: ""
          
          - name: "merges_url"
            type: "string"
            description: ""
          
          - name: "milestones_url"
            type: "string"
            description: ""
          
          - name: "notifications_url"
            type: "string"
            description: ""
          
          - name: "pulls_url"
            type: "string"
            description: ""
          
          - name: "releases_url"
            type: "string"
            description: ""
          
          - name: "ssh_url"
            type: "string"
            description: ""
          
          - name: "stargazers_url"
            type: "string"
            description: ""
          
          - name: "statuses_url"
            type: "string"
            description: ""
          
          - name: "subscribers_url"
            type: "string"
            description: ""
          
          - name: "subscription_url"
            type: "string"
            description: ""
          
          - name: "tags_url"
            type: "string"
            description: ""
          
          - name: "teams_url"
            type: "string"
            description: ""
          
          - name: "trees_url"
            type: "string"
            description: ""
          
          - name: "clone_url"
            type: "string"
            description: ""
          
          - name: "mirror_url"
            type: "string"
            description: ""
          
          - name: "hooks_url"
            type: "string"
            description: ""
          
          - name: "svn_url"
            type: "string"
            description: ""
          
          - name: "homepage"
            type: "string"
            description: ""
          
          - name: "language"
            type: "string"
            description: ""
          
          - name: "forks_count"
            type: "integer"
            description: ""
          
          - name: "stargazers_count"
            type: "integer"
            description: ""
          
          - name: "watchers_count"
            type: "integer"
            description: ""
          
          - name: "size"
            type: "integer"
            description: ""
          
          - name: "default_branch"
            type: "string"
            description: ""
          
          - name: "open_issues_count"
            type: "integer"
            description: ""
          
          - name: "is_template"
            type: "boolean"
            description: ""
          
          - name: "topics"
            type: "array"
            description: ""
            subattributes:
            - name: "items"
              type: "string"
              description: ""
            
          
          - name: "has_issues"
            type: "boolean"
            description: ""
          
          - name: "has_projects"
            type: "boolean"
            description: ""
          
          - name: "has_wiki"
            type: "boolean"
            description: ""
          
          - name: "has_pages"
            type: "boolean"
            description: ""
          
          - name: "has_downloads"
            type: "boolean"
            description: ""
          
          - name: "archived"
            type: "boolean"
            description: ""
          
          - name: "disabled"
            type: "boolean"
            description: ""
          
          - name: "visibility"
            type: "string"
            description: ""
          
          - name: "pushed_at"
            type: "string"
            description: ""
          
          - name: "created_at"
            type: "date-time"
            description: ""
          
          - name: "updated_at"
            type: "date-time"
            description: ""
          
          - name: "allow_rebase_merge"
            type: "boolean"
            description: ""
          
          - name: "template_repository"
            type: "object"
            description: ""
            subattributes:
              - name: "id"
                type: "integer"
                description: ""
              
              - name: "node_id"
                type: "string"
                description: ""
              
              - name: "name"
                type: "string"
                description: ""
              
              - name: "full_name"
                type: "string"
                description: ""
              
              - name: "owner"
                type: "object"
                description: ""
                subattributes: *user-attributes
              
              - name: "private"
                type: "boolean"
                description: ""
              
              - name: "html_url"
                type: "string"
                description: ""
              
              - name: "description"
                type: "string"
                description: ""
              
              - name: "fork"
                type: "boolean"
                description: ""
              
              - name: "url"
                type: "string"
                description: ""
              
              - name: "archive_url"
                type: "string"
                description: ""
              
              - name: "assignees_url"
                type: "string"
                description: ""
              
              - name: "blobs_url"
                type: "string"
                description: ""
              
              - name: "branches_url"
                type: "string"
                description: ""
              
              - name: "collaborators_url"
                type: "string"
                description: ""
              
              - name: "comments_url"
                type: "string"
                description: ""
              
              - name: "commits_url"
                type: "string"
                description: ""
              
              - name: "compare_url"
                type: "string"
                description: ""
              
              - name: "contents_url"
                type: "string"
                description: ""
              
              - name: "contributors_url"
                type: "string"
                description: ""
              
              - name: "deployments_url"
                type: "string"
                description: ""
              
              - name: "downloads_url"
                type: "string"
                description: ""
              
              - name: "events_url"
                type: "string"
                description: ""
              
              - name: "forks_url"
                type: "string"
                description: ""
              
              - name: "git_commits_url"
                type: "string"
                description: ""
              
              - name: "git_refs_url"
                type: "string"
                description: ""
              
              - name: "git_tags_url"
                type: "string"
                description: ""
              
              - name: "git_url"
                type: "string"
                description: ""
              
              - name: "issue_comment_url"
                type: "string"
                description: ""
              
              - name: "issue_events_url"
                type: "string"
                description: ""
              
              - name: "issues_url"
                type: "string"
                description: ""
              
              - name: "keys_url"
                type: "string"
                description: ""
              
              - name: "labels_url"
                type: "string"
                description: ""
              
              - name: "languages_url"
                type: "string"
                description: ""
              
              - name: "merges_url"
                type: "string"
                description: ""
              
              - name: "milestones_url"
                type: "string"
                description: ""
              
              - name: "notifications_url"
                type: "string"
                description: ""
              
              - name: "pulls_url"
                type: "string"
                description: ""
              
              - name: "releases_url"
                type: "string"
                description: ""
              
              - name: "ssh_url"
                type: "string"
                description: ""
              
              - name: "stargazers_url"
                type: "string"
                description: ""
              
              - name: "statuses_url"
                type: "string"
                description: ""
              
              - name: "subscribers_url"
                type: "string"
                description: ""
              
              - name: "subscription_url"
                type: "string"
                description: ""
              
              - name: "tags_url"
                type: "string"
                description: ""
              
              - name: "teams_url"
                type: "string"
                description: ""
              
              - name: "trees_url"
                type: "string"
                description: ""
              
              - name: "clone_url"
                type: "string"
                description: ""
              
              - name: "mirror_url"
                type: "string"
                description: ""
              
              - name: "hooks_url"
                type: "string"
                description: ""
              
              - name: "svn_url"
                type: "string"
                description: ""
              
              - name: "homepage"
                type: "string"
                description: ""
              
              - name: "language"
                type: "string"
                description: ""
              
              - name: "forks_count"
                type: "integer"
                description: ""
              
              - name: "stargazers_count"
                type: "integer"
                description: ""
              
              - name: "watchers_count"
                type: "integer"
                description: ""
              
              - name: "size"
                type: "integer"
                description: ""
              
              - name: "default_branch"
                type: "string"
                description: ""
              
              - name: "open_issues_count"
                type: "integer"
                description: ""
              
              - name: "is_template"
                type: "boolean"
                description: ""
              
              - name: "topics"
                type: "array"
                description: ""
                subattributes:
                - name: "items"
                  type: "string"
                  description: ""
                
              - name: "has_issues"
                type: "boolean"
                description: ""
              
              - name: "has_projects"
                type: "boolean"
                description: ""
              
              - name: "has_wiki"
                type: "boolean"
                description: ""
              
              - name: "has_pages"
                type: "boolean"
                description: ""
              
              - name: "has_downloads"
                type: "boolean"
                description: ""
              
              - name: "archived"
                type: "boolean"
                description: ""
              
              - name: "disabled"
                type: "boolean"
                description: ""
              
              - name: "visibility"
                type: "string"
                description: ""
              
              - name: "pushed_at"
                type: "string"
                description: ""
              
              - name: "created_at"
                type: "date-time"
                description: ""
              
              - name: "updated_at"
                type: "date-time"
                description: ""
              
              - name: "permissions"
                type: "object"
                description: ""
                subattributes: *pull-permissions
              
              - name: "allow_rebase_merge"
                type: "boolean"
                description: ""
              
              - name: "temp_clone_token"
                type: "string"
                description: ""
              
              - name: "allow_squash_merge"
                type: "boolean"
                description: ""
              
              - name: "allow_auto_merge"
                type: "boolean"
                description: ""
              
              - name: "delete_branch_on_merge"
                type: "boolean"
                description: ""
              
              - name: "allow_update_branch"
                type: "boolean"
                description: ""
              
              - name: "use_squash_pr_title_as_default"
                type: "boolean"
                description: ""
              
              - name: "allow_merge_commit"
                type: "boolean"
                description: ""
              
              - name: "subscribers_count"
                type: "integer"
                description: ""
              
              - name: "network_count"
                type: "integer"
                description: ""
              
            
          
          - name: "temp_clone_token"
            type: "string"
            description: ""
          
          - name: "allow_squash_merge"
            type: "boolean"
            description: ""
          
          - name: "allow_auto_merge"
            type: "boolean"
            description: ""
          
          - name: "delete_branch_on_merge"
            type: "boolean"
            description: ""
          
          - name: "allow_update_branch"
            type: "boolean"
            description: ""
          
          - name: "use_squash_pr_title_as_default"
            type: "boolean"
            description: ""
          
          - name: "allow_merge_commit"
            type: "boolean"
            description: ""
          
          - name: "allow_forking"
            type: "boolean"
            description: ""
          
          - name: "subscribers_count"
            type: "integer"
            description: ""
          
          - name: "network_count"
            type: "integer"
            description: ""
          
          - name: "open_issues"
            type: "integer"
            description: ""
          
          - name: "watchers"
            type: "integer"
            description: ""
          
          - name: "master_branch"
            type: "string"
            description: ""
          
          - name: "starred_at"
            type: "string"
            description: ""

      - name: "repository_url"
        type: "string"
        description: ""

      - name: "state"
        type: "string"
        description: ""

      - name: "title"
        type: "string"
        description: ""

      - name: "updated_at"
        type: "date-time"
        description: ""

      - name: "url"
        type: "string"
        description: ""

      - name: "user"
        type: "object"
        description: ""
        subattributes: *user-attributes

  - name: "label"
    type: "object"
    description: ""
    subattributes:
      - name: "color"
        type: "string"
        description: ""

      - name: "name"
        type: "string"
        description: ""

  - name: "node_id"
    type: "string"
    description: ""

  - name: "performed_via_github_app"
    type: "object, string"
    description: ""
    subattributes: *performed-via-github-app

  - name: "rename"
    type: "object"
    description: ""
    subattributes:
      - name: "from"
        type: "string"
        description: ""

      - name: "to"
        type: "string"
        description: ""

  - name: "requested_reviewer"
    type: "object"
    description: ""
    subattributes: *user-attributes

  - name: "review_requester"
    type: "object"
    description: ""
    subattributes: *user-attributes

  - name: "requested_team"
    type: "object"
    description: ""
    subattributes:
      - name: "id"
        type: "integer"
        description: ""
          
      - name: "node_id"
        type: "string"
        description: ""
          
      - name: "name"
        type: "string"
        description: ""
          
      - name: "slug"
        type: "string"
        description: ""
          
      - name: "description"
        type: "string"
        description: ""
          
      - name: "privacy"
        type: "string"
        description: ""
          
      - name: "permission"
        type: "string"
        description: ""
          
      - name: "permissions"
        type: "object"
        description: ""
        subattributes: *pull-permissions
          
      - name: "url"
        type: "string"
        description: ""
          
      - name: "html_url"
        type: "string"
        description: ""
          
      - name: "members_url"
        type: "string"
        description: ""
          
      - name: "repositories_url"
        type: "string"
        description: ""
          
      - name: "parent"
        type: "object"
        description: ""
        subattributes:
          - name: "id"
            type: "integer"
            description: ""
              
          - name: "node_id"
            type: "string"
            description: ""
              
          - name: "url"
            type: "string"
            description: ""
              
          - name: "members_url"
            type: "string"
            description: ""
              
          - name: "name"
            type: "string"
            description: ""
              
          - name: "description"
            type: "string"
            description: ""
              
          - name: "permission"
            type: "string"
            description: ""
              
          - name: "privacy"
            type: "string"
            description: ""
              
          - name: "html_url"
            type: "string"
            description: ""
              
          - name: "repositories_url"
            type: "string"
            description: ""
              
          - name: "slug"
            type: "string"
            description: ""
              
          - name: "ldap_dn"
            type: "string"
            description: ""

  - name: "dismissed_review"
    type: "object"
    description: ""
    subattributes:
      - name: "state"
        type: "string"
        description: ""
          
      - name: "review_id"
        type: "integer"
        description: ""
          
      - name: "dismissal_message"
        type: "string"
        description: ""
          
      - name: "dismissal_commit_id"
        type: "string"
        description: ""

  - name: "milestone"
    type: "object"
    description: ""
    subattributes:
      - name: "title"
        description: ""
        type: "string"

  - name: "project_card"
    type: "object"
    description: ""
    subattributes:
      - name: "url"
        type: "string"
        description: ""
          
      - name: "id"
        type: "integer"
        description: ""
          
      - name: "project_url"
        type: "string"
        description: ""
          
      - name: "project_id"
        type: "integer"
        description: ""
          
      - name: "column_name"
        type: "string"
        description: ""
          
      - name: "previous_column_name"
        type: "string"
        description: ""

  - name: "url"
    type: "string"
    description: ""

  - name: "draft"
    type: "boolean"
    description: ""
      
  - name: "author_association"
    type: "string"
    description: ""
      
  - name: "lock_reason"
    type: "string"
    description: ""
---