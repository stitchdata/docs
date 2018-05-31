---
tap: "github"
# version: ""

name: "commits"
doc-link:
singer-schema: https://github.com/singer-io/tap-github/blob/master/tap_github/commits.json
description: |
  The `commits` table contains info about repository commits in a project.

replication-method: "Key-based Incremental"
replication-key:
  name: "since"
  tooltip: "This is query parameter used to extract new/updated data from GitHub. It will not be included in the table's fields."

api-method:
  name: "listRepositoryCommits"
  doc-link: https://developer.github.com/v3/repos/commits/#list-commits-on-a-repository

attributes:
  - name: "sha"
    type: "string"
    primary-key: true
    description: "The git commit hash."

  - name: "comments_url"
    type: "string"
    description: "The URL to the commit's comments page."

  - name: "commit"
    type: "object"
    description: "Details about the commit."
    object-attributes:
      - name: "url"
        type: "string"
        description: "The URL to the commit."

      - name: "tree"
        type: "object"
        description: "Details about the commit tree."
        object-attributes:
          - name: "sha"
            type: "string"
            description: "The git commit tree hash."

          - name: "url"
            type: "string"
            description: "The URL to the commit tree."

      - name: "author"
        type: "object"
        description: "Details about the author of the commit."
        object-attributes:
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
        object-attributes:
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
    array-attributes:
      - name: "sha"
        type: "string"
        description: "The git hash of the parent commit."
        foreign-key: true

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
