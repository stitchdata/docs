---
# tap: "zuora"
version: 1.0

name: ""
doc-link: https://live-www.zuora.com/developer/api-reference/#tag/Accounts
#singer-schema: 
description: |
  The `account` table contains information about .

replication-method: "Incremental"
api-method:
  name:
  doc-link:

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The account ID."

  - name: "updatedDate"
    type: "date-time"
    replication-key: true
    description: "The date when the account was last updated."

  - name: "createdById"
    type: "string"
    description: "The ID of the Zuora user who created the account."

  - name: "createdDate"
    type: "date-time"
    description: "The date when the account was created."

  - name: "deleted"
    type: "boolean"
    description: |
      **Only supported for the AQuA API.** If `true`, this record was deleted in Zuora.

  - name: "updatedById"
    type: "string"
    description: "The ID of the Zuora user who last updated the account."

  - name: ""
    type: 
    description: ""

---