---
tap: "github"
version: "1"
key: "release"

name: "releases"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-github/blob/master/tap_github/schemas/releases.json"
description: |
  The `{{ table.name }}` table contains info about releases in the repositories specified for the integration.

  **Note**: {{ integration.display_name }} doesn't include regular Git tags that haven't been associated with a release.

replication-method: "Full Table"

api-method:
  name: "List releases"
  doc-link: "https://docs.github.com/en/rest/reference/repos#list-releases"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The release ID."
    # foreign-key-id: "release-id"

  - name: "_sdc_repository"
    type: "string"
    description: ""

  - name: "author"
    type: "object"
    description: "Details about the author of the release."
    subattributes:
      - name: "id"
        type: "integer"
        description: "The user ID of the author."

      - name: "login"
        type: "string"
        description: "The username of the author."

  - name: "body"
    type: "string"
    description: "The text describing the tag."

  - name: "created_at"
    type: "date-time"
    description: "The date the release was created."

  - name: "draft"
    type: "boolean"
    description: "If `TRUE`, the release is a draft release."

  - name: "html_url"
    type: "string"
    description: "The HTML URL to the release." 

  - name: "name"
    type: "string"
    description: "The name of the release."

  - name: "prerelease"
    type: "boolean"
    description: "If `TRUE`, the release is a pre-release."

  - name: "published_at"
    type: "date-time"
    description: "The date the release was published."

  - name: "tag_name"
    type: "string"
    description: "The name of the tag."

  - name: "target_commitish"
    type: "string"
    description: "The commitish value that determines where the Git tag was created."

  - name: "url"
    type: "string"
    description: "The URL to the release."
---