---
tap: "surveymonkey"
version: "1"
key: ""

name: "responses"
doc-link: "https://developer.surveymonkey.com/api/v3/"
singer-schema: "https://github.com/singer-io/tap-surveymonkey/blob/master/tap_surveymonkey/schemas/responses.json"
description: "This table contains information about your survey responses."

replication-method: "Key-based Incremental"

api-method:
    name: "GET Survey Responses"
    doc-link: "https://developer.surveymonkey.com/api/v3/#collectors-id-responses-id-details"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The response ID."
    foreign-key-id: "response-id"

  - name: "date_modified"
    type: "date-time"
    description: "The date the response was last modified."
    replication-key: true

  - name: "analyze_url"
    type: "string"
    description: "The weblink to the analyze page to view the response."
  
  - name: "collection_mode"
    type: "string"
    description: |
      The collection mode of the response: `default`, `preview`, `data_entry`, `survey_preview`, or `edit`.
  
  - name: "collector_id"
    type: "string"
    description: "The ID of the collector the response was taken for."
  
  - name: "custom_value"
    type: "string"
    description: "The custom value associated with a response."
  
  - name: "custom_variables"
    type: "object"
    description: "The values to any available custom variables in the survey."
    subattributes:
  
  - name: "date_created"
    type: "date-time"
    description: "The date the response was created."
  
  - name: "edit_url"
    type: "string"
    description: "The weblink to the survey taking page to edit the response."

  - name: "email_address"
    type: "string"
    description: "The email address of the responder."  

  - name: "first_name"
    type: "string"
    description: "The first name of the responder."  
  
  - name: "href"
    type: "string"
    description: "The **Resource API** URL."
  
  - name: "ip_address"
    type: "string"
    description: "The IP Address the response was taken from."

  - name: "last_name"
    type: "string"
    description: "The last name of the responder."  
  
  - name: "logic_path"
    type: "object"
    description: "The logic path taken during the survey."
    subattributes:
  
  - name: "metadata"
    type: "object"
    description: "Other associated metadata or custom values."
    subattributes:
  
  - name: "page_path"
    type: "array"
    description: "The order in which the pages were responded to."
    subattributes:
      - name: "value"
        type: "string"
        description: ""
  
  - name: "pages"
    type: "array"
    description: "Pages from the survey and their associated responses."
    subattributes:
      - name: "id"
        type: "string"
        description: "The ID of the page with responses."
      - name: "questions"
        type: "array"
        description: "The questions on that page with responses."
        subattributes:
          - name: "answers"
            type: "array"
            description: "The answers for the question with responses."
            subattributes:
              - name: "choice_id"
                type: "string"
                description: "The choice selected."
              - name: "col_id"
                type: "string"
                description: "The column selected."
              - name: "image"
                type: "string"
                description: ""
              - name: "other_id"
                type: "string"
                description: "The other text choice selected."
              - name: "row_id"
                type: "string"
                description: "The row selected."
              - name: "text"
                type: "string"
                description: "Any open ended text."
          - name: "id"
            type: "string"
            description: "ID of the question with responses."
          - name: "variable_id"
            type: "string"
            description: "ID of the random assignment variable for the question."
  
  - name: "recipient_id"
    type: "string"
    description: "The ID of the recipient."
  
  - name: "response_status"
    type: "string"
    description: |
      The status of the response: `completed`, `partial`, `overquota`, or `disqualified`.
  
  - name: "survey_id"
    type: "string"
    description: "ID of the survey the response was taken for."
    foreign-key-id: "survey-id"
  
  - name: "total_time"
    type: "integer"
    description: "Total time in seconds spent on the survey."
---
