---
tap: "closeio"
version: "1.0"

name: "tasks"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-closeio/blob/master/tap_closeio/schemas/tasks.json"

description: |
  The `{{ table.name }}` table contains info about the tasks in your {{ integration.display_name }} account. Tasks are action items with a given date that are assigned to a sales rep.

replication-method: "Key-based Incremental"

api-method:
  name: "List or filter tasks"
  doc-link: "https://developer.close.io/#tasks-list-or-filter-tasks"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The task ID."

  - name: "date_updated"
    type: "string"
    replication-key: true
    description: "The date the task was last updated."

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

  - name: "body_preview"
    type: "string"
    description: |
      For `incoming_email` tasks, a preview of the body content of the email.

  - name: "contact_id"
    type: "string"
    description: "The contact ID associated with the task."
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

  - name: "due_date"
    type: "string"
    description: "The date the task is due."

  - name: "email_id"
    type: "string"
    description: "For `email_followup` tasks, the ID of the email."

  - name: "emails"
    type: "array"
    description: "For `incoming_email` tasks, a list email activity IDs related to the task."
    array-attributes:
      - name: "value"
        type: "string"
        description: "The email ID."

  - name: "is_complete"
    type: "boolean"
    description: "Indicates if the task has been completed."

  - name: "is_dateless"
    type: "boolean"
    description: "Indicates if the task is dateless."

  - name: "lead_id"
    type: "string"
    description: "The ID of the lead associated with the task."
    foreign-key-id: "lead-id"

  - name: "lead_name"
    type: "string"
    description: "The name of the lead associated with the task."

  - name: "local_phone"
    type: "string"
    description: "For `incoming_sms` and `missed_call` tasks, the local phone number."

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

  - name: "opportunity_note"
    type: "string"
    description: "For `opportunity_due` tasks, the note associated with the task."

  - name: "opportunity_value"
    type: "integer"
    description: "For `opportunity_due` tasks, the value of the opportunity."

  - name: "opportunity_value_currency"
    type: "string"
    description: "For `opportunity_due` tasks, the currency code of `opportunity_value`."

  - name: "opportunity_value_formatted"
    type: "string"
    description: "For `opportunity_due` tasks, the formatted version of `opportunity_value`."

  - name: "opportunity_value_period"
    type: "string"
    description: "For `opportunity_due` tasks, the value period of the opportunity. For example: `one_time`"

  - name: "organization_id"
    type: "string"
    description: "The ID of the organization associated with the task."
    foreign-key-id: "organization-id"

  - name: "phone"
    type: "string"
    description: "For `missed_call` and `voicemail` tasks, the phone number."

  - name: "phone_formatted"
    type: "string"
    description: "For `missed_call` and `voicemail` tasks, the formatted version of `phone`."

  - name: "phone_number_description"
    type: "string"
    description: "For `answered_detached_call` and `missed_call` tasks, the phone number description."

  - name: "recording_url"
    type: "string"
    description: "For `answered_detached_call` tasks, the URL of the call recording."

  - name: "remote_phone"
    type: "string"
    description: "For `incoming_sms` tasks, the phone number of the sender."

  - name: "remote_phone_description"
    type: "string"
    description: "For `incoming_sms` tasks, the `remote_phone` description."

  - name: "remote_phone_formatted"
    type: "string"
    description: "For `incoming_sms` tasks, the formatted version of `remote_phone`."

  - name: "subject"
    type: "string"
    description: "For `incoming_email` and `email_followup` tasks, the subject of the email."

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

  - name: "voicemail_duration"
    type: "integer"
    description: "For `voicemail` tasks, the duration of the voicemail."

  - name: "voicemail_url"
    type: "string"
    description: "For `voicemail` tasks, the URL of the voicemail."
---