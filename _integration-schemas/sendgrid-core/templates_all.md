---
tap: "sendgrid-core"

name: "templates_all"
doc-link: 
singer-schema: https://github.com/singer-io/tap-sendgrid/blob/master/tap_sendgrid/schemas/templates_all.json
description: |
  The `templates_all` table contains info about the transactional templates in your SendGrid account. Transactional templates are templates specifically created for transactional email and are different than Marketing Campaign templates.

replication-method: "Full Table"

api-method:
  name: "List all templates"
  doc-link: "https://sendgrid.com/docs/API_Reference/Web_API_v3/Transactional_Templates/templates.html#-GET"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The template ID."

  - name: "name"
    type: "string"
    description: "The name of the template."

  - name: "versions"
    type: "array"
    description: "Details about each version of the template, if the template is versioned."
    array-attributes:
      - name: "template_id"
        type: "string"
        primary-key: true
        description: "The ID of the original template."

      - name: "active"
        type: "integer"
        description: "Indicates if the template version is the active version associated with the template."

      - name: "name"
        type: "string"
        description: "The name of the template version."

      - name: "html_content"
        type: "string"
        description: "The HTML content of the template version."

      - name: "plain_content"
        type: "string"
        description: "The plain text content of the template version."

      - name: "subject"
        type: "string"
        description: "The subject of the template version."

      - name: "editor"
        type: "string"
        description: "The editor used in the SendGrid UI. Possible values are `code` or `design`."
---