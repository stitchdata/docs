---
tap: "looker"
version: "1"
key: "version"

name: "versions"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-looker/blob/master/tap_looker/schemas/versions.json"
description: |
  The `{{ table.name }}` table contains info about the API versions supported by your {{ integration.display_name }} instance.

replication-method: "Full Table"

api-method:
  name: "Get API versions"
  doc-link: "https://docs.looker.com/reference/api-and-integration/api-reference/v3.1/config#get_apiversion"

attributes:
  - name: "looker_release_version"
    type: "string"
    primary-key: true
    description: "The {{ integration.display_name }} release version."
    foreign-key-id: "looker-version-id"

  - name: "current_version"
    type: "object"
    description: ""
    subattributes:
      - name: "full_version"
        type: "string"
        description: ""
        foreign-key-id: "looker-version-id"

      - name: "status"
        type: "string"
        description: ""

      - name: "swagger_url"
        type: "string"
        description: ""

      - name: "version"
        type: "string"
        description: ""

  - name: "supported_versions"
    type: "array"
    description: ""
    subattributes:
      - name: "full_version"
        type: "string"
        description: ""
        foreign-key-id: "looker-version-id"

      - name: "status"
        type: "string"
        description: ""

      - name: "swagger_url"
        type: "string"
        description: ""

      - name: "version"
        type: "string"
        description: ""
---