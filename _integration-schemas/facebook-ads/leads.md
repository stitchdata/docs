---
tap: "facebook-ads"
version: "1"

name: "leads"
doc-link: https://developers.facebook.com/docs/marketing-api/guides/lead-ads/
singer-schema: https://github.com/singer-io/tap-facebook/blob/master/tap_facebook/schemas/leads.json
description: |
  ## description of the table

replication-method: "Key-based Incremental"

api-method:
  name: "Retrieving Leads - Bulk Read"
  doc-link: "https://developers.facebook.com/docs/marketing-api/guides/lead-ads/retrieving#bulk-read"

attributes:
  - name: "id"
    type: "string"
    description: "The lead ID." 
    primary-key: true
    
  - name: "ad_id"
    type: "string"
    description: "The ad ID." 
    
  - name: "form_id"
    type: "string"
    description: "The form ID." 
    
  - name: "created_time"
    type: "date-time"
    description: "The time the lead was created." 
    replication-key: true

  - name: "field_data"
    type: "array"
    description: "" 
    subattributes:

      - name: "items"
        type: "object"
        description: ""
        subattributes:

          - name: "properties"
            type: "string"
            description: ""

          - name: "values"
            type: "array"
            description: ""
            subattributes:

              - name: "items"
                type: "string"
                description: ""

---