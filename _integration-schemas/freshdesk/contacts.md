---
# As per Brian, this table isn't currently live in the tap
# because we encountered issues with server traffic during
# development. That's why this isn't live in the docs.
# We can uncomment this when/if it's addressed.

# tap: "freshdesk"
# version:

name: "contacts"
doc-link: https://developers.freshdesk.com/api/#contacts
singer-schema: https://github.com/singer-io/tap-freshdesk/blob/master/tap_freshdesk/schemas/contacts.json
description: |
  The `contacts` table contains info about the customers or potential customers that have filed support tickets in any of the channels in your Freshdesk account.

  #### Custom Fields

  If applicable, Stitch will replicate custom fields related to `contacts` in {{ integration.display_name }}.

replication-method: "Key-based Incremental"
api-method:
  name: "listAllContacts"
  doc-link: https://developers.freshdesk.com/api/#list_all_contacts

attributes:
  - name: "id"
    primary-key: true
    type: "integer"
    description: "The contact ID."

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The last time the contact was updated."

  - name: "other_companies"
    type: "array"
    description: "Other companies associated with the contact."
    array-attributes:
      - name: "value"
        type: "string"
        description: "An additional company associated with the user."

  - name: "view_all_tickets"
    type: "boolean"
    description: "Indicates if the contact can see all tickets associated with the company they belong to."

  - name: "other_emails"
    type: "array"
    description: "Other email addresses associated with the contact."
    array-attributes:
      - name: "value"
        type: "string"
        description: "An additional email associated with the contact."

  - name: "company_id"
    type: "number"
    description: "The company ID associated with the contact."

  - name: "email"
    type: "string"
    description: "The email address associated with the contact."

  - name: "job_title"
    type: "string"
    description: "The job title of the contact."

  - name: "description"
    type: "string"
    description: "The description of the contact."

  - name: "tags"
    type: "array"
    description: "Tags associated with the contact."
    array-attributes:
      - name: "value"
        type: "string"
        description: "The tag associated with the contact."

  - name: "deleted"
    type: "boolean"
    description: "Indicates if the contact has been deleted. This attribute will only be present for contacts that have been deleted in Freshdesk."

  - name: "phone"
    type: "string"
    description: "The phone number of the contact."

  - name: "address"
    type: "string"
    description: "The address of the contact."

  - name: "active"
    type: "boolean"
    description: "Indicates if the contact has been verified."

  - name: "name"
    type: "string"
    description: "The name of the contact."

  - name: "language"
    type: "string"
    description: "The language of the contact."

  - name: "mobile"
    type: "string"
    description: "The mobile number of the contact."

  - name: "created_at"
    type: "date-time"
    description: "The timestamp when the contact was first created."

  - name: "twitter_id"
    type: "string"
    description: "The contact's Twitter ID."

  - name: "time_zone"
    type: "string"
    description: "The timezone in which the contact resides."

  # - name: "avatar"
  #   type: "object"
  #   description: "The contact's avatar."
---
