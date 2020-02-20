---
tap: "typeform"
version: "1"

name: "questions"
doc-link: "https://developer.typeform.com/create/reference/retrieve-form/"
singer-schema: "https://github.com/singer-io/tap-typeform/blob/master/tap_typeform/schemas/questions.json"
description: |
  The `{{ table.name }}` table contains a list of question titles and IDs that can be used to link to [`answers`](#answers).

replication-method: "Full Table"

api-method:
    name: "Retrieve form"
    doc-link: "https://developer.typeform.com/create/reference/retrieve-form/"

attributes:
  - name: "form_id"
    type: "string"
    primary-key: true
    description: "The form ID."
    # foreign-key-id: "form-id"
    
  - name: "question_id"
    type: "string"
    primary-key: true
    description: "The question ID."
    foreign-key-id: "question-id"
    
  - name: "ref"
    type: "string"
    description: "The readable name used to reference the question field."
    
  - name: "title"
    type: "string"
    description: "The unique name assigned to the field on the form."
---