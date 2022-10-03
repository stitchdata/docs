---
# -------------------------- #
#        Table Details       #
# -------------------------- #

tap: "github"
version: "2"
key: "pull-request"

name: "pull_requests"
doc-link: https://developer.github.com/v3/pulls/
singer-schema: https://github.com/singer-io/tap-github/blob/master/tap_github/schemas/pull_requests.json
description: |
  The `{{ table.name }}` table contains info about pull requests made against the repositories specified for the integration.


# -------------------------- #
#    Replication Details     #
# -------------------------- #

api-method:
  name: "List pull requests"
  doc-link: "https://docs.github.com/en/rest/reference/pulls#list-pull-requests"

replication-method: "Key-based Incremental"
replication-key:
  name: "since"
  based-on: "updated_at"
  tooltip: "This is a query parameter used to extract new/updated data from GitHub. It will not be included in the table's fields."

# -------------------------- #
#       Table Attributes     #
# -------------------------- #

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The pull request ID."
    foreign-key-id: "pull-request-id"

  - name: "_sdc_repository"
    type: "string"
    description: ""

  - name: "base"
    type: "object"
    description: "Details about the base branch."
    subattributes:
      - name: "label"
        type: "string"
        description: ""
        
      - name: "ref"
        type: "string"
        description: ""
        
      - name: "repo"
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
            subattributes: &user-attributes
              - name: "name"
                type: "string"
                description: ""
                
              - name: "email"
                type: "string"
                description: ""

              - name: "login"
                type: "string"
                description: ""

              - name: "id"
                type: "string"
                description: ""

              - name: "node_id"
                type: "string"
                description: ""

              - name: "avatar_url"
                type: "string"
                description: ""

              - name: "gravatar_id"
                type: "string"
                description: ""

              - name: "url"
                type: "string"
                description: ""

              - name: "html_url"
                type: "string"
                description: ""

              - name: "followers_url"
                type: "string"
                description: ""

              - name: "following_url"
                type: "string"
                description: ""

              - name: "gists_url"
                type: "string"
                description: ""

              - name: "starred_url"
                type: "string"
                description: ""

              - name: "subscriptions_url"
                type: "string"
                description: ""

              - name: "organizations_url"
                type: "string"
                description: ""

              - name: "repos_url"
                type: "string"
                description: ""

              - name: "events_url"
                type: "string"
                description: ""

              - name: "received_events_url"
                type: "string"
                description: ""

              - name: "type"
                type: "string"
                description: ""

              - name: "site_admin"
                type: "string"
                description: ""
                
              - name: "starred_at"
                type: "string"
                description: ""
            
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
            type: "date-time"
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

      - name: "sha"
        type: "string"
        description: ""
        
      - name: "user"
        type: "object"
        description: ""
        subattributes: *user-attributes

  - name: "body"
    type: "string"
    description: "The description of the pull request."

  - name: "closed_at"
    type: "date-time"
    description: "The time the pull request was closed."

  - name: "created_at"
    type: "date-time"
    description: "The time the pull request was created."

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
        foreign-key-id: "issue-label-id"

      - name: "name"
        type: "string"
        description: ""

      - name: "node_id"
        type: "string"
        description: ""

      - name: "url"
        type: "string"
        description: ""

  - name: "merged_at"
    type: "string"
    description: "The time the pull request was merged."

  - name: "number"
    type: "integer"
    description: "The number of the pull request in the repository."

  - name: "state"
    type: "string"
    description: "The current status of the pull request. For example: `open`"

  - name: "title"
    type: "string"
    description: "The title of the pull request."

  - name: "updated_at"
    type: "date-time"
    description: "The last time the pull request was updated."

  - name: "url"
    type: "string"
    description: "The URL to the pull request."

  - name: "user"
    type: "object"
    description: "Details about the user who created the pull request."
    subattributes: *user-attributes
    
  - name: "node_id"
    type: "string"
    description: ""
    
  - name: "statuses_url"
    type: "string"
    description: ""
    
  - name: "draft"
    type: "boolean"
    description: ""
    
  - name: "requested_reviewers"
    type: "array"
    description: ""
    subattributes: *user-attributes
          
  - name: "merge_commit_sha"
    type: "string"
    description: ""
    
  - name: "review_comments_url"
    type: "string"
    description: ""
    
  - name: "active_lock_reason"
    type: "string"
    description: ""
    
  - name: "author_association"
    type: "string"
    description: ""
    
  - name: "diff_url"
    type: "string"
    description: ""
    
  - name: "assignee"
    type: "object"
    description: ""
    subattributes: *user-attributes
    
  - name: "comments_url"
    type: "string"
    description: ""
    
  - name: "head"
    type: "object"
    description: ""
    subattributes:
      - name: "label"
        type: "string"
        description: ""
        
      - name: "ref"
        type: "string"
        description: ""
        
      - name: "repo"
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
            subattributes:
              - name: "name"
                type: "string"
                description: ""
                
              - name: "email"
                type: "string"
                description: ""
                
              - name: "login"
                type: "string"
                description: ""
                
              - name: "id"
                type: "integer"
                description: ""
                
              - name: "node_id"
                type: "string"
                description: ""
                
              - name: "avatar_url"
                type: "string"
                description: ""
                
              - name: "gravatar_id"
                type: "string"
                description: ""
                
              - name: "url"
                type: "string"
                description: ""
                
              - name: "html_url"
                type: "string"
                description: ""
                
              - name: "followers_url"
                type: "string"
                description: ""
                
              - name: "following_url"
                type: "string"
                description: ""
                
              - name: "gists_url"
                type: "string"
                description: ""
                
              - name: "starred_url"
                type: "string"
                description: ""
                
              - name: "subscriptions_url"
                type: "string"
                description: ""
                
              - name: "organizations_url"
                type: "string"
                description: ""
                
              - name: "repos_url"
                type: "string"
                description: ""
                
              - name: "events_url"
                type: "string"
                description: ""
                
              - name: "received_events_url"
                type: "string"
                description: ""
                
              - name: "type"
                type: "string"
                description: ""
                
              - name: "site_admin"
                type: "boolean"
                description: ""
                
              - name: "starred_at"
                type: "string"
                description: ""
                
          - name: "forks"
            type: "integer"
            description: ""
            
          - name: "permissions"
            type: "object"
            description: ""
            subattributes: *pull-permissions
            
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
            type: "date-time"
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
            
      - name: "sha"
        type: "string"
        description: ""
        
      - name: "user"
        type: "object"
        description: ""
        subattributes: *user-attributes
        
  - name: "commits_url"
    type: "string"
    description: ""
    
  - name: "auto_merge"
    type: "object"
    description: ""
    subattributes:
      - name: "enabled_by"
        type: "object"
        description: ""
        subattributes: *user-attributes
        
      - name: "merge_method"
        type: "string"
        description: ""
        
      - name: "commit_title"
        type: "string"
        description: ""
        
      - name: "commit_message"
        type: "string"
        description: ""
        
  - name: "locked"
    type: "boolean"
    description: ""
    
  - name: "assignees"
    type: "array"
    description: ""
    subattributes:
      - name: "items"
        type: "object"
        description: ""
        subattributes: *user-attributes
      
  - name: "issues_url"
    type: "string"
    description: ""
    
  - name: "milestone"
    type: "object"
    description: ""
    subattributes:
      - name: "url"
        type: "string"
        description: ""
        
      - name: "html_url"
        type: "string"
        description: ""
        
      - name: "labels_url"
        type: "string"
        description: ""
        
      - name: "id"
        type: "integer"
        description: ""
        
      - name: "node_id"
        type: "string"
        description: ""
        
      - name: "number"
        type: "integer"
        description: ""
        
      - name: "state"
        type: "string"
        description: ""
        
      - name: "title"
        type: "string"
        description: ""
        
      - name: "description"
        type: "string"
        description: ""
        
      - name: "creator"
        type: "object"
        description: ""
        subattributes: *user-attributes
        
      - name: "open_issues"
        type: "integer"
        description: ""
        
      - name: "closed_issues"
        type: "integer"
        description: ""
        
      - name: "created_at"
        type: "date-time"
        description: ""
        
      - name: "updated_at"
        type: "date-time"
        description: ""

      - name: "closed_at"
        type: "date-time"
        description: ""
        
      - name: "due_on"
        type: "date-time"
        description: ""

  - name: "_links"
    type: "object"
    description: ""
    subattributes:
      - name: "comments"
        type: "object"
        description: ""
        subattributes:
          - name: "href"
            type: "string"
            description: ""

      - name: "commits"
        type: "object"
        description: ""
        subattributes:
          - name: "href"
            type: "string"
            description: ""

      - name: "statuses"
        type: "object"
        description: ""
        subattributes:
          - name: "href"
            type: "string"
            description: ""
            
      - name: "html"
        type: "object"
        description: ""
        subattributes:
          - name: "href"
            type: "string"
            description: ""

      - name: "issue"
        type: "object"
        description: ""
        subattributes:
          - name: "href"
            type: "string"
            description: ""

      - name: "review_comments"
        type: "object"
        description: ""
        subattributes:
          - name: "href"
            type: "string"
            description: ""

      - name: "review_comment"
        type: "object"
        description: ""
        subattributes:
          - name: "href"
            type: "string"
            description: ""

      - name: "self"
        type: "object"
        description: ""
        subattributes:
          - name: "href"
            type: "string"
            description: ""

  - name: "html_url"
    type: "string"
    description: ""
    
  - name: "requested_teams"
    type: "array"
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
    
  - name: "patch_url"
    type: "string"
    description: ""
---