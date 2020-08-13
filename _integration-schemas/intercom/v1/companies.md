---
tap: "intercom"
version: "1"

name: "companies"
doc-link: "https://developers.intercom.com/intercom-api-reference/v2.0/reference#company-model"
singer-schema: "https://github.com/singer-io/tap-intercom/blob/master/tap_intercom/schemas/companies.json"
description: |
  The `{{ table.name }}` table contains info about companies that use your {{ integration.display_name }} product.

  #### Custom Attributes

  If applicable, Stitch will replicate custom fields related to `{{ table.name }}` in {{ integration.display_name }}.

replication-method: "Key-based Incremental"

api-method:
    name: "scrollOverAllCompanies"
    doc-link: "https://developers.intercom.com/intercom-api-reference/v2.0/reference#iterating-over-all-companies"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The company ID."
    foreign-key-id: "company-id"

  - name: "updated_at"
    type: "date-time"
    description: "The time the company was last updated."
    replication-key: true  

  - name: "company_id"
    type: "string"
    description: ""
  - name: "created_at"
    type: "date-time"
    description: ""
  - name: "custom_attributes"
    type: "object"
    description: ""
  - name: "industry"
    type: "string"
    description: ""
  - name: "monthly_spend"
    type: "number"
    description: ""
  - name: "name"
    type: "string"
    description: ""
  - name: "plan"
    type: "object"
    description: ""
    subattributes:
      - name: "id"
        type: "string"
        description: ""
      - name: "name"
        type: "string"
        description: ""
      - name: "type"
        type: "string"
        description: ""
  - name: "remote_created_at"
    type: "date-time"
    description: ""
  - name: "segments"
    type: "array"
    description: "A list of segments within a company."
    subattributes:
      - name: "id"
        type: "string"
        description: "The segment ID."
        foreign-key-id: "segment-id"

  - name: "session_count"
    type: "integer"
    description: ""
  - name: "size"
    type: "integer"
    description: ""
  - name: "tags"
    type: "array"
    description: "A list of tags within a company."
    subattributes:
      - name: "id"
        type: "string"
        description: "The tag ID."
        foreign-key-id: "tag-id"
  - name: "type"
    type: "string"
    description: ""
  
  - name: "user_count"
    type: "integer"
    description: ""
  - name: "website"
    type: "string"
    description: ""
---
