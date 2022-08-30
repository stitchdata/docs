---
# -------------------------- #
#        Table Details       #
# -------------------------- #

tap: "github"
version: "2"
key: "commit"

name: "commits"
doc-link:
singer-schema: https://github.com/singer-io/tap-github/blob/master/tap_github/schemas/commits.json
description: |
  The `{{ table.name }}` table contains info about repository commits in a project.


# -------------------------- #
#    Replication Details     #
# -------------------------- #

api-method:
  name: "List commits"
  doc-link: "https://docs.github.com/en/rest/reference/repos#list-commits"

replication-method: "Key-based Incremental"
replication-key:
  name: "since"
  tooltip: "This is a query parameter used to extract new/updated data from GitHub. It will not be included in the table's fields."


# -------------------------- #
#       Table Attributes     #
# -------------------------- #

attributes:
  - name: "sha"
    type: "string"
    primary-key: true
    description: "The git commit hash."
    # foreign-key-id: "sha"

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

      - name: "message"
        type: "string"
        description: ""

      - name: "tree"
        type: "object"
        description: ""
        subattributes:
          - name: "sha"
            type: "string"
            description: ""

          - name: "url"
            type: "string"
            description: ""

      - name: "url"
        type: "string"
        description: ""

  - name: "files"
    type: "array"
    description: ""
    subattributes:
      - name: "additions"
        type: "number"
        description: ""

      - name: "blob_url"
        type: "string"
        description: ""
        
      - name: "changes"
        type: "number"
        description: ""

      - name: "deletions"
        type: "number"
        description: ""

      - name: "filename"
        type: "string"
        description: ""

      - name: "patch"
        type: "string"
        description: ""

      - name: "raw_url"
        type: "string"
        description: ""

      - name: "status"
        type: "string"
        description: ""

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

  - name: "_sdc_repository"
    type: "string"
    description: ""

  - name: "url"
    type: "string"
    description: "The URL to the commit."
---