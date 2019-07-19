---
tap: "mailchimp"
version: "1.0"

key: "automation"
name: "automations"
doc-link: "https://developer.mailchimp.com/documentation/mailchimp/reference/automations/#read-get_automations"
singer-schema: "https://github.com/singer-io/tap-mailchimp/blob/master/tap_mailchimp/schemas/automations.json"
description: |
  The `{{ table.name }}` table contains summary info about your {{ integration.display_name }} account's automations.

replication-method: ""

api-method:
    name: "Get a list of automations"
    doc-link: "https://developer.mailchimp.com/documentation/mailchimp/reference/automations/#read-get_automations"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The automation ID."
    foreign-key-id: "automation-id"

  - name: "create_time"
    type: "date-time"
    replication-key: true
    description: "The date and time the Automation was created in ISO 8601 format."

  - name: "emails_sent"
    type: "integer"
    description: ""

  - name: "recipients"
    type: "object"
    description: "The list settings for the automation."
    subattributes:
      - name: "list_id"
        type: "string"
        description: "The list ID."
        foreign-key-id: "list-id"

      - name: "list_is_active"
        type: "boolean"
        description: "The status of the list used, namely if it's deleted or disabled."

      - name: "list_name"
        type: "string"
        description: "The name of the list."

      - name: "segment_opts"
        type: "object"
        description: "Details about segmentation options."
        subattributes:
          - name: "match"
            type: "string"
            description: |
              The segment match type. Possible values are:

              - `any`
              - `all`

          - name: "saved_segment_id"
            type: "integer"
            description: "The ID for an existing saved segment."

          - name: "conditions"
            type: "array"
            description: "Details about segment conditions."
            subattributes:
              - name: "condition_type"
                type: "string"
                description: "The type of the segment."

              - name: "field"
                type: "string"
                description: "The segment field."

              - name: "op"
                type: "string"
                description: "The operator."

              - name: "value"
                type: "string"
                description: "The value."

      - name: "store_id"
        type: "string"
        description: "The ID of the store."

  - name: "report_summary"
    type: "object"
    description: "A summary of opens, clicks, and unsubscribes for sent campaigns."
    subattributes:
      - name: "click_rate"
        type: "number"
        description: "The number of unique clicks, divided by the total number of successful deliveries."

      - name: "clicks"
        type: "integer"
        description: "The total number of clicks for an campaign."

      - name: "open_rate"
        type: "number"
        description: "The number of unique opens divided by the total number of successful deliveries."

      - name: "opens"
        type: "integer"
        description: "The total number of opens for a campaign."

      - name: "subscriber_clicks"
        type: "integer"
        description: "The number of unique clicks."

      - name: "unique_opens"
        type: "integer"
        description: "The number of unique opens."

  - name: "settings"
    type: "object"
    description: "The settings for the automation workflow."
    subattributes:
      - name: "authenticate"
        type: "boolean"
        description: "Indicates whether {{ integration.display_name }} authenticated the automation."

      - name: "auto_footer"
        type: "boolean"
        description: "Indicates whether {{ integration.display_name }}'s default footer is automatically appended to the automation."

      - name: "from_name"
        type: "string"
        description: "The `from` name for the automation."

      - name: "inline_css"
        type: "boolean"
        description: "Indicates whether the CSS included with the automation content is automatically inlined."

      - name: "reply_to"
        type: "string"
        description: "The reply-to email address for the automation."

      - name: "title"
        type: "string"
        description: "The title of the automation."

      - name: "to_name"
        type: "string"
        description: "The automation's custom `to` name, typically the first name merge field."

      - name: "use_conversation"
        type: "boolean"
        description: "Indicates whether {{ integration.display_name }}'s Conversations feature is used to manage out-of-office replies."

  - name: "start_time"
    type: "date-time"
    description: "The date and time the Automation was started in ISO 8601 format."

  - name: "status"
    type: "string"
    description: |
      The current status of the Automation. Possible values are:

      - `save`
      - `paused`
      - `sending`

  - name: "tracking"
    type: "object"
    description: "The tracking options for the automation."
    subattributes:
      - name: "capsule"
        type: "object"
        description: "Capsule tracking options for the automation."
        subattributes:
          - name: "notes"
            type: "boolean"
            description: "Indicates whether contact notes are updated for a campaign based on a subscriber's email address."

      - name: "clicktale"
        type: "string"
        description: "The custom slug for ClickTale tracking."

      - name: "ecomm360"
        type: "boolean"
        description: "Indicates whether eCommerce360 tracking is enabled."

      - name: "goal_tracking"
        type: "boolean"
        description: "Indicates whether Goal tracking is enabled."

      - name: "google_analytics"
        type: "string"
        description: "The custom slug for Google Analytics tracking."

      - name: "html_clicks"
        type: "boolean"
        description: "Indicates whether clicks in the HTML version of the automation are tracked."

      - name: "opens"
        type: "boolean"
        description: "Indicates whether opens are tracked."

      - name: "salesforce"
        type: "object"
        description: "Salesforce tracking options for an automation."
        subattributes:
          - name: "campaign"
            type: "boolean"
            description: "Indicates whether a campaign should be created in a connected Salesforce account."

          - name: "notes"
            type: "boolean"
            description: "Indicates whether contact notes are updated for a campaign based on a subscriber's email address."

      - name: "text_clicks"
        type: "boolean"
        description: "Indicates whether clicks are tracked in the plain-text version of the automation."

  - name: "trigger_settings"
    type: "object"
    description: "Available triggers for automation workflows."
    subattributes:
      - name: "runtime"
        type: "string"
        description: |
          A workflow's runtime settings for an automation.

      - name: "workflow_emails_count"
        type: "integer"
        description: "The number of emails in the automation workflow."

      - name: "workflow_title"
        type: "string"
        description: |
          The title of the workflow type.

      - name: "workflow_type"
        type: "string"
        description: |
          The type of the workflow.
---