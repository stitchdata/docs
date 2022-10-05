---
tap: "quickbooks"
version: "2"
key: "customer-types"

name: "customer_types"
doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/changedatacapture#the-changedatacapture-object"
singer-schema: "https://github.com/singer-io/tap-quickbooks/blob/master/tap_quickbooks/schemas/customer_types.json"
description: |
  The `{{ table.name }}` table contains info about types of customers.
 
replication-method: "Key-based Incremental"

replication-key:
  name: "MetaData.LastUpdatedTime"

api-method:
  name: "Query a customertype"
  doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/customertype#query-a-customertype"

attributes:
  - name: "Id"
    type: "string"
    description: ""
    primary-key: true

  - name: "Active"
    type: "boolean"
    description: ""

  - name: "domain"
    type: "string"
    description: ""
    
  - name: "MetaData"
    type: "object"
    description: ""
    subattributes:
      - name: "LastUpdatedTime"
        type: "date-time"
        description: ""

  - name: "Name"
    type: "string"
    description: ""

  - name: "sparse"
    type: "string"
    description: ""

  - name: "SyncToken"
    type: "string"
    description: ""
---