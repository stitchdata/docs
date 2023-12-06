---
tap: "hubspot"
version: "2"
key: "engagement"

name: "engagements"
doc-link: https://developers.hubspot.com/docs/methods/engagements/engagements-overview
singer-schema: https://github.com/singer-io/tap-hubspot/blob/master/tap_hubspot/schemas/engagements.json
description: |
  The `{{ table.name }}` table contains info about all the engagements in a {{ integration.display_name }} portal.

replication-method: "Key-based Incremental"

api-method:
  name: "Get all engagements"
  doc-link: https://developers.hubspot.com/docs/methods/engagements/get-all-engagements

attributes:
  - name: "engagement_id"
    type: "integer"
    primary-key: true
    description: "The ID for the engagement."
    # foreign-key-id: "engagement-id"

  - name: "lastUpdated"
    type: "date-time"
    replication-key: true
    description: "The time the engagement was last updated."

  - name: "portalId"
    type: "integer"
    description: "The ID of the portal the engagement belongs to."
    foreign-key-id: "portal-id"

  - name: "active"
    type: "boolean"
    description: "Indicates if the engagement is active."

  - name: "createdAt"
    type: "date-time"
    description: "The time the engagement was created."

  - name: "ownerId"
    type: "integer"
    description: "The ID of the owner associated with the engagement."
    foreign-key-id: "owner-id"

  - name: "type"
    type: "string"
    description: "The type of engagement. For example: `NOTE` OR `TASK`"

  - name: "timestamp"
    type: "date-time"
    description: "The time the engagement should appear in the timeline."

  - name: "associations"
    type: "array"
    description: "IDs of the objects associated with the engagement. For example: contacts, deals."
    subattributes:
      - name: "contactIds"
        type: "array"
        description: "IDs of the contacts associated with the engagement."
        subattributes:
          - name: "value"
            type: "integer"
            description: "The ID of the contact associated with the campaign."
            foreign-key-id: "contact-id"

      - name: "companyIds"
        type: "array"
        description: "IDs of the companies associated with the engagement."
        subattributes:
          - name: "value"
            type: "integer"
            description: "The ID of the company associated with the campaign."
            foreign-key-id: "company-id"

      - name: "dealIds"
        type: "array"
        description: "IDs of the deals associated with the engagement."
        subattributes:
          - name: "value"
            type: "integer"
            description: "The ID of the deal associated with the campaign."
            foreign-key-id: "deal-id"

  - name: "attachments"
    type: "array"
    description: "For `NOTE` engagements only. IDs of the files from the file manager that should display in the attachments list when viewing the engagement in HubSpot."
    subattributes:
      - name: "id"
        type: "integer"
        primary-key: true
        description: "The ID of the attachment."

  - name: "metadata"
    type: "object"
    description: "Metadata about the engagement."
    subattributes:
      - name: "body"
        type: "string"
        description: |
          For `NOTE` engagements, this will be the body of the note.

          For `TASK` engagements, this will be the body or details of the task.

          For `MEETING` engagements, this will be the body or details of the meeting.

          For `CALL` engagements, this will be the details or notes of the call.

      - name: "from"
        type: "object"
        description: "For `EMAIL` engagements only. Details about the sender of the email engagement."
        subattributes:
          - name: "email"
            type: "string"
            description: "The email address of the sender."

          - name: "firstName"
            type: "string"
            description: "The first name of the sender."

          - name: "lastName"
            type: "string"
            description: "The last name of the sender."

      - name: "to"
        type: "object"
        description: "For `EMAIL` engagements only. Details about the recipient of the email engagement."
        subattributes:
          - name: "email"
            type: "sring"
            description: "The email address of the recipient."

      - name: "cc"
        type: "object"
        description: "For `EMAIL` engagements only. Details about anyone CC'd on the email engagement."
        subattributes:
          - name: "email"
            type: "string"
            description: "The email of the CC'd recipient."

      - name: "bcc"
        type: "object"
        description: "For `EMAIL` engagements only. Details about anyone BCC'D on the email engagement."
        subattributes:
          - name: "email"
            type: "string"
            description: "The email of the BCC'd recipient."

      - name: "subject"
        type: "string"
        description: |
          For `EMAIL` engagements, this will be the subject of the email.

          For `TASK` engagements, this will be the subject or title of the task.

      - name: "html"
        type: "string"
        description: "For `EMAIL` engagements only. The body of the HTML email."

      - name: "text"
        type: "string"
        description: "For `EMAIL` engagements only. The body of the text-only email."

      - name: "status"
        type: "string"
        description: "For `TASK` engagements only. The status of the task. For example: `COMPLETED`"

      - name: "forObjectType"
        type: "string"
        description: "For `TASK` engagements only. The object type the task is for. For example: `CONTACT`"

      - name: "startTime"
        type: "integer"
        description: "For `MEETING` engagements only. The start time of the meeting."

      - name: "endTime"
        type: "integer"
        description: "For `MEETING` engagements only. The ending time of the meeting."

      - name: "title"
        type: "string"
        description: "For `MEETING` engagements only. The title or subject of the meeting."

      - name: "toNumber"
        type: "string"
        description: "For `CALL` engagements only. The phone number that was called."

      - name: "fromNumber"
        type: "string"
        description: "For `CALL` engagements only. The phone number that placed the call."

      - name: "externalId"
        type: "string"
        description: "For `CALL` engagements only. For calls made in HubSpot, this will be the internal ID of the call."

      - name: "durationMilliseconds"
        type: "integer"
        description: "For `CALL` engagements only. The length of the call in milliseconds."

      - name: "externalAccountId"
        type: "string"
        description: "For `CALL` engagements only. For calls made in HubSpot, this will be the internal ID of the account used to place the call."

      - name: "recordingUrl"
        type: "string"
        description: "For `CALL` engagements only. The URL of the recording file."
---