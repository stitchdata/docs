---
tap: "zuora"
version: "1"

name: "import"
doc-link: https://live-www.zuora.com/developer/api-reference/#tag/imports
#singer-schema: 
description: |
  The `{{ table.name }}` table contains information about content uploads.

replication-method: "Key-based Incremental"
api-method:
  name:
  doc-link:

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The import ID."

  - name: "updatedDate"
    type: "date-time"
    replication-key: true
    description: "The date when the import was last updated."

  - name: "createdById"
    type: "string"
    description: "The ID of the {{ integration.display_name }} user who created the import."

  - name: "createdDate"
    type: "date-time"
    description: "The date when the import was created."

  - name: "deleted"
    type: "boolean"
    description: |
      **Only supported for the AQuA API.** If `true`, this record was deleted in {{ integration.display_name }}.

  - name: "importType"
    type: "string"
    description: |
      The type of item imported.

  - name: "importedCount"
    type: "integer"
    description: "The number of successfully imported records."

  - name: "md5"
    type: "string"
    description: "A check to validate the import file's integrity."

  - name: "name"
    type: "string"
    description: "The name of the import."

  - name: "originalResourceUrl"
    type: "string"
    description: "The URL of the import file."

  - name: "resultResourceUrl"
    type: "string"
    description: "The URL for the import result file, which is a zipped CSV file."

  - name: "status"
    type: "string"
    description: |
      The status of the import. Possible values are:

      - `Pending`
      - `Processing`
      - `Completed`
      - `Canceled`
      - `Failed`

  - name: "statusReason"
    type: "string"
    description: "The reason for the given status. Useful for troubleshooting import failures."

  - name: "totalCount"
    type: "integer"
    description: "The number of records in the import file."

  - name: "updatedById"
    type: "string"
    description: "The ID of the {{ integration.display_name }} user who last updated the import."
---