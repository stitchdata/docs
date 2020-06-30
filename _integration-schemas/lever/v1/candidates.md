---
tap: "lever"
version: "1"
key: "candidate"

name: "candidates"
doc-link: "https://hire.lever.co/developer/documentation#candidates"
singer-schema: "https://github.com/singer-io/tap-lever/blob/master/tap_lever/schemas/candidates.json"
description: |
  The `{{ table.name }}` table contains info about candidates, or individuals who've been added to your {{ integration.display_name }} account as potential fits for job opportunities.

  **Note**: This table must be set to replicate in order to replicate the `candidate_applications`, `candidate_offers`, `candidate_referrals`, and `candidate_resumes` tables.

  During Extraction, this table will be replicated before any other selected `candidate_*` tables. Then, for every candidate, Stitch will query for every candidate's applications, offers, referrals, and resumes.

  For example: During Extraction, Stitch replicates a candidate with `id: 12345` from {{ integration.display_name }}'s `/candidates` endpoint.

  Using `id: 12345`, Stitch will then query for the rest of the candidate's data:

  - `/candidates/12345/applications`
  - `/candidates/12345/offers`
  - `/candidates/12345/referrals`
  - `/candidates/12345/resumes`

replication-method: "Key-based Incremental"

replication-key:
  name: "updated_at"

api-method:
  name: "List all candidates"
  doc-link: "https://hire.lever.co/developer/documentation#list-all-candidates"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The candidate ID."
    foreign-key-id: "candidate-id"

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
    description: "Details about the candidate's archived status."
    subattributes:
      - name: "archivedAt"
        type: "date-time"
        description: "The datetime when the candidate was archived."

      - name: "reason"
        type: "string"
        description: "The ID of the archive reason applied to the candidate."
        foreign-key-id: "archive-reason-id"

  - name: "contact"
    type: "string"
    description: "The candidate's contact ID."
    foreign-key-id: "contact-id"

  - name: "createdAt"
    type: "date-time"
    description: "The datetime when the candidate was created in {{ integration.display_name }}."

  - name: "dataProtection"
    type: "object"
    description: "Details about the candidate's data protection status, based on candidate-provided consent and applicable data policy regulations. If there isn't a policy in place or if no policies are applicable to the candidate, the values of these fields may be `null`."
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
    description: "A list of emails for the candidate."
    subattributes:
      - name: "value"
        type: "string"
        description: "The email address."

  - name: "followers"
    type: "array"
    description: "A list of IDs of the users following the candidate."
    subattributes:
      - name: "value"
        type: "string"
        description: "The follower's user ID."
        foreign-key-id: "user-id"

  - name: "headline"
    type: "string"
    description: "The candidate's headline. This is typically a list of previous companies where the candidate has worked or schools the candidate has attended."

  - name: "isAnonymized"
    type: "boolean"
    description: "If `true`, the candidate has been anonymized."

  - name: "lastAdvancedAt"
    type: "date-time"
    description: "The datetime when the candidate advanced to the current `stage`."

  - name: "lastInteractionAt"
    type: "date-time"
    description: "The datetime when the last interaction with candidate occurred."

  - name: "links"
    type: "array"
    description: "A list of links for the candidate."
    subattributes:
      - name: "value"
        type: "string"
        description: "The link URL."

  - name: "location"
    type: "string"
    description: "The candidate's current location."

  - name: "name"
    type: "string"
    description: "The candidate's full name."

  - name: "origin"
    type: "string"
    description: |
      The way the candidate was added to {{ integration.display_name }}. Possible values are:

      - `agency`
      - `applied`
      - `internal`
      - `referred`
      - `sourced`
      - `university`

  - name: "owner"
    type: "string"
    description: "The ID of the owner of the candidate."
    foreign-key-id: "user-id"

  - name: "phones"
    type: "array"
    description: "A list of phone numbers for the candidate."
    subattributes:
      - name: "type"
        type: "string"
        description: "The type of phone number."

      - name: "value"
        type: "string"
        description: "The phone number."

  - name: "resume"
    type: "object"
    description: "Details about the candidate's resume."
    subattributes: 

  - name: "snoozedUntil"
    type: "date-time"
    description: "If the candidate is snoozed, this field will reflect the datetime when the snooze period ends."

  - name: "sources"
    type: "array"
    description: "A list of sources associated with the candidate."
    subattributes:
      - name: "value"
        type: "string"
        description: "The source."
        # foreign-key-id: "source-id"

  - name: "stage"
    type: "string"
    description: "The ID of the candidate's current stage."
    foreign-key-id: "stage-id"

  - name: "stageChanges"
    type: "array"
    description: "Historical details of the candidate's stage changes."
    subattributes:
      - name: "toStageId"
        type: "string"
        description: "The ID of the stage the candidate entered."
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
    description: "A list of tags applied to the candidate."
    subattributes:
      - name: "value"
        type: "string"
        description: "The tag."

  - name: "urls"
    type: "object"
    description: "A list of list and show URLs for the candidate."
    subattributes: 
      - name: "list"
        type: "string"
        description: "The URL that points to the account's list of candidates."

      - name: "show"
        type: "string"
        description: "The URL that points to the candidate's profile page for this opportunity."
---