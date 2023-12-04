---
tap: "typeform"
version: "2"

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
    foreign-key-id: "form-id"
    
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
    
  - name: "attachment"
    type: "object"
    description: ""
    subattributes: &attachment
      - name: "type"
        type: "string"
        description: ""
        
      - name: "href"
        type: "string"
        description: ""
        
      - name: "scale"
        type: "number"
        description: ""
        
      - name: "properties"
        type: "object"
        description: ""
        subattributes:
          - name: "description"
            type: "string"
            description: ""
    
  - name: "field_type"
    type: "string"
    description: ""
    
  - name: "id"
    type: "string"
    description: ""
    
  - name: "layout"
    type: "object"
    description: ""
    subattributes:
      - name: "type"
        type: "string"
        description: ""
        
      - name: "placement"
        type: "string"
        description: ""
        
      - name: "attachment"
        type: "object"
        description: ""
        subattributes: *attachment
    
  - name: "name"
    type: "string"
    description: ""
    
  - name: "options"
    type: "array"
    description: ""
    subattributes:
      - name: "label"
        type: "string"
        description: ""
    
  - name: "properties"
    type: "object"
    description: ""
    subattributes:
      - name: "allow_multiple_selection"
        type: "boolean"
        description: ""
        
      - name: "allow_other_choice"
        type: "boolean"
        description: ""
        
      - name: "alphabetical_order"
        type: "boolean"
        description: ""
        
      - name: "button_text"
        type: "string"
        description: ""
        
      - name: "choices"
        type: "array"
        description: ""
        subattributes:
          - name: "attachment"
            type: "object"
            description: ""
            subattributes: 
              - name: "type"
                type: "string"
                description: ""
        
              - name: "href"
                type: "string"
                description: ""

          - name: "description"
            type: "string"
            description: ""
          
          - name: "label"
            type: "string"
            description: ""
          
          - name: "ref"
            type: "string"
            description: ""

      - name: "currency"
        type: "string"
        description: ""
        
      - name: "default_country_code"
        type: "string"
        description: ""
        
      - name: "description"
        type: "string"
        description: ""
        
      - name: "fields"
        type: "array"
        description: ""
        subattributes:
          - name: "items"
            type: "object"
            description: ""
        
      - name: "hide_marks"
        type: "boolean"
        description: ""
        
      - name: "labels"
        type: "object"
        description: ""
        subattributes:
          - name: "center"
            type: "string"
            description: ""
            
          - name: "left"
            type: "string"
            description: ""
            
          - name: "right"
            type: "string"
            description: ""
        
      - name: "price"
        type: "object"
        description: ""
        subattributes:
          - name: "type"
            type: "string"
            description: ""
            
          - name: "value"
            type: "string"
            description: ""
        
      - name: "randomize"
        type: "boolean"
        description: ""
        
      - name: "separator"
        type: "string"
        description: ""
        
      - name: "shape"
        type: "string"
        description: ""
    
  - name: "required"
    type: "boolean"
    description: ""
    
  - name: "type"
    type: "string"
    description: ""
    
  - name: "validations"
    type: "object"
    description: ""
    subattributes:
      - name: "max_length"
        type: "integer"
        description: ""
        
      - name: "max_selection"
        type: "integer"
        description: ""
        
      - name: "max_value"
        type: "integer"
        description: ""
        
      - name: "min_selection"
        type: "integer"
        description: ""
        
      - name: "min_value"
        type: "integer"
        description: ""
        
      - name: "required"
        type: "boolean"
        description: ""
---