---
tap: "intercom"
# version:

name: "companies"
doc-link: https://developers.intercom.com/reference#companies
description: |
  The `companies` table contains info about the companies (or commercial organizations) that use your Intercom product.

  #### Custom Attributes

  If applicable, Stitch will replicate custom fields related to `companies` in Intercom.

replication-method: "Key-based Incremental"
api-method:
  name: scrollOverAllCompanies
  doc-link: https://developers.intercom.com/reference#iterating-over-all-companies

attribution-window: true

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The Intercom-defined company ID."
    foreign-key-id: "company-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the company was last updated."

  - name: "company_id"
    type: "string"
    description: "The ID that you assigned to the company."

  - name: "created_at"
    type: "date-time"
    description: "The time the company was added to Intercom."

  - name: "remote_created_at"
    type: "date-time"
    description: "The time the company was created by you."

  - name: "name"
    type: "string"
    description: "The name of the company."

  - name: "custom_attributes"
    type: "object"
    description: "If applicable, the custom attributes you've applied to the company."

  - name: "session_count"
    type: "integer"
    description: "The number of recorded sessions for the company."

  - name: "monthly_spend"
    type: "number"
    description: "The amount of revenue the company generates for your business."

  - name: "user_count"
    type: "number"
    description: "The number of users in the company."

  - name: "plan"
    type: "string"
    description: "The name of the plan associated with the company."

  - name: "type"
    type: "string"
    description: "The value of this field will be `company`."
---