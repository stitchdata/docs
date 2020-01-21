---
tap: "eloqua"
version: "1"

name: "accounts"
key: "accounts"

doc-link: &doc-link "https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAC/op-api-bulk-2.0-accounts-exports-post.html"
description: |
  The `{{ table.name }}` table contains info about the accounts, or companies, in your {{ integration.display_name }} account.

  **Note**: This table is replicated using the {{ integration.display_name }} Bulk API.

  #### Custom {{ table.name }} fields

  If applicable, Stitch will replicate custom fields related to `{{ table.name }}` in {{ integration.display_name }}.

replication-method: "Key-based Incremental"

api-method:
    name: "Bulk: Create an account export definition"
    doc-link: *doc-link

attributes:
  - name: "Id"
    type: "string"
    primary-key: true
    description: "The account ID."
    # foreign-key-id: "account-id"

  - name: "UpdatedAt"
    type: "date-time"
    replication-key: true
    description: "The Unix timestamp for the date and time the account was last updated."

  - name: "CompanyIDExt"
    type: "string"
    description: ""

  - name: "CreatedAt"
    type: "date-time"
    description: "The date and time the account was created, expressed in Unix time."

  - name: "Custom Fields"
    type: "varies"
    description: |
      Custom fields associated with accounts in your {{ integration.display_name }} account.
---