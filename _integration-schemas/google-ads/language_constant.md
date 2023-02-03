---
tap: "google-ads"
version: "1"
name: "language_constant"
doc-link: https://developers.google.com/google-ads/api/reference/rpc/v10/LanguageConstant
dependent-on: "campaign-criterion"
description: |
  The `{{ table.name }}` table contains info about about languages.

  [This is a **Core Object** table](#replication). 
  
  This table is dependent on the [`{{ table.dependent-on }}`](#{{ table.dependent-on }}) stream.

replication-method: "Full Table"
attribution-window: true

attributes:
  - name: "resouce_name"
    type: "string"
    description: ""
    
  - name: "id"
    type: "integer"
    description: ""
    primary-key: true
    
  - name: "code"
    type: "string"
    description: ""
    
  - name: "name"
    type: "string"
    description: ""
    
  - name: "targetable"
    type: "boolean"
    description: ""

---