---
tap: "eloqua"
version: "1.0"

name: "contacts"
key: "contacts"

doc-link: &doc-link "https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAC/op-api-bulk-2.0-contacts-exports-post.html"
description: |
  The `{{ table.name }}` table contains info the contacts in your {{ integration.display_name }} account.

  **Note**: This table is replicated using the {{ integration.display_name }} Bulk API.

  #### Custom {{ table.name }} fields

  If applicable, Stitch will replicate custom fields related to `{{ table.name }}` in {{ integration.display_name }}.

replication-method: "Key-based Incremental"

api-method:
    name: "Bulk: Create a contact export definition"
    doc-link: *doc-link

attributes:
  - name: "Id"
    type: "string"
    primary-key: true
    description: "The contact ID."
    foreign-key-id: "contact-id"

  - name: "UpdatedAt"
    type: "date-time"
    replication-key: true
    description: "The Unix timestamp for the date and time the contact was last updated."

  - name: "ContactIDExt"
    type: "string"
    description: ""

  - name: "CreatedAt"
    type: "date-time"
    description: "The date and time the contact was created, expressed in Unix time."

  - name: "Custom Fields"
    type: "varies"
    description: |
      Custom fields associated with accounts in your {{ integration.display_name }} account.
---