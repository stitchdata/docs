---
tap: "hubspot"
version: "1.0"

name: "contacts"
doc-link: https://developers.hubspot.com/docs/methods/contacts/contacts-overview
singer-schema: https://github.com/singer-io/tap-hubspot/blob/master/tap_hubspot/schemas/contacts.json
description: |
  The `contacts` table contains info about individual contacts in HubSpot.

notes: 

replication-method: "Full Table"
api-method:
  name: getContacts
  doc-link: https://developers.hubspot.com/docs/methods/contacts/get_contacts

attributes:
## Primary Key
  - name: "canonical-vid"
    type: "integer"
    primary-key: true
    description: "The canonical ID of the contact. In {{ integration.display_name }}, contacts may have multiple vids, but the canonical-vid will be the primary ID for a contact."

  - name: "vid"
    type: "integer"
    description: "The internal ID of the contact."

  - name: "merged-vids"
    type: "array"
    description: "A list of vids that have been merged into this contact record."
    array-attributes:
      - name: "type"
        type: "integer"
        description: "The vid that was merged into the contact record."

  - name: "portal-id"
    type: "integer"
    alias: "portalId"
    description: "The ID of the portal the contact is associated with."

  - name: "is-contact"
    type: "boolean"
    description: "Indicates if the contact is a valid contact. "

  - name: "profile-token"
    type: "string"
    description: "A unique token that can be used to view the contact without logging into {{ integration.display_name }}."

  - name: "profile-url"
    type: "string"
    description: "A unique token that can be used to view the contact without logging into {{ integration.display_name }}. Anyone with this URL can view (not edit) the contact's record."

  # - name: "associated-company"
  #   type: "object"
  #   description: ""

  - name: "identity-profiles"
    type: "array"
    description: "A list of the identities of the contact."
    array-attributes:
      - name: "deleted-changed-timestamp"
        type: "date-time"
        description: "The timestamp of the last delete or change event associated with a contact's identity profile."

      - name: "saved-at-timestamp"
        type: "date-time"
        description: "A Unix timestamp in milliseconds of when the identity was last updated."

      - name: "vid"
        type: "integer"
        description: "The original vid for the identity."

      - name: "identities"
        type: "array"
        description: "A list of individual identities for the contact."
        array-attributes:
          - name: "timestamp"
            type: "date-time"
            description: "A Unix timestamp in milliseconds for when the identity was created."

          - name: "type"
            type: "string"
            description: "The type of identity. According to {{ integration.display_name }}'s documentation, this will be either `email` or `lead_guid`."

          - name: "value"
            type: "string"
            description: "The value of the identity. For example: `stitch-hubspot@stitchdata.com`"

  - name: "list-memberships"
    type: "array"
    description: "A list of the contact's memberships in contact lists."
    array-attributes:
      - name: "internal-list-id"
        type: "integer"
        description: "The internal list ID."

      - name: "is-member"
        type: "boolean"
        description: "Indicates if the contact is a member of the list."

      - name: "static-list-id"
        type: "integer"
        description: "The ID of the contact list."

      - name: "timestamp"
        type: "date-time"
        description: "A Unix timestamp in milliseconds for when the contact joined the list."

      - name: "vid"
        type: "integer"
        description: "The vid of the contact record."

  - name: "form-submissions"
    type: "array"
    description: "A list of form submissions for the contact."
    array-attributes:
      - name: "conversion-id"
        type: "string"
        description: "A unique ID for the specific form conversion."

      - name: "timestamp"
        type: "date-time"
        description: "A Unix timestamp in milliseconds of the time the submission occurred."

      - name: "form-id"
        type: "string"
        description: "The GUID of the form the submission belongs to."

      - name: "portal-id"
        type: "integer"
        description: "The ID of the portal the submission belongs to."

      - name: "page-url"
        type: "string"
        description: "The URL that the form was submitted on."

      - name: "title"
        type: "string"
        description: "The title of the page that the form was submitted on."

  - name: "merge-audits"
    type: "array"
    description: "Details about any merges that have happened for the record."
    array-attributes:
      - name: "canonical-vid"
        type: "integer"
        description: "The vid of the primary contact, or the record that was merged into."

      - name: "vid-to-merge"
        type: "integer"
        description: "The vid of the secondary contact, or the record that the data was merged from."

      - name: "timestamp"
        type: "date-time"
        description: "A Unix timestamp in milliseconds of when the merge occurred."

      - name: "user-id"
        type: "integer"
        description: "The internal ID of the user who performed the merge."

      - name: "num-properties-moved"
        type: "integer"
        description: "The number of properties that were updated as a result of the merge."

      - name: "merged-from-email"
        type: "object"
        description: "Data from the secondary contact, or the record that the data was merged from."
        object-attributes:
          - name: "value"
            type: "string"
            description: "The email address of the secondary contact at the time of the merge."

          - name: "source-type"
            type: "string"
            description: "The method by which the email property was last updated. For example: `contacts_web`"

          - name: "source-id"
            type: "string"
            description: "Additional data related to the `source-type`."

          - name: "source-label"
            type: "string"
            description: "Additional data related to the `source-type`."

          - name: "timestamp"
            type: "integer"
            description: "A Unix timestamp in milliseconds for when the last email address was last updated."

          - name: "selected"
            type: "boolean"
            description: &deprecated-field Deprecated by {{ integration.display_name }}.

          - name: "source-vids"
            type: "array"
            description: "A list of secondary contact vids."
            array-attributes:
              - name: "items"
                type: "integer"
                description: "The secondary contact's vid."

      - name: "merged-to-email"
        type: "object"
        description: "Data for the primary contact, or the record the data was merged into."
        object-attributes:
          - name: "value"
            type: "string"
            description: "The email address of the primary contact at the time of the merge."

          - name: "source-type"
            type: "string"
            description: "The method by which the last email property was updated. For example: `contacts_web`"

          - name: "source-id"
            type: "string"
            description: "Additional data related to the `source-type`."

          - name: "source-label"
            type: "string"
            description: "Additional data related to the `source-type`."

          - name: "timestamp"
            type: "integer"
            description: "A Unix timestamp in milliseconds for when the last email address was last updated."

          - name: "selected"
            type: "boolean"
            description: *deprecated-field
---
