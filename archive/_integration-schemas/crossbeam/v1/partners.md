---
tap: "crossbeam"
version: "1"
key: ""

name: "partners"
doc-link: "https://developers.crossbeam.com/#dd64387a-b410-40f3-9993-e87f1df96963"
singer-schema: "https://github.com/singer-io/tap-crossbeam/blob/master/tap_crossbeam/schemas/partners.json"
description: |
  The `{{ table.name }}` table contains information about your partners as well as partner invitations sent to you in your {{ integration.display_name }} account.

replication-method: "Full Table"

api-method:
    name: "get Partners"
    doc-link: "https://developers.crossbeam.com/#dd64387a-b410-40f3-9993-e87f1df96963"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The partner ID."

  - name: "clearbit_domain"
    type: "string"
    description: ""
  - name: "domain"
    type: "string"
    description: ""
  
  - name: "logo_url"
    type: "string"
    description: ""
  - name: "name"
    type: "string"
    description: ""
  - name: "url"
    type: "string"
    description: ""
  - name: "users"
    type: "array"
    description: ""
    subattributes:
      - name: "first_name"
        type: "string"
        description: ""
      - name: "gravatar_url"
        type: "string"
        description: ""
      - name: "id"
        type: "integer"
        description: ""
      - name: "last_name"
        type: "string"
        description: ""
  - name: "uuid"
    type: "string"
    description: ""
---
