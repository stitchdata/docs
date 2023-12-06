---
tap: "lever"
version: "1"
key: "candidate-offer"

name: "candidate_offers"
doc-link: "https://hire.lever.co/developer/documentation#offers"
singer-schema: "https://github.com/singer-io/tap-lever/blob/master/tap_lever/schemas/candidate_offers.json"
description: |
  The `{{ table.name }}` table contains data sent to candidates about [`opportunities`](#opportunities) via {{ integration.display_name }}'s Offers feature.

replication-method: "Key-based Incremental"

replication-key:
  name: "candidates.updated_at"

api-method:
  name: "List all offers for a candidate"
  doc-link: "https://hire.lever.co/developer/documentation#list-all-offers"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The offer ID."
    foreign-key-id: "offer-id"

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

  - name: "sentAt"
    type: "date-time"
    description: "The datetime when the offer was sent."

  - name: "signatures"
    type: "object"
    description: "Details about the signature(s) associated with the offer."
    subattributes:
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