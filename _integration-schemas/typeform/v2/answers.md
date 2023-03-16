---
tap: "typeform"
version: "2"
name: "answers"

doc-link: "https://developer.typeform.com/responses/"
singer-schema: "https://github.com/singer-io/tap-typeform/blob/master/tap_typeform/schemas/answers.json"

description: |
  The `{{ table.name }}` table contains info about the answers submitted for the forms specified in the {{ app.page-names.int-settings }} page. 
  **Note**: There is no replication key for this table, it uses the replication key `submitted_at` from its parent stream [`submitted_landings`](#submitted-landings).
replication-method: "Key-based Incremental"

api-method:
  name: "Retrieve responses"
  doc-link: "https://developer.typeform.com/responses/reference/retrieve-responses"

attributes:
  - name: "landing_id"
    type: "string"
    primary-key: true
    description: "The ID for the form landing."
    foreign-key-id: "landing-id"

  - name: "submitted_at"
    type: "date-time"
    description: |
      The time that the form response was submitted in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601){:target="new"} format, UTC time.

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