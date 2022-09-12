---
tap: "intercom"
version: "2"
key: "company"

name: "companies"
doc-link: "https://developers.intercom.com/intercom-api-reference/reference/company-model"
singer-schema: "https://github.com/singer-io/tap-intercom/blob/master/tap_intercom/schemas/companies.json"
description: |
  The `{{ table.name }}` table contains info about companies that use your {{ integration.display_name }} product.

  #### Custom attributes {#company-custom-attributes}

  If applicable, Stitch will replicate custom fields related to `{{ table.name }}` in {{ integration.display_name }}.

  #### Limitations {#company-limitations}

  [{{ integration.display_name }}'s API limits the number of simultaneous requests]({{ table.api-method.doc-link }}){:target="new"} a single {{ integration.display_name }} app, or connection, can make to the {{ table.api-method.name }} endpoint. Stitch uses this endpoint to replicate company data. Currently, only one request can occur at a time.

  If multiple connections exist and they attempt to use this endpoint at the same time, only the connection who made the request first will succeed.

  This means that if Stitch attempts to extract data when another connection is using the endpoint, Extraction will fail and an [error](TODO) will surface in the Extraction Logs.

  To prevent or minimize this issue, we recommend limiting the number of connections a single workspace has or scheduling extraction jobs in Stitch around your other connections' usage.

replication-method: "Key-based Incremental"

api-method:
  name: "Scroll over all companies"
  doc-link: "https://developers.intercom.com/intercom-api-reference/reference/iterating-over-all-companies"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The {{ integration.display_name }}-generated company ID."
    foreign-key-id: "company-id"

  - name: "updated_at"
    type: "date-time"
    description: "The time the company was last updated."
    replication-key: true  

  - name: "company_id"
    type: "string"
    description: "The ID for the company, as defined by you."

  - name: "created_at"
    type: "date-time"
    description: "The time the company was added to {{ integration.display_name }}."

  - name: "custom_attributes"
    type: "object"
    description: "If applicable, the custom attributes you've applied to the company."

  - name: "industry"
    type: "string"
    description: "The industry the company operates in."

  - name: "last_request_at"
    type: "date-time"
    description: "The time the company last recorded making a request."

  - name: "monthly_spend"
    type: "integer"
    description: "The amount of revenue the company generates for your business."

  - name: "name"
    type: "string"
    description: "The name of the company."

  - name: "plan"
    type: "object"
    description: "The name of the plan associated with the company."
    subattributes:
      - name: "id"
        type: "string"
        description: "The plan ID."

      - name: "name"
        type: "string"
        description: "The name of the plan."

      - name: "type"
        type: "string"
        description: "This will be `plan`."

  - name: "remote_created_at"
    type: "date-time"
    description: "The time the company was created, as a Unix timestamp."

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
    description: "The number of recorded sessions for the company."

  - name: "size"
    type: "integer"
    description: "The number of employees in the company."

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
    description: "This will be `company`."

  - name: "user_count"
    type: "integer"
    description: "The number of users in the company."

  - name: "website"
    type: "string"
    description: "The URL for the company's website."
---