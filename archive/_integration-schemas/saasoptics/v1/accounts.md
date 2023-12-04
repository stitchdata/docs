---
tap: "saasoptics"
version: "1"
key: "account"

name: "accounts"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-saasoptics/blob/master/tap_saasoptics/schemas/accounts.json"
description: |
  The `{{ table.name }}` table contains info about accounts, or records in your Chart of Accounts, in {{ integration.display_name }}.

replication-method: "Full Table"

api-method:
  name: "Accounts List"
  doc-link: "https://saasoptics.zendesk.com/hc/en-us/articles/115013751507-Accounts-R-"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: ""
    foreign-key-id: "account-id"

  - name: "account_type"
    type: "string"
    description: ""

  - name: "intacct_id"
    type: "string"
    description: ""

  - name: "intacct_modified"
    type: "date-time"
    description: ""

  - name: "intacct_recordno"
    type: "integer"
    description: ""

  - name: "name"
    type: "string"
    description: ""

  - name: "netsuite_id"
    type: "string"
    description: ""

  - name: "source_system"
    type: "string"
    description: ""
---