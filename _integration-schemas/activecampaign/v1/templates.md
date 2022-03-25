---
tap: "activecampaign"
version: "0.3"
key: ""

name: "templates"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-activecampaign/blob/master/tap_activecampaign/schemas/templates.json"
description: |
  The `{{ table.name }}` table contains information about templates used for campaign emails in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: "Templates"
    doc-link: "https://developers.activecampaign.com/reference#templates"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The template ID."
    #foreign-key-id: "template-id"

  - name: "mdate"
    type: "date-time"
    description: "The time the template was last modified."
    replication-key: true

  - name: "categoryid"
    type: "integer"
    description: ""
  - name: "content"
    type: "string"
    description: ""
  - name: "ed_instanceid"
    type: "integer"
    description: ""
  - name: "ed_version"
    type: "integer"
    description: ""
  - name: "hidden"
    type: "integer"
    description: ""
  
  - name: "importnum"
    type: "integer"
    description: ""

  - name: "modified"
    type: "integer"
    description: ""
  - name: "name"
    type: "string"
    description: ""
  - name: "preview_content"
    type: "string"
    description: ""
  - name: "screenshot"
    type: "string"
    description: ""
  - name: "subject"
    type: "string"
    description: ""
  - name: "used"
    type: "integer"
    description: ""
  - name: "userid"
    type: "integer"
    description: "The user ID."
    foreign-key-id: "user-id"
  - name: "waitpreview"
    type: "integer"
    description: ""
---
