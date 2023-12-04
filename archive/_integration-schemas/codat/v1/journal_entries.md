---
tap: "codat"
version: "1"
key: "journal-entry"

name: "journal_entries"
doc-link: "https://docs.codat.io/reference/journals"
singer-schema: "https://github.com/singer-io/tap-codat/blob/master/tap_codat/schemas/journal_entries.json"
description: |
  The {{ table.name }} table contains information about journal entries for a given company in your {{ integration.display_name }} account.

replication-method: "Key-based Incremental"

api-method:
  name: "Get journal entries"
  doc-link: "https://docs.codat.io/reference/journals#journals_listpaged"

attributes:
  - name: "companyId"
    type: "string"
    primary-key: true
    description: "The company ID."
    foreign-key-id: "company-id"
  
  - name: "id"
    type: "string"
    primary-key: true
    description: "The journal entry ID."
    foreign-key-id: "journal-id"
      
  - name: "modifiedDate"
    type: "string"
    description: "The date the entry was last modified."
    replication-key: true
    
  - name: "createdOn"
    type: "string"
    description: ""

  - name: "journalLines"
    type: "array"
    description: ""
    subattributes:
      - name: "accountRef"
        type: "object"
        description: ""
        subattributes:
          - name: "id"
            type: "string"
            description: ""
            foreign-key-id: "account-id"

          - name: "name"
            type: "string"
            description: ""

      - name: "currency"
        type: "string"
        description: ""

      - name: "description"
        type: "string"
        description: ""

      - name: "grossAmount"
        type: "number"
        description: ""

      - name: "id"
        type: "string"
        description: ""

      - name: "netAmount"
        type: "number"
        description: ""

      - name: "taxAmount"
        type: "number"
        description: ""

  - name: "postedOn"
    type: "string"
    description: ""

  - name: "sourceModifiedDate"
    type: "string"
    description: ""
---