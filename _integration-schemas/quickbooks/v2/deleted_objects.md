---
tap: "quickbooks"
version: "2"
key: "deleted-objects"

name: "deleted_objects"
doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/changedatacapture#the-changedatacapture-object"
singer-schema: "https://github.com/singer-io/tap-quickbooks/blob/master/tap_quickbooks/schemas/deleted_objects.json"
description: |
  The `{{ table.name }}` table contains info about objects deleted from {{ integration.display_name }}.
 
replication-method: "Key-based Incremental"

replication-key:
  name: "Metadata.LastUpdatedTime"

api-method:
  name: "Get a list of changed entities"
  doc-link: "https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/changedatacapture#get-a-list-of-changed-entities"

attributes:
  - name: "Id"
    type: "string"
    description: ""
    primary-key: true

  - name: "domain"
    type: "string"
    description: ""

  - name: "Metadata"
    type: "object"
    description: ""
    subattributes:
      - name: "LastUpdatedTime"
        type: "date-time"
        description: ""

  - name: "Type"
    type: "string"
    description: ""
---