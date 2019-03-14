---
tap: "freshdesk"
# version:

name: "companies"
doc-link: https://developers.freshdesk.com/api/#companies
singer-schema: 
description: |
  The `companies` table contains info about the companies your various customers and contacts belong to.

  #### Custom Fields

  If applicable, Stitch will replicate custom fields related to `companies` in {{ integration.display_name }}.
 
replication-method: "Key-based Incremental"
api-method:
  name: "listAllCompanies"
  doc-link: https://developers.freshdesk.com/api/#list_all_companies

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The company ID."

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The last time the company was updated."

  - name: "description"
    type: "string"
    description: "The description of the company."

  - name: "domains"
    type: "array"
    description: "The domains (ex: `stitchdata.com`) associated with the company."
    subattributes:
      - name: "value"
        type: "string"
        description: "The domain (ex: `stitchdata.com`) associated with the company."

  - name: "name"
    type: "string"
    description: "The name of the company."

  - name: "note"
    type: "string"
    description: "Any notes about the company."

  - name: "created_at"
    type: "date-time"
    description: "The timestamp when the company was first created."
---