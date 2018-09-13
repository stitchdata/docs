---
tap: "closeio"
version: "1.0"

name: "activities"
doc-link: "https://developer.close.io/#activities"
singer-schema: "https://github.com/singer-io/tap-closeio/blob/master/tap_closeio/schemas/activities.json"

description: |
  The `{{ table.name }}` table contains info about various activities in your {{ integration.display_name }} account.

  An activity belongs to a lead and can represent any type of activity that was performed on a lead or its contact. This includes calls, emails, notes, and so on.

  #### Attribution window {#email-attribution-window}
   When Stitch replicates data for this table, it will use an attribution window of {{ integration.attribution-window }} to fetch updated activities.

   This means that every time a replication job runs, the last 24 hours' worth of data will be replicated for this table. This is because {{ integration.display_name }} doesn't provide a way to query for activites based on a modification time, only when activities are created. A list of available querying methods can be found in [{{ integration.display_name }}'s documentation](https://developer.close.io/#activities-list-or-filter-all-activity-types){:target="new"}.
   
   Refer to the [Replication](#replication) section for more info and examples of how the attribution window is used to query for data.

replication-method: "Append-Only Incremental"
attribution-window: true

api-method:
  name: "List or filter all activity types"
  doc-link: "https://developer.close.io/#activities-list-or-filter-all-activity-types"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The activity ID."
    foreign-key-id: "activity-id"

  - name: "date_created"
    type: "string"
    replication-key: true
    description: "The date the activity was created."

  - name: "_type"
    type: "string"
    description: |
      The activity type. Possible values:

      - `Call`
      - `Created`
      - `Email`
      - `EmailThread`
      - `LeadStatusChange`
      - `OpportunityStatusChange`
      - `TaskCompleted`
      - `SMS`

  - name: "attachments"
    type: "array"
    description: "A list of attachments associated with the activity."
    array-attributes:
      - name: "content_id"
        type: "string"
        primary-key: true
        description: "The attachment's content ID."

      - name: "content_type"
        type: "string"
        description: "The attachment's content type."

      - name: "filename"
        type: "string"
        description: "The file name of the attachment."

      - name: "size"
        type: "integer"
        description: "The size of the attachment."

      - name: "url"
        type: "string"
        description: "The full URL of the attachment."

  - name: "bcc"
    type: "array"
    description: "For `Email` activities, a list of those BCC'd on the email."
    array-attributes:
      - name: "value"
        type: "string"
        description: "The bcc on the email."

  - name: "body_html"
    type: "string"
    description: "For `Email` activities, the body content of the email in HTML format."

  - name: "body_html_quoted"
    type: "array"
    description: ""
    array-attributes:
      - name: "expand"
        type: "boolean, integer"
        description: ""

      - name: "html"
        type: "string"
        description: ""

  - name: "body_preview"
    type: "string"
    description: "A preview of the body content."

  - name: "body_text"
    type: "string"
    description: |
      For `Email` activities, the plain text version of the email body.

  - name: "body_text_quoted"
    type: "array"
    description: ""
    array-attributes:
      - name: "expand"
        type: "boolean, integer"
        description: ""

      - name: "text"
        type: "string"
        description: ""

  - name: "cc"
    type: "array"
    description: "For `Email` activities, a list of those CC'd on the email."
    array-attributes:
      - name: "value"
        type: "string"
        description: "The cc on the email."

  - name: "contact_id"
    type: "string"
    description: "The contact ID associated with the activity."
    foreign-key-id: "contact-id"

  - name: "created_by"
    type: "string"
    description: "The ID of the user who created the activity."
    foreign-key-id: "user-id"

  - name: "created_by_name"
    type: "string"
    description: "The name of the user who created the activity."

  - name: "date_scheduled"
    type: "string"
    description: "The date the activity was scheduled for."

  - name: "date_sent"
    type: "string"
    description: "The date the activity was sent."

  - name: "date_updated"
    type: "string"
    description: "The date the activity was last updated."

  - name: "dialer_id"
    type: "string"
    description: "For `Call` activities, the ID of the person who initiated the call."

  - name: "direction"
    type: "string"
    description: |
      The direction of the call, email, or SMS. Possible values are:

      - **For `Call` or `SMS` activities:** `outbound` or `inbound`
      - **For `Email` activities:** `incoming` or `outgoing`

  - name: "duration"
    type: "integer"
    description: "For `Call` activities, the duration of the call."

  - name: "email_account_id"
    type: "string"
    description: "For `Email` activities, the ID of the email account associated with the activity."

  - name: "envelope"
    type: "object"
    description: "For `Email` activities, details about the email associated with the activity."
    object-attributes:
      - name: "bcc"
        type: "array"
        description: "A list of those BCC'd on the email."
        array-attributes:
          - name: "email"
            type: "string"
            description: "The email of the bcc."

          - name: "name"
            type: "string"
            description: "The name of the bcc."

      - name: "cc"
        type: "array"
        description: "A list of those CC'd on the email."
        array-attributes:
          - name: "email"
            type: "string"
            description: "The email of the cc."

          - name: "name"
            type: "string"
            description: "The name of the cc."

      - name: "date"
        type: "date-time"
        description: "The date the email was sent."

      - name: "from"
        type: "array"
        description: "Details about who sent the email."
        array-attributes:
          - name: "email"
            type: "string"
            description: "The address the email was sent from."

          - name: "name"
            type: "string"
            description: "The name of the person who sent the email."

      - name: "in_reply_to"
        type: "string"
        description: ""

      - name: "is_autoreply"
        type: "boolean, integer"
        description: "If `true`, the email was an autoreply email."

      - name: "message_id"
        type: "string"
        description: "The ID of the message."

      - name: "reply_to"
        type: "array"
        description: ""
        array-attributes:
          - name: "email"
            type: "string"
            description: ""

          - name: "name"
            type: "string"
            description: ""

      - name: "sender"
        type: "array"
        description: "Details about the sender of the email."
        array-attributes:
          - name: "email"
            type: "string"
            description: "The email address of the sender."

          - name: "name"
            type: "string"
            description: "The name of the sender."

      - name: "subject"
        type: "string"
        description: "The subject of the email."

      - name: "to"
        type: "array"
        description: "Details about who the email was sent to."
        array-attributes:
          - name: "email"
            type: "string"
            description: "The email address the email was sent to."

          - name: "name"
            type: "string"
            description: "The name of the email recipient."

  - name: "import_id"
    type: "string"
    description: ""

  - name: "in_reply_to_id"
    type: "string"
    description: ""

  - name: "lead_id"
    type: "string"
    description: "The ID of the lead associated with the activity."
    foreign-key-id: "lead-id"

  - name: "local_phone"
    type: "string"
    description: "For `Call` and `SMS` activities, the local phone number associated with the call or SMS."

  - name: "message_ids"
    type: "array"
    description: "A list of messages associated with the activity."
    array-attributes:
      - name: "value"
        type: "string"
        description: "The message ID."

  - name: "need_smtp_credentials"
    type: "boolean, integer"
    description: ""

  - name: "new_status_id"
    type: "string"
    description: |
      For `LeadStatusChange` and `OpportunityStatusChange` activities, the new status ID.

  - name: "new_status_label"
    type: "string"
    description: |
      For `LeadStatusChange` and `OpportunityStatusChange` activities, the new status label.

  - name: "new_status_type"
    type: "string"
    description: |
      For `LeadStatusChange` and `OpportunityStatusChange` activities, the new status type.

  - name: "note"
    type: "string"
    description: "For `Note` activities, the content of the note."

  - name: "old_status_id"
    type: "string"
    description: |
      For `LeadStatusChange` and `OpportunityStatusChange` activities, the old status ID.

  - name: "old_status_label"
    type: "string"
    description: |
      For `LeadStatusChange` and `OpportunityStatusChange` activities, the old status label.

  - name: "old_status_type"
    type: "string"
    description: |
      For `LeadStatusChange` and `OpportunityStatusChange` activities, the old status type.

  - name: "opens"
    type: "array"
    description: "For `Email` activities, details about the person who opened the email."
    array-attributes:
      - name: "ip_address"
        type: "string"
        description: "The IP address of the person who opened the email."

      - name: "opened_at"
        type: "string"
        description: "The date the email was opened."

      - name: "opened_by"
        type: "string"
        description: "The ID of the person who opened the email."

      - name: "user_agent"
        type: "string"
        description: "The user agent of the person who opened the email."

  - name: "opens_summary"
    type: "string"
    description: ""

  - name: "opportunity_confidence"
    type: "integer"
    description: "For `OpportunityStatusChange` activities, the confidence score of the opportunity."

  - name: "opportunity_date_won"
    type: "string"
    description: "For `OpportunityStatusChange` activities, the date the opportunity was marked as `won`."

  - name: "opportunity_id"
    type: "string"
    description: "For `OpportunityStatusChange` activities, the ID of the opportunity."

  - name: "opportunity_value"
    type: "integer"
    description: "For `OpportunityStatusChange` activities, the value of the opportunity."

  - name: "opportunity_value_currency"
    type: "string"
    description: "For `OpportunityStatusChange` activities, the currency code of the opportunity value."

  - name: "opportunity_value_formatted"
    type: "string"
    description: "For `OpportunityStatusChange` activities, the formatted version of `opportunity_value."

  - name: "opportunity_value_period"
    type: "string"
    description: "For `OpportunityStatusChange` activities, the value period of the opportunity. For example: `one_time`"

  - name: "organization_id"
    type: "string"
    description: "The ID of the organization associated with the activity."
    foreign-key-id: "organization-id"

  - name: "phone"
    type: "string"
    description: "For `Call` activities, the phone number associated with the activity."

  - name: "recording_url"
    type: "string"
    description: "For `Call` activities, the URL of the recording, if applicable."

  - name: "references"
    type: "array"
    description: "A list of references associated with the activity."
    array-attributes:
      - name: "value"
        type: "string"
        description: "The reference."

  - name: "remote_phone"
    type: "string"
    description: "For `Call` and `SMS` activities, the remote phone number associated with the call or SMS."

  - name: "send_attempts"
    type: "array"
    description: "For `Email` activities, details about the send attempts."
    array-attributes:
      - name: "date"
        type: "string"
        description: "The date the send was attempted."

      - name: "error_class"
        type: "string"
        description: "The error class associated with the send failure."

      - name: "error_message"
        type: "string"
        description: "The error message associated with the send failure."

  - name: "sender"
    type: "string"
    description: |
      For `Email` activities, the email address of the user who sent the email.

  - name: "source"
    type: "string"
    description: "The source of the activity."

  - name: "status"
    type: "string"
    description: |
      For `Email` activities, the status of the email. (`inbox`)

  - name: "subject"
    type: "string"
    description: |
      For `Email` activities, the subject of the email.

  - name: "task_assigned_to"
    type: "string"
    description: "The ID of the user who the task is assigned to."
    foreign-key-id: "user-id"

  - name: "task_assigned_to_name"
    type: "string"
    description: "The name of the user who the task is assigned to."

  - name: "task_id"
    type: "string"
    description: "For `TaskCompleted` activities, the ID of the completed task."
    foreign-key-id: "task-id"

  - name: "task_text"
    type: "string"
    description: "For `TaskCompleted` activities, the text of the completed task."

  - name: "template_id"
    type: "string"
    description: |
      For `Email` activities, the ID of the template that was used in the email.

  - name: "template_name"
    type: "string"
    description: |
      For `Email` activities, the name of the template that was used in the email.

  - name: "thread_id"
    type: "string"
    description: ""

  - name: "to"
    type: "array"
    description: |
      For `Email` activities, a list of the people the email was sent to.
    array-attributes:
      - name: "value"
        type: "string"
        description: "The email address the email was sent to."

  - name: "transferred_from"
    type: "string"
    description: ""

  - name: "transferred_to"
    type: "string"
    description: ""

  - name: "updated_by"
    type: "string"
    description: "The ID of the user who last updated the activity."
    foreign-key-id: "user-id"

  - name: "updated_by_name"
    type: "string"
    description: "The name of the user who last updated the activity."

  - name: "user_id"
    type: "string"
    description: "The ID of the user associated with the activity."
    foreign-key-id: "user-id"

  - name: "user_name"
    type: "string"
    description: "The name of the user associated with the activity."

  - name: "users"
    type: "array"
    description: "For `Created` activities, the list of users associated with the activity."
    array-attributes:
      - name: "id"
        type: "string"
        primary-key: true
        description: "The user ID."
        foreign-key-id: "user-id"

      - name: "date_created"
        type: "string"
        description: "The date the user was created."

      - name: "date_updated"
        type: "string"
        description: "The date the user was last updated."

      - name: "email"
        type: "string"
        description: "The email address associated with the user."

      - name: "first_name"
        type: "string"
        description: "The first name of the user."

      - name: "image"
        type: "string"
        description: "The URL of the user's avatar."

      - name: "last_name"
        type: "string"
        description: "The last name of the user."

      - name: "last_used_timezone"
        type: "string"
        description: "The user's last used timezone."

      - name: "organizations"
        type: "array"
        description: "The list of organizations associated with the user."
        array-attributes:
          - name: "value"
            type: "string"
            description: "The ID of the organization associated with the user."

  - name: "voicemail_duration"
    type: "integer"
    description: |
      For `Call` activities, the duration of the voicemail, if applicable.

  - name: "voicemail_url"
    type: "string"
    description: |
      For `Call` activities, the URL of the voicemail, if applicable.
---