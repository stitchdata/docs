---
tap: "iterable"
version: "1"
key: ""

name: "templates"
doc-link: https://api.iterable.com/api/docs#templates_getTemplates
singer-schema: https://github.com/singer-io/tap-iterable/tree/master/tap_iterable/schemas/templates.json
description: |
  The **{{ table.name }}** table contains information about project templates in you {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
  name: "Get project templates"
  doc-link: "https://api.iterable.com/api/docs#templates_getTemplates"

attributes:
  - name: "templateId"
    type: "integer"
    primary-key: true
    description: "The template ID."
    foreign-key-id: "template-id"

  - name: "updatedAt"
    type: "date-time"
    replication-key: true
    description: "The time the template was updated."

  - name: "campaignId"
    type: "integer"
    description: "The campaign ID."
    foreign-key-id: "campaign-id"

  - name: "clientTemplateId"
    type: "string"
    description: ""

  - name: "createdAt"
    type: "date-time"
    description: ""

  - name: "creatorUserId"
    type: "string"
    description: ""

  - name: "messageTypeId"
    type: "integer"
    description: "The message type ID."
    foreign-key-id: "message-id"

  - name: "name"
    type: "string"
    description: ""

---
