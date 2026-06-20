---
tap: "mailchimp"
version: "2"
key: ""


key: "campaign"
name: "campaigns"
doc-link: "https://mailchimp.com/developer/marketing/api/campaigns/"
singer-schema: "https://github.com/singer-io/tap-mailchimp/tree/master/tap_mailchimp/schemas/campaigns.json"
description: |
  The `{{ table.name }}` table contains info about the campaigns in your {{ integration.display_name }} account.

api-method:
    name: "Get all campaigns"
    doc-link: "https://mailchimp.com/developer/marketing/api/campaigns/list-campaigns/"

replication-method: "Full Table"

table-key-properties: "id"
valid-replication-keys: ""

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The campaign ID."
    foreign-key-id: "campaign-id"

  - name: "ab_split_opts"
    type: "object"
    description: ""
    subattributes:
      - name: "split_test"
        type: "string"
        description: ""

      - name: "pick_winner"
        type: "string"
        description: ""

      - name: "wait_units"
        type: "string"
        description: ""

      - name: "wait_time"
        type: "integer"
        description: ""

      - name: "split_size"
        type: "integer"
        description: ""

      - name: "from_name_a"
        type: "string"
        description: ""

      - name: "from_name_b"
        type: "string"
        description: ""

      - name: "reply_email_a"
        type: "string"
        description: ""

      - name: "reply_email_b"
        type: "string"
        description: ""

      - name: "subject_a"
        type: "string"
        description: ""

      - name: "subject_b"
        type: "string"
        description: ""

      - name: "send_time_a"
        type: "string"
        description: ""

      - name: "send_time_b"
        type: "string"
        description: ""

      - name: "send_time_winner"
        type: "string"
        description: ""

  - name: "archive_url"
    type: "string"
    description: "The link to the campaign’s archive version in ISO 8601 format."

  - name: "content_type"
    type: "string"
    description: |
      How the campaign’s content is put together. Possible values are:

      - `template`
      - `drag_and_drop`
      - `html`
      - `url`

  - name: "create_time"
    type: "date-time"
    description: "The date and time the campaign was created in ISO 8601 format."

  - name: "delivery_status"
    type: "object"
    description: "Updates on campaigns in the process of sending."
    subattributes:
      - name: "enabled"
        type: "boolean"
        description: "Indicates if Campaign Delivery Status is enabled for this account and campaign."

      - name: "can_cancel"
        type: "boolean"
        description: ""

      - name: "status"
        type: "string"
        description: ""

      - name: "emails_sent"
        type: "integer"
        description: ""

      - name: "emails_canceled"
        type: "integer"
        description: ""

  - name: "emails_sent"
    type: "integer"
    description: "The total number of emails sent for this campaign."

  - name: "has_logo_merge_tag"
    type: "boolean"
    description: "Determines if the campaign contains the Brand Logo merge tag."

  - name: "long_archive_url"
    type: "string"
    description: "The original link to the campaign’s archive version."

  - name: "needs_block_refresh"
    type: "boolean"
    description: "Determines if the campaign needs its blocks refreshed by opening the web-based campaign editor."

  - name: "parent_campaign_id"
    type: "string"
    description: "If this campaign is the child of another campaign, this identifies the parent campaign. For Example, for RSS or Automation children."

  - name: "recipients"
    type: "object"
    description: "List settings for the campaign."
    subattributes:
      - name: "list_id"
        type: "string"
        description: "The list ID."
        foreign-key-id: "list-id"

      - name: "list_is_active"
        type: "boolean"
        description: "The status of the list used, namely if it’s deleted or disabled."

      - name: "list_name"
        type: "string"
        description: "The name of the list."

      - name: "recipient_count"
        type: "integer"
        description: ""

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

          - name: "prebuilt_segment_id"
            type: "string"
            description: "The prebuilt segment ID, if a prebuilt segment has been designated for this campaign."

      - name: "segment_text"
        type: "string"
        description: "A description of the segment used for the campaign. Formatted as a string marked up with HTML."

  - name: "report_summary"
    type: "object"
    description: "For sent campaigns, a summary of opens, clicks, and e-commerce data."
    subattributes:
      - name: "opens"
        type: "integer"
        description: "The total number of opens for a campaign."

      - name: "unique_opens"
        type: "integer"
        description: "The number of unique opens."

      - name: "open_rate"
        type: "number"
        description: "The number of unique opens divided by the total number of successful deliveries."

      - name: "clicks"
        type: "integer"
        description: "The total number of clicks for an campaign."

      - name: "subscriber_clicks"
        type: "integer"
        description: "The number of unique clicks."

      - name: "click_rate"
        type: "number"
        description: "The number of unique clicks, divided by the total number of successful deliveries."

      - name: "ecommerce"
        type: "object"
        description: "E-Commerce stats for a campaign."
        subattributes:
          - name: "total_orders"
            type: "integer"
            description: "The total orders for a campaign."

          - name: "total_spent"
            type: "integer"
            description: "The total spent for a campaign. Calculated as the sum of all order totals with no deductions."

          - name: "total_revenue"
            type: "integer"
            description: "The total revenue for a campaign. Calculated as the sum of all order totals minus shipping and tax totals."


  - name: "resendable"
    type: "boolean"
    description: "Determines if the campaign qualifies to be resent to non-openers."

  - name: "rss_opts"
    type: "object"
    description: ""
    subattributes:
      - name: "feed_url"
        type: "string"
        description: ""

      - name: "frequency"
        type: "string"
        description: ""

      - name: "schedule"
        type: "object"
        description: ""
        subattributes:
          - name: "hour"
            type: "integer"
            description: ""

          - name: "daily_send"
            type: "object"
            description: ""
            subattributes:
              - name: "sunday"
                type: "boolean"
                description: ""

              - name: "monday"
                type: "boolean"
                description: ""

              - name: "tuesday"
                type: "boolean"
                description: ""

              - name: "wednesday"
                type: "boolean"
                description: ""

              - name: "thursday"
                type: "boolean"
                description: ""

              - name: "friday"
                type: "boolean"
                description: ""

              - name: "saturday"
                type: "boolean"
                description: ""

          - name: "weekly_send_day"
            type: "string"
            description: ""

          - name: "monthly_send_Date"
            type: "number"
            description: ""

      - name: "last_sent"
        type: "string"
        description: ""

      - name: "constrain_rss_img"
        type: "boolean"
        description: ""

  - name: "send_time"
    type: "date-time"
    description: "The date and time a campaign was sent."

  - name: "settings"
    type: "object"
    description: "The settings for the campaign."
    subattributes:
      - name: "subject_line"
        type: "string"
        description: "The subject line for the campaign."

      - name: "title"
        type: "string"
        description: "The title of the campaign."

      - name: "folder_id"
        type: "string"
        description: "If the campaign is listed in a folder, the ID for the folder."

      - name: "preview_text"
        type: "string"
        description: "The preview text for the campaign."

      - name: "from_name"
        type: "string"
        description: "The `from` name for the campaign."

      - name: "reply_to"
        type: "string"
        description: "The reply-to email address for the campaign."

      - name: "use_conversation"
        type: "boolean"
        description: "Indicates whether {{ integration.display_name }}'s Conversations feature is used to manage out-of-office replies."

      - name: "to_name"
        type: "string"
        description: "The campaign's custom `to` name, typically the first name merge field."

      - name: "authenticate"
        type: "boolean"
        description: "Indicates whether {{ integration.display_name }} authenticated the campaign."

      - name: "auto_footer"
        type: "boolean"
        description: "Indicates whether {{ integration.display_name }}'s default footer is automatically appended to the campaign."

      - name: "inline_css"
        type: "boolean"
        description: "Indicates whether the CSS included with the campaign content is automatically inlined."

      - name: "auto_tweet"
        type: "boolean"
        description: ""

      - name: "auto_fb_post"
        type: "array"
        description: ""
        subattributes:
          - name: "items"
            type: "string"
            description: ""

      - name: "fb_comments"
        type: "boolean"
        description: ""

      - name: "timewarp"
        type: "boolean"
        description: "Indicates if the campaign is sent using the Timewarp feature."

      - name: "template_id"
        type: "string"
        description: "The ID for the template used in the campaign."

      - name: "drag_and_drop"
        type: "boolean"
        description: ""

  - name: "social_card"
    type: "object"
    description: "The preview for the campaign, rendered by social networks like Facebook and Twitter."
    subattributes:
      - name: "image_url"
        type: "string"
        description: "The url for the header image for the card."

      - name: "description"
        type: "string"
        description: "A short summary of the campaign to display."

      - name: "title"
        type: "string"
        description: "The title for the card. Typically the subject line of the campaign."

  - name: "status"
    type: "string"
    description: "The current status of the campaign."

  - name: "tracking"
    type: "object"
    description: "The tracking options for the campaign."
    subattributes:
      - name: "opens"
        type: "boolean"
        description: "Indicates whether opens are tracked."

      - name: "html_clicks"
        type: "boolean"
        description: "Indicates whether clicks in the HTML version of the automation are tracked."

      - name: "text_clicks"
        type: "boolean"
        description: "Indicates whether clicks are tracked in the plain-text version of the campaign."

      - name: "goal_tracking"
        type: "boolean"
        description: "Indicates whether Goal tracking is enabled."

      - name: "ecomm360"
        type: "boolean"
        description: "Indicates whether eCommerce360 tracking is enabled."

      - name: "google_analytics"
        type: "string"
        description: "The custom slug for Google Analytics tracking."

      - name: "clicktale"
        type: "string"
        description: "The custom slug for ClickTale tracking."

  - name: "type"
    type: "string"
    description: |
      The type of the campaign. Possible values are:

      - `regular`
      - `plaintext`
      - `absplit`
      - `rss`
      - `variate`

  - name: "variate_settings"
    type: "object"
    description: ""
    subattributes:
      - name: "winning_combination_id"
        type: "string"
        description: ""

      - name: "winning_campaign_id"
        type: "string"
        description: ""

      - name: "winner_criteria"
        type: "string"
        description: ""

      - name: "wait_time"
        type: "integer"
        description: ""

      - name: "test_size"
        type: "integer"
        description: ""

      - name: "subject_lines"
        type: "array"
        description: ""
        subattributes:
          - name: "items"
            type: "string"
            description: ""

      - name: "send_times"
        type: "array"
        description: ""
        subattributes:
          - name: "items"
            type: "string"
            description: ""

      - name: "from_names"
        type: "array"
        description: ""
        subattributes:
          - name: "items"
            type: "string"
            description: ""

      - name: "reply_to_addresses"
        type: "array"
        description: ""
        subattributes:
          - name: "items"
            type: "string"
            description: ""

      - name: "contents"
        type: "array"
        description: ""
        subattributes:
          - name: "items"
            type: "string"
            description: ""

      - name: "combinations"
        type: "array"
        description: ""
        subattributes:
          - name: "id"
            type: "string"
            description: ""

          - name: "subject_line"
            type: "integer"
            description: ""

          - name: "send_time"
            type: "integer"
            description: ""

          - name: "from_name"
            type: "integer"
            description: ""

          - name: "reply_to"
            type: "integer"
            description: ""

          - name: "content_description"
            type: "integer"
            description: ""

          - name: "recipients"
            type: "integer"
            description: ""

  - name: "web_id"
    type: "integer"
    description: "The ID used in the {{ integration.display_name }} web application."