---
tap: "typeform"
version: "1"
name: "answers"

doc-link: "https://developer.typeform.com/responses/"
singer-schema: "https://github.com/singer-io/tap-typeform/blob/master/tap_typeform/schemas/answers.json"

description: |
  The `{{ table.name }}` table contains info about the answers submitted for the forms specified in the {{ app.page-names.int-settings }} page.
replication-method: "Key-based Incremental"

api-method:
  name: "Retrieve responses"
  doc-link: "https://developer.typeform.com/responses/reference/retrieve-responses"

attributes:
  - name: "landing_id"
    type: "string"
    primary-key: true
    replication-key: true
    description: "The ID for the form landing."
    foreign-key-id: "landing-id"

  - name: "question_id"
    type: "string"
    primary-key: true
    description: "The question ID."
    foreign-key-id: "question-id"

  - name: "answer"
    type: "string"
    description: ""

  - name: "data_type"
    type: "string"
    description: |
      The field type of the question. Possible values are:
       - `choice`
      - `choices`
      - `date`
      - `email`
      - `url`
      - `file_url`
      - `number`
      - `boolean`
      - `text`
      - `payment`
   
  - name: "ref"
    type: "string"
    description: ""

  - name: "type"
    type: "string"
    description: ""
---