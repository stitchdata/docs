---
tap: "autopilot"

name: "contacts"
doc-link: http://docs.autopilot.apiary.io/#reference/api-methods/get-all-contacts
singer-schema: https://github.com/singer-io/tap-autopilot/blob/master/tap_autopilot/schemas/contacts.json
description: |
  The `contacts` table contains info about the contacts in your Autopilot account.

  Any custom fields associated with contacts will also be replicated.

replication-method: "Key-based Incremental"
api-method:
  name: "getAllContacts"
  doc-link: http://docs.autopilot.apiary.io/#reference/api-methods/get-all-contacts

attributes:
  - name: "contact_id"
    type: "string"
    primary-key: true
    description: "The contact ID."

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the contact was last updated."

  - name: "name"
    type: "string"
    description: "The name of the contact."

  - name: "first_name"
    type: "string"
    description: "The first name of the contact."

  - name: "last_name"
    type: "string"
    description: "The last name of the contact."

  - name: "company"
    type: "string"
    description: "The company of the contact."

  - name: "company_priority"
    type: "boolean"
    description: "Indicates the contact's company priority."

  - name: "email"
    type: "string"
    description: "The email address of the contact."

  - name: "lead_source"
    type: "string"
    description: "The lead source of the contact."

  - name: "mailing_country"
    type: "string"
    description: "The mailing country of the contact."

  - name: "mailing_state"
    type: "string"
    description: "The mailing state of the contact."

  - name: "phone"
    type: "string"
    description: "The phone number associated with the contact."

  - name: "status"
    type: "string"
    description: "The status of the contact."

  - name: "salutation"
    type: "string"
    description: "The salutation of the contact. Ex: `Mr.`"

  - name: "anywhere_page_visits"
    type: "array"
    description: "Details about the contact's page visits."
    subattributes:
      - name: "url"
        type: "string"
        description: "The URL associated with the page visit."

      # - name: "value"
      #   type: "boolean"
      #   description: ""

  - name: "anywhere_utm"
    type: "array"
    description: "Details about the UTM parameters associated with the contact's page visits."
    subattributes:
      - name: "url"
        type: "string"
        description: "The UTM parameter and value associated with the page visit."

      # - name: "value"
      #   type: "boolean"
      #   description: ""

  - name: "mail_opened"
    type: "array"
    description: "Details about the emails opened by the contact."
    subattributes:
      - name: "id"
        type: "string"
        description: "The ID of the email."

      - name: "timestamp"
        type: "date-time"
        description: "The time the email was opened by the contact."

  - name: "mail_received"
    type: "array"
    description: "Details about the emails received by the contact."
    subattributes:
      - name: "id"
        type: "string"
        description: "The ID of the email."

      - name: "timestamp"
        type: "date-time"
        description: "The time the email was received by the contact."

  - name: "mail_bounced"
    type: "array"
    description: "Details about the emails sent to the contact that have bounced."
    subattributes:
      - name: "id"
        type: "string"
        description: "The ID of the email."

      - name: "timestamp"
        type: "date-time"
        description: "The time the email bounced."

  - name: "mail_hardbounced"
    type: "array"
    description: "Details about the emails sent to the contact that have hardbounced."
    subattributes:
      - name: "id"
        type: "string"
        description: "The ID of the email."

      - name: "timestamp"
        type: "date-time"
        description: "The time the email hardbounced."

  - name: "mail_clicked"
    type: "array"
    description: "Details about the emails clicked by the contact."
    subattributes:
      - name: "id"
        type: "string"
        description: "The ID of the email."

      - name: "timestamp"
        type: "date-time"
        description: "The time the email was clicked by the contact."

  - name: "mail_complained"
    type: "array"
    description: "Details about the emails the contact reported as spam."
    subattributes:
      - name: "id"
        type: "string"
        description: "The ID of the email."

      - name: "timestamp"
        type: "date-time"
        description: "The time the contact reported the email as spam."

  - name: "twitter"
    type: "string"
    description: "The Twitter handle associated with the contact."

  - name: "mail_unsubscribed"
    type: "array"
    description: "Details about the emails the contact has unsubscribed from."
    subattributes:
      - name: "id"
        type: "string"
        description: "The ID of the email."

      - name: "timestamp"
        type: "date-time"
        description: "The time the contact unsubscribed."

  - name: "created_at"
    type: "date-time"
    description: "The time the contact was created."

  - name: "first_conversion_at"
    type: "date-time"
    description: "The time the contact first converted."

  - name: "first_visit_at"
    type: "date-time"
    description: "The time of the contact's first visit."

  - name: "lists"
    type: "array"
    description: "The IDs of the lists that the contact belongs to."
    subattributes:
      - name: "value"
        type: "string"
        description: "The ID of the contact list."
---