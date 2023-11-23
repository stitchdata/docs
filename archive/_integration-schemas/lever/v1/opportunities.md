---
tap: "lever"
version: "1"
key: "opportunity"

name: "opportunities"
doc-link: "https://hire.lever.co/developer/documentation#opportunities"
singer-schema: "https://github.com/singer-io/tap-lever/blob/master/tap_lever/schemas/opportunities.json"
description: |
  The `{{ table.name }}` table contains info about opportunities. In {{ integration.display_name }}, an opportunity represents each of an individual candidate's unique candidacies or journeys through your hiring pipeline for a position. A candidate can be associated with multiple opportunities.

  **Note**: This table must be set to replicate in order to replicate the `opportunity_applications`, `opportunity_offers`, `opportunity_referrals`, and `opportunity_resumes` tables.

  During Extraction, this table will be replicated before any other selected `opportunity_*` tables. Then, for every opportunity, Stitch will query for every opportunity's applications, offers, referrals, and resumes.

  For example: During Extraction, Stitch replicates an opportunity with `id: 12345` from {{ integration.display_name }}'s `/opportunities` endpoint.

  Using `id: 12345`, Stitch will then query for the rest of the opportunity's data:

  - `/opportunities/12345/applications`
  - `/opportunities/12345/offers`
  - `/opportunities/12345/referrals`
  - `/opportunities/12345/resumes`

replication-method: "Key-based Incremental"

replication-key:
  name: "updated_at"

api-method:
  name: "List all opportunities"
  doc-link: "https://hire.lever.co/developer/documentation#list-all-opportunities"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The opportunity ID."
    foreign-key-id: "opportunity-id"

  - name: "applications"
    type: "array"
    description: "The ID of the candidate's application."
    subattributes:
      - name: "value"
        type: "string"
        description: "The application ID."
        foreign-key-id: "application-id"

  - name: "archived"
    type: "object"
    description: "Details about the opportunity's archived status."
    subattributes:
      - name: "archivedAt"
        type: "date-time"
        description: "The datetime when the opportunity was archived."

      - name: "reason"
        type: "string"
        description: "The ID of the archive reason applied to the opportunity."
        foreign-key-id: "archive-reason-id"

  - name: "contact"
    type: "string"
    description: "The opportunity's contact ID."
    foreign-key-id: "contact-id"

  - name: "createdAt"
    type: "date-time"
    description: "The datetime when the opportunity was created in {{ integration.display_name }}."

  - name: "dataProtection"
    type: "object"
    description: "Details about the opportunity's data protection status, based on opportunity-provided consent and applicable data policy regulations. If there isn't a policy in place or if no policies are applicable to the opportunity, the values of these fields may be `null`."
    subattributes:
      - name: "contact"
        type: "object"
        description: "Details about the consent status for a specified processing activity."
        subattributes: &consent-status
          - name: "allowed"
            type: "boolean"
            description: "If `true`, the applicable data policy regulation allows for storage of this record."

          - name: "expiresAt"
            type: "date-time"
            description: "The timestamp when this permission expires."

      - name: "store"
        type: "object"
        description: "Details about the consent status for a specified processing activity."
        subattributes: *consent-status

  - name: "emails"
    type: "array"
    description: "A list of emails for the opportunity."
    subattributes:
      - name: "value"
        type: "string"
        description: "The email address."

  - name: "followers"
    type: "array"
    description: "A list of IDs of the users following the opportunity."
    subattributes:
      - name: "value"
        type: "string"
        description: "The follower's user ID."
        foreign-key-id: "user-id"

  - name: "headline"
    type: "string"
    description: "The contact's headline. This is typically a list of previous companies where the contact has worked or schools the contact has attended."

  - name: "isAnonymized"
    type: "boolean"
    description: "If `true`, the opportunity has been anonymized."

  - name: "lastAdvancedAt"
    type: "date-time"
    description: "The datetime when the candidate advanced to the current `stage` for this opportunity."

  - name: "lastInteractionAt"
    type: "date-time"
    description: "The datetime when the last interaction with opportunity occurred."

  - name: "links"
    type: "array"
    description: "A list of links for the opportunity."
    subattributes:
      - name: "value"
        type: "string"
        description: "The link URL."

  - name: "location"
    type: "string"
    description: "The opportunity's current location."

  - name: "name"
    type: "string"
    description: "The opportunity's full name."

  - name: "origin"
    type: "string"
    description: |
      The way the opportunity was added to {{ integration.display_name }}. Possible values are:

      - `agency`
      - `applied`
      - `internal`
      - `referred`
      - `sourced`
      - `university`

  - name: "owner"
    type: "string"
    description: "The ID of the owner of the opportunity."
    foreign-key-id: "user-id"

  - name: "phones"
    type: "array"
    description: "A list of phone numbers for the opportunity."
    subattributes:
      - name: "type"
        type: "string"
        description: "The type of phone number."

      - name: "value"
        type: "string"
        description: "The phone number."

  - name: "resume"
    type: "object"
    description: "Details about the opportunity's resume. **This field has been deprecated by {{ integration.display_name }}.**"

  - name: "snoozedUntil"
    type: "date-time"
    description: "If the opportunity is snoozed, this field will reflect the datetime when the snooze period ends."

  - name: "sources"
    type: "array"
    description: "A list of sources associated with the opportunity."
    subattributes:
      - name: "value"
        type: "string"
        description: "The source."

  - name: "stage"
    type: "string"
    description: "The ID of the opportunity's current stage."
    foreign-key-id: "stage-id"

  - name: "stageChanges"
    type: "array"
    description: "Historical details of the opportunity's stage changes."
    subattributes:
      - name: "toStageId"
        type: "string"
        description: "The ID of the stage the opportunity entered."
        foreign-key-id: "stage-id"

      - name: "toStageIndex"
        type: "integer"
        description: "The index of the stage in the pipeline at the time the stage change occurred."

      - name: "updatedAt"
        type: "date-time"
        description: "The time when the stage change occurred."

      - name: "userId"
        type: "string"
        description: "The user ID."
        foreign-key-id: "user-id"

  - name: "tags"
    type: "array"
    description: "A list of tags applied to the opportunity."
    subattributes:
      - name: "value"
        type: "string"
        description: "The tag."

  - name: "urls"
    type: "object"
    description: "A list of list and show URLs for the opportunity."
    subattributes: 
      - name: "list"
        type: "string"
        description: "The URL that points to the account's list of opportunitys."

      - name: "show"
        type: "string"
        description: "The URL that points to the opportunity's profile page for this opportunity."
---