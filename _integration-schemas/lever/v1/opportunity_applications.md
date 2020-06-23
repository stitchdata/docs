---
tap: "lever"
version: "1"
key: "opportunity-application"

name: "opportunity_applications"
doc-link: "https://hire.lever.co/developer/documentation#list-all-opportunities"
singer-schema: "https://github.com/singer-io/tap-lever/blob/master/tap_lever/schemas/opportunity_applications.json"
description: |
  The `{{ table.name }}` table contains info about candidate applications in your {{ integration.display_name }} account.

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
    primary-key: true
    description: "The opportunity application ID."
    foreign-key-id: "application-id"

  - name: "archived"
    type: "object"
    description: "The application's archived status."
    subattributes:
      - name: "archivedAt"
        type: "number"
        description: "The datetime when the application was last archived."

      - name: "reason"
        type: "string"
        description: "The reason why the application was archived."
        foreign-key-id: "archive-reason-id"

  - name: "candidateId"
    type: "string"
    description: "The ID of the candidate associated with the application."
    foreign-key-id: "opportunity-id"

  - name: "comments"
    type: "string"
    description: "Any additional comments from the candidate included in the application."

  - name: "company"
    type: "string"
    description: "The candidate's current company or organization."

  - name: "createdAt"
    type: "number"
    description: "Datetime the application was created in {{ integration.display_name }}."

  - name: "customQuestions"
    type: "array"
    description: "If application is `type: referral`, this data will include a referral form. If application is `type:posting`, this data will include customized posting forms."
    # subattributes: TODO

  - name: "email"
    type: "string"
    description: "The email address of the candidate who applied."

  - name: "links"
    type: "array"
    description: "A list of links associated with the candidate."
    subattributes:
      - name: "value"
        type: "string"
        description: "The URL of the link."

  - name: "name"
    type: "string"
    description: "The name of the candidate who applied."

  - name: "phone"
    type: "object"
    description: "The phone numbers for the candidate."
    subattributes:
      - name: "type"
        type: "string"
        description: "The type of phone number."

      - name: "value"
        type: "string"
        description: "The phone number."

  - name: "posting"
    type: "string"
    description: "The ID of the job posting associated with the application."
    foreign-key-id: "posting-id"

  - name: "postingHiringManager"
    type: "string"
    description: "The hiring manager of the job posting at the time when the candidate applies to that job."
    foreign-key-id: "user-id"

  - name: "postingOwner"
    type: "string"
    description: "The ID of the user who owned the job posting when the candidate applied to the job."
    foreign-key-id: "user-id"

  - name: "requisitionForHire"
    type: "object"
    description: "If the application was archived as hired against a requisition, this is the data related to the requisition."
    subattributes:
      - name: "id"
        type: "string"
        description: "The ID of the requisition."
        foreign-key-id: "requisition-id"

      - name: "requisitionCode"
        type: "string"
        description: "The `requisitionCode` field from the requisition."

      - name: "hiringManagerOnHire"
        type: "string"
        description: "The ID of the hiring manager specified on the requisition, if any."
        foreign-key-id: "user-id"

  - name: "resume"
    type: "object"
    description: "Details about the candidate's resume. **This field has been deprecated by {{ integration.display_name }}.**"

  - name: "type"
    type: "string"
    description: |
      The type of application. Possible values are:

      - `referral`
      - `user`
      - `posting`

  - name: "user"
    type: "string"
    description: "If the application is a `referral`, this is the user who made the referral."
    foreign-key-id: "user-id"
---