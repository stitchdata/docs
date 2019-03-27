---
tap: "closeio"
version: "1.0"

name: "leads"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-closeio/blob/master/tap_closeio/schemas/leads.json"

description: |
  The `{{ table.name }}` table contains info about the leads in your {{ integration.display_name }} account.

  Leads represent a company or organization and may contain contacts, tasks, opportunities, and activities. In {{ integration.display_name }}, a lead is synonymous with "account" in other CRMs.

replication-method: "Key-based Incremental"

api-method:
  name: "List or search for leads"
  doc-link: "https://developer.close.io/#leads-list-or-search-for-leads"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The lead ID."
    foreign-key-id: "lead-id"

  - name: "date_updated"
    type: "string"
    replication-key: true
    description: "The time the lead was last updated."

  - name: "addresses"
    type: "array"
    description: "A list of physical addresses associated with the lead."
    subattributes:
      - name: "address_1"
        type: "string"
        description: "The first line of the lead's address."

      - name: "address_2"
        type: "string"
        description: "The second line of the lead's address."

      - name: "city"
        type: "string"
        description: "The city."

      - name: "country"
        type: "string"
        description: "The country."

      - name: "label"
        type: "string"
        description: "The label for the address. For example: `business` or `home`"

      - name: "state"
        type: "string"
        description: "The state."

      - name: "zipcode"
        type: "string"
        description: "The zipcode."

  - name: "contacts"
    type: "array"
    description: "A list of contacts associated with the lead."
    subattributes:
      - name: "id"
        type: "string"
        primary-key: true
        description: "The contact ID."
        foreign-key-id: "contact-id"

      - name: "created_by"
        type: "string"
        description: "The ID of the user who created the contact."
        foreign-key-id: "user-id"

      - name: "date_created"
        type: "string"
        description: "The date the contact was created."

      - name: "date_updated"
        type: "string"
        description: "The date the contact was updated."

      - name: "display_name"
        type: "string"
        description: "The display name of the contact."

      - name: "emails"
        type: "array"
        description: "A list of the email addresses associated with the contact."
        subattributes:
          - name: "email"
            type: "string"
            description: "The contact's email address."

          - name: "type"
            type: "string"
            description: "The type of email address. For example: `office`"

      - name: "integration_links"
        type: "array"
        description: "A list of integration links associated with the contact."
        subattributes:
          - name: "name"
            type: "string"
            description: &integration-link-name "The name of the integration link."

          - name: "url"
            type: "string"
            description: &integration-link-url "The URL of the integration link."

      - name: "lead_id"
        type: "string"
        description: "The lead ID associated with the contact."
        foreign-key-id: "lead-id"

      - name: "name"
        type: "string"
        description: "The name of the contact."

      - name: "organization_id"
        type: "string"
        description: "The ID of the organization associated with the contact."
        foreign-key-id: "organization-id"

      - name: "phones"
        type: "array"
        description: "A list of phone numbers associated with the contact."
        subattributes:
          - name: "phone"
            type: "string"
            description: "The phone number associated with the contact."

          - name: "phone_formatted"
            type: "string"
            description: "The formatted version of `phone`."

          - name: "type"
            type: "string"
            description: "The type of phone number. For example: `office`"

      - name: "title"
        type: "string"
        description: "The contact's title."

      - name: "updated_by"
        type: "string"
        description: "The ID of the user who last updated the contact."
        foreign-key-id: "user-id"

      - name: "urls"
        type: "array"
        description: ""
        subattributes:
          - name: "value"
            type: "string"
            description: ""

  - name: "created_by"
    type: "string"
    description: "The ID of the user who created the lead."
    foreign-key-id: "user-id"

  - name: "created_by_name"
    type: "string"
    description: "The name of the user who created the lead."

  - name: "custom_fields"
    type: "array"
    description: "A list of custom fields associated with the lead, if applicable."
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "date_created"
    type: "string"
    description: "The date the lead was created."

  - name: "description"
    type: "string"
    description: "The description of the lead."

  - name: "display_name"
    type: "string"
    description: "The display name of the lead."

  - name: "html_url"
    type: "string"
    description: "The {{ integration.display_name }} URL for the lead."

  - name: "integration_links"
    type: "array"
    description: "A list of integration links associated with the lead."
    subattributes:
      - name: "name"
        type: "string"
        description: *integration-link-name

      - name: "url"
        type: "string"
        description: *integration-link-url

  - name: "name"
    type: "string"
    description: "The name of the lead."

  - name: "opportunities"
    type: "array"
    description: "A list of opportunities associated with the lead."
    subattributes:
      - name: "id"
        type: "string"
        primary-key: true
        description: "The opportunity ID."

      - name: "confidence"
        type: "integer"
        description: "The opportunity's confidence score."

      - name: "contact_id"
        type: "string"
        description: "The contact ID associated with the opportunity."
        foreign-key-id: "contact-id"

      - name: "contact_name"
        type: "string"
        description: "The contact name associated with the opportunity."

      - name: "created_by"
        type: "string"
        description: "The ID of the user who created the opportunity."
        foreign-key-id: "user-id"

      - name: "created_by_name"
        type: "string"
        description: "The name of the user who created the opportunity."

      - name: "date_created"
        type: "string"
        description: "The date the opportunity was created."

      - name: "date_lost"
        type: "string"
        description: "The date the opportunity was lost."

      - name: "date_updated"
        type: "string"
        description: "The date the opportunity was last updated."

      - name: "date_won"
        type: "string"
        description: "The date the opportunity was won."

      - name: "integration_links"
        type: "array"
        description: "A list of integration links associated with the opportunity."
        subattributes:
          - name: "name"
            type: "string"
            description: *integration-link-name

          - name: "url"
            type: "string"
            description: *integration-link-url

      - name: "lead_id"
        type: "string"
        description: "The ID of the lead associated with the opportunity."
        foreign-key-id: "lead-id"

      - name: "lead_name"
        type: "string"
        description: "The name of the lead associated with the opportunity."

      - name: "note"
        type: "string"
        description: "Any notes about the opportunity."

      - name: "organization_id"
        type: "string"
        description: "The ID of the organization associated with the opportunity."
        foreign-key-id: "organization-id"

      - name: "status_id"
        type: "string"
        description: "The ID of the status associated with the opportunity."

      - name: "status_label"
        type: "string"
        description: "The status label. For example: `Active`"

      - name: "status_type"
        type: "string"
        description: "The status type. For example: `active`"

      - name: "updated_by"
        type: "string"
        description: "The ID of the user who last updated the opportunity."
        foreign-key-id: "user-id"

      - name: "updated_by_name"
        type: "string"
        description: "The name of the user who last updated the opportunity."

      - name: "user_id"
        type: "string"
        description: "The ID of the user associated with the opportunity."
        foreign-key-id: "user-id"

      - name: "user_name"
        type: "string"
        description: "The name of the user associated with the opportunity."

      - name: "value"
        type: "integer"
        description: "The value of the opportunity."

      - name: "value_currency"
        type: "string"
        description: "The currency code of the opportunity's `value`."

      - name: "value_formatted"
        type: "string"
        description: "The formatted version of `value`."

      - name: "value_period"
        type: "string"
        description: "The opportunity's value period. For example: `one_time`"

  - name: "organization_id"
    type: "string"
    description: "The ID of the organization associated with the lead."
    foreign-key-id: "organization-id"

  - name: "status_id"
    type: "string"
    description: "The ID of the status associated with the lead."

  - name: "status_label"
    type: "string"
    description: "The status label. For example: `Active`"

  - name: "tasks"
    type: "array"
    description: "A list of tasks associated with the lead."
    subattributes:
      - name: "id"
        type: "string"
        primary-key: true
        description: "The task ID."
        foreign-key-id: "task-id"

      - name: "_type"
        type: "string"
        description: |
          The task type. Possible values are:

          - `answered_detached_call` 
          - `email_followup`
          - `incoming_email`
          - `incoming_sms`
          - `lead`
          - `missed_call`
          - `opportunity_due`
          - `voicemail`

      - name: "assigned_to"
        type: "string"
        description: "The ID of the user the task is assigned to."
        foreign-key-id: "user-id"

      - name: "assigned_to_name"
        type: "string"
        description: "The name of the user the task is assigned to."

      - name: "contact_id"
        type: "string"
        description: "The ID of the contact associated with the task."
        foreign-key-id: "contact-id"

      - name: "contact_name"
        type: "string"
        description: "The name of the contact associated with the task."

      - name: "created_by"
        type: "string"
        description: "The ID of the user who created the task."
        foreign-key-id: "user-id"

      - name: "created_by_name"
        type: "string"
        description: "The name of the user who created the task."

      - name: "date"
        type: "string"
        description: "The date of the task."

      - name: "date_created"
        type: "string"
        description: "The date the task was created."

      - name: "date_updated"
        type: "string"
        description: "The date the task was updated."

      - name: "due_date"
        type: "string"
        description: "The date the task is due."

      - name: "is_complete"
        type: "boolean, integer"
        description: "Indicates if the task is complete."

      - name: "is_dateless"
        type: "boolean, integer"
        description: "Indicates if the task is dateless."

      - name: "lead_id"
        type: "string"
        description: "The ID of the lead associated with the task."
        foreign-key-id: "lead-id"

      - name: "lead_name"
        type: "string"
        description: "The name of the lead associated with the task."

      - name: "object_id"
        type: "string"
        description: |
          The object ID. The value of this field varies depending on a task's `_type`:

          - `answered_detached_call` - The ID of the corresponding call.
          - `email_followup` - The ID of the corresponding email thread.
          - `incoming_email` - The ID of the corresponding email thread.
          - `incoming_sms` - The ID of the corresponding SMS.
          - `missed_call` - The `activity` ID of the call that was missed.
          - `opportunity_due` - The ID of the corresponding opportunity.
          - `voicemail` - The `activity` ID of the call that was missed.

      - name: "object_type"
        type: "string"
        description: |
          The object type. Possible values vary depending on a task's `_type`:

          - `answered_detached_call` - `call`
          - `email_followup` - `emailthread`
          - `incoming_email` - `emailthread`
          - `incoming_sms` - `sms`
          - `missed_call` - `call`
          - `opportunity_due` - `opportunity`
          - `voicemail` - `call`

      - name: "organization_id"
        type: "string"
        description: "The ID of the organization associated with the lead."
        foreign-key-id: "organization-id"

      - name: "text"
        type: "string"
        description: "For `lead` and `incoming_sms` tasks, the text that was sent."

      - name: "updated_by"
        type: "string"
        description: "The ID of the user who last updated the task."
        foreign-key-id: "user-id"

      - name: "updated_by_name"
        type: "string"
        description: "The name of the user who last updated the task."

      - name: "view"
        type: "string"
        description: "The view associated with the task."

  - name: "updated_by"
    type: "string"
    description: "The ID of the user who last updated the lead."
    foreign-key-id: "user-id"

  - name: "updated_by_name"
    type: "string"
    description: "The name of the user who last updated the lead."

  - name: "url"
    type: "string"
    description: "The {{ integration.display_name }} URL of the lead."
---