---
tap: "lever"
version: "1"
key: "opportunity-offer"

name: "opportunity_offers"
doc-link: "https://hire.lever.co/developer/documentation#opportunities"
singer-schema: "https://github.com/singer-io/tap-lever/blob/master/tap_lever/schemas/opportunity_offers.json"
description: |
  The `{{ table.name }}` table contains info about 

  **Note**: To replicate this table, the [`opportunities`](#opportunities) table must be set to replicate.

replication-method: "Key-based Incremental"

replication-key:
  name: "opportunities.updated_at"

api-method:
  name: "List all opportunities"
  doc-link: "https://hire.lever.co/developer/documentation#list-all-opportunities"

attributes:
  - name: "id"
    type: "string"
    description: "The offer ID."
    foreign-key-id: "offer-id"

  - name: "approved"
    type: "boolean"
    description: ""

  - name: "approvedAt"
    type: "date-time"
    description: "The datetime when the offer was approved."

  - name: "createdAt"
    type: "date-time"
    description: "The datetime when the offer was created."

  - name: "creator"
    type: "string"
    description: "The ID of the offer creator."
    foreign-key-id: "user-id"

  - name: "fields"
    type: "array"
    description: "Details about the fields on the offer. This includes standard fields and all custom fields."
    subattributes:
      - name: "identifier"
        type: "string"
        description: "The underscored, machine-readable name identifier of the field."

      - name: "text"
        type: "string"
        description: "The plain text name of the field."

      - name: "value"
        type: "string"
        description: "The value of the field."

  - name: "opportunityId"
    type: "string"
    description: "The ID of the opportunity associated with the offer."
    foreign-key-id: "opportunity-id"

  - name: "posting"
    type: "string"
    description: "The ID of the posting associated with the offer."
    foreign-key-id: "posting-id"

  - name: "sentAt"
    type: "date-time"
    description: "The datetime when the offer was sent."

  - name: "sentDocument"
    type: "object"
    description: "Details about the document sent to the candidate."
    subattributes: &file-attributes
      - name: "downloadUrl"
        type: "string"
        description: "The URL to access the file."

      - name: "fileName"
        type: "string"
        description: "The name of the file."

      - name: "uploadedAt"
        type: "date-time"
        description: "The timestamp when the file was uploaded."

  - name: "signatures"
    type: "object"
    description: "Details about the signature(s) associated with the offer."
    subattributes:
      - name: "candidate"
        type: "object"
        description: "Details about the candidate's signature."
        subattributes:
          - name: "email"
            type: "string"
            description: "The email of the candidate."

          - name: "firstOpenedAt"
            type: "date-time"
            description: "The time when the candidate first opened the offer."

          - name: "lastOpenedAt"
            type: "date-time"
            description: "The time when the candidate last opened the offer."

          - name: "name"
            type: "string"
            description: "The name of the candidate."

          - name: "role"
            type: "string"
            description: "The role of the candidate."

          - name: "signed"
            type: "boolean"
            description: "If `true`, the candidate signed the offer."

          - name: "signedAt"
            type: "date-time"
            description: "The time when the candidate signed the offer."

      - name: "email"
        type: "string"
        description: "The email of the signee."

      - name: "firstOpenedAt"
        type: "date-time"
        description: "The time when the signee first opened the offer."

      - name: "lastOpenedAt"
        type: "date-time"
        description: "The time when the signee last opened the offer."

      - name: "name"
        type: "string"
        description: "The name of the signee."

      - name: "role"
        type: "string"
        description: "The role of the signee."

      - name: "signed"
        type: "boolean"
        description: "If `true`, the signee signed the offer."

      - name: "signedAt"
        type: "date-time"
        description: "The time when the signee signed the offer."

  - name: "signedDocument"
    type: "object"
    description: "Details about the signed offer file."
    subattributes: *file-attributes

  - name: "status"
    type: "string"
    description: |
      The status of the offer. Possible values are:

      - `draft` - The offer is still under construction
      - `approval-sent` - The offer needs approval
      - `approved` - The offer has been approved
      - `sent` - The offer has been sent through Lever
      - `sent-manually` - The offer has been sent to the candidate outside of {{ integration.display_name }}
      - `opened` - The candidate has opened the offer
      - `denied` - The candidate denied the offer
      - `signed` - The candidate signed the offer
---