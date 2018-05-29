---
tap: "github"
# version: ""

name: "commits"
doc-link:
singer-schema:
description: |
  The `commits` table contains info about repository commits in a project.

replication-method: "Incremental"
api-method:
  name: "listRepositoryCommits"
  doc-link:

attributes:
  - name: "sha"
    type: "string"
    description: "The git commit hash"

  - name: "url"
    type: "string"
    description: ""

  - name: "parents"
    type: "object"
    description: ""
    object-attributes:
    - name: "sha"
      type: "string"
      description: "The git hash of the parent commit"

    - name: "url"
      type: "string"
      description: "The URL to the parent commit"

    - name: "html_url"
      type: "string"
      description: "The HTML URL to the parent commit"

  - name: "html_url"
    type: "string"
    description: "The HTML URL to the commit"

  - name: "comments_url"
    type: "string"
    description: "The URL to the commit's comments page"

  - name: "commit"
    type: "object"
    description: ""
    object-attributes:
    - name: "url"
      type: "string"
      description: "The URL to the commit"

    - name: "tree"
      type: "object"
      description: ""
      object-attributes:
      - name: "sha"
        type: "string"
        description: ""

      - name: "url"
        type: "string"
        description: ""

    - name: "author"
      type: "object"
      description: ""
      object-attributes:
      - name: "date"
        type: "string"
        description: "The date the author committed the change"

      - name: "name"
        type: "string"
        description: "The author's name"

      - name: "email"
        type: "string"
        description: "The author's email"

    - name: "message"
      type: "string"
      description: "The commit message"

    - name: "committer"
      type: "object"
      description: ""
      object-attributes:
      - name: "date"
        type: "string"
        description: "The date the committer committed the change"

      - name: "name"
        type: "string"
        description: "The committer's name"

      - name: "email"
        type: "string"
        description: "The committer's email"

    - name: "comment_count"
      type: "integer"
      description: "The number of comments on the commit"
---
