---
tap: "lever"
version: "1"
key: "opportunity-referral"

name: "opportunity_referrals"
doc-link: "https://hire.lever.co/developer/documentation#opportunities"
singer-schema: "https://github.com/singer-io/tap-lever/blob/master/tap_lever/schemas/opportunity_referrals.json"
description: |
  The `{{ table.name }}` table contains info about the referrals in your {{ integration.display_name }} account.

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
    description: "The referral ID."
    foreign-key-id: "referral-id"

  - name: "baseTemplateId"
    type: "string"
    description: "The form template ID associated with the referral."

  - name: "completedAt"
    type: "date-time"
    description: "The datetime the referral was completed."

  - name: "createdAt"
    type: "date-time"
    description: "The datetime the referral was created."

  - name: "fields"
    type: "array"
    description: "Details about the fields on the referral form."
    subattributes:
      - name: "description"
        type: "string"
        description: "A description of the field."

      - name: "options"
        type: "array"
        description: "The valid values for the field. **Note**: This isn't applicable to all field types."
        subattributes:
          - name: "text"
            type: "string"
            description: "The valid value for the field."

      - name: "prompt"
        type: "string"
        description: |
          If an option for the field isn't selected, this prompt will be displayed. **Note**: This isn't applicable to all field types.

      - name: "required"
        type: "boolean"
        description: "If `true`, the field is required."

      - name: "text"
        type: "string"
        description: "The field's label text."

      - name: "type"
        type: "string"
        description: |
          The field type. Possible values are:

          - `currency`
          - `date`
          - `dropdown`
          - `multiple-choice`
          - `multiple-select`
          - `score`
          - `scorecard`
          - `text`
          - `textarea`
          - `yes-no`

      - name: "value"
        type: "string"
        description: "The value of the field."

  - name: "instructions"
    type: "string"
    description: "The instructions on the referral form."

  - name: "referrer"
    type: "string"
    description: "The ID of the referrer."
    foreign-key-id: "user-id"

  - name: "stage"
    type: "string"
    description: "The stage of the candidate at the time the form was completed."

  - name: "text"
    type: "string"
    description: "The title of the referral form."

  - name: "type"
    type: "string"
    description: "The form type."

  - name: "user"
    type: "string"
    description: "The ID of the referral creator."
    foreign-key-id: "user-id"
---