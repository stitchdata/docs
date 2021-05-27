---
tap: "github"
version: "1"
key: "pull-request-commit"

name: "pr_commits"
doc-link: ""
singer-schema: ""
description: |
  The `{{ table.name }}` table contains info about pull request commits and is a slight variation of the [`commits`](#commits) table. This allows you to associate commits to pull requests that are squash merged.

replication-method: "Key-based Incremental"
replication-key:
  name: "since"
  based-on: "updated_at"
  tooltip: "This is a query parameter used to extract new/updated data from GitHub. It will not be included in the table's fields."

dependent-on: "pull_requests"

api-method:
  name: "List pull requests"
  doc-link: "https://docs.github.com/en/rest/reference/pulls#list-commits-on-a-pull-request"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The commit ID."

  - name: "pr_number"
    type: "integer"
    description: ""

  - name: "pr_id"
    type: "string"
    description: "The ID of the pull request associated with the commit."
    foreign-key-id: "pull-request-id"

  - name: "sha"
    type: "string"
    description: "The git commit hash."
    foreign-key-id: "sha"

  - name: "comments_url"
    type: "string"
    description: "The URL to the commit's comments page."

  - name: "commit"
    type: "object"
    description: "Details about the commit."
    subattributes:
      - name: "url"
        type: "string"
        description: "The URL to the commit."

      - name: "tree"
        type: "object"
        description: "Details about the commit tree."
        subattributes:
          - name: "sha"
            type: "string"
            description: "The git commit tree hash."

          - name: "url"
            type: "string"
            description: "The URL to the commit tree."

      - name: "author"
        type: "object"
        description: "Details about the author of the commit."
        subattributes:
          - name: "date"
            type: "string"
            description: "The date the author committed the change."

          - name: "email"
            type: "string"
            description: "The author's email address."

          - name: "name"
            type: "string"
            description: "The author's name."

      - name: "message"
        type: "string"
        description: "The commit message."

      - name: "committer"
        type: "object"
        description: "Details about the user who committed the change."
        subattributes:
          - name: "date"
            type: "string"
            description: "The date the committer committed the change."

          - name: "email"
            type: "string"
            description: "The committer's email address."

          - name: "name"
            type: "string"
            description: "The committer's name."

      - name: "comment_count"
        type: "integer"
        description: "The number of comments on the commit."

  - name: "html_url"
    type: "string"
    description: "The HTML URL to the commit."

  - name: "parents"
    type: "array"
    description: "Details about the parent commits."
    subattributes:
      - name: "sha"
        type: "string"
        description: "The git hash of the parent commit."
        # foreign-key-id: "sha"

      - name: "html_url"
        type: "string"
        description: "The HTML URL to the parent commit."

      - name: "url"
        type: "string"
        description: "The URL to the parent commit."

  - name: "url"
    type: "string"
    description: "The URL to the commit."
---