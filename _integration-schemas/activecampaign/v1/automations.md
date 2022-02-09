---
tap: "activecampaign"
version: "0.3"
key: ""

name: "automations"
doc-link: "https://developers.activecampaign.com/reference#automation"
singer-schema: "https://github.com/singer-io/tap-activecampaign/blob/master/tap_activecampaign/schemas/automations.json"
description: |
  The `{{ table.name }}` table contains information about automations in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
    name: "List all automations"
    doc-link: "https://developers.activecampaign.com/reference#list-all-automations"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The automation ID."
    foreign-key-id: "automation-id"

  - name: "mdate"
    type: "date-time"
    description: "The date the automation was last modified."
    replication-key: true

  - name: "cdate"
    type: "date-time"
    description: ""
  - name: "defaultscreenshot"
    type: "string"
    description: ""
  - name: "entered"
    type: "integer"
    description: ""
  - name: "exited"
    type: "integer"
    description: ""
  - name: "hidden"
    type: "integer"
    description: ""
  
  - name: "name"
    type: "string"
    description: ""
  - name: "screenshot"
    type: "string"
    description: ""
  - name: "status"
    type: "integer"
    description: ""
  - name: "userid"
    type: "integer"
    description: "The user ID."
    foreign-key-id: "user-id"  
---
