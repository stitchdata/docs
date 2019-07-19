---
tap: "mailchimp"
version: "1.0"

key: "campaign"
name: "campaigns"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-mailchimp/blob/master/tap_mailchimp/schemas/campaigns.json"
description: |
  The `{{ table.name }}` table contains info about the campaigns in your {{ integration.display_name }} account.

replication-method: ""

api-method:
    name: "Get all campaigns"
    doc-link: "https://developer.mailchimp.com/documentation/mailchimp/reference/campaigns/#read-get_campaigns"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The campaign ID."
    foreign-key-id: "campaign-id"

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

  - name: "emails_sent"
    type: "integer"
    description: "The total number of emails sent for this campaign."

  - name: "has_logo_merge_tag"
    type: "boolean"
    description: "Determines if the campaign contains the `|BRAND:LOGO|` merge tag."

  - name: "long_archive_url"
    type: "string"
    description: "The original link to the campaign’s archive version."

  - name: "needs_block_refresh"
    type: "boolean"
    description: "Determines if the campaign needs its blocks refreshed by opening the web-based campaign editor."

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

          - name: "saved_segment_id"
            type: "integer"
            description: "The id for an existing saved segment."

      - name: "segment_text"
        type: "string"
        description: "A description of the segment used for the campaign. Formatted as a string marked up with HTML."

  - name: "report_summary"
    type: "object"
    description: "For sent campaigns, a summary of opens, clicks, and e-commerce data."
    subattributes:
      - name: "click_rate"
        type: "number"
        description: "The number of unique clicks, divided by the total number of successful deliveries."

      - name: "clicks"
        type: "integer"
        description: "The total number of clicks for an campaign."

      - name: "ecommerce"
        type: "object"
        description: "E-Commerce stats for a campaign."
        subattributes:
          - name: "total_orders"
            type: "integer"
            description: "The total orders for a campaign."

          - name: "total_revenue"
            type: "integer"
            description: "The total revenue for a campaign. Calculated as the sum of all order totals minus shipping and tax totals."

          - name: "total_spent"
            type: "integer"
            description: "The total spent for a campaign. Calculated as the sum of all order totals with no deductions."

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

  - name: "resendable"
    type: "boolean"
    description: "Determines if the campaign qualifies to be resent to non-openers."

  - name: "send_time"
    type: "date-time"
    description: "The date and time a campaign was sent."

  - name: "settings"
    type: "object"
    description: "The settings for the campaign."
    subattributes:
      - name: "authenticate"
        type: "boolean"
        description: "Indicates whether {{ integration.display_name }} authenticated the campaign."

      - name: "auto_footer"
        type: "boolean"
        description: "Indicates whether {{ integration.display_name }}'s default footer is automatically appended to the campaign."

      - name: "auto_tweet"
        type: "boolean"
        description: ""

      - name: "drag_and_drop"
        type: "boolean"
        description: ""

      - name: "fb_comments"
        type: "boolean"
        description: ""

      - name: "folder_id"
        type: "string"
        description: "If the campaign is listed in a folder, the ID for the folder."

      - name: "from_name"
        type: "string"
        description: "The `from` name for the campaign."

      - name: "inline_css"
        type: "boolean"
        description: "Indicates whether the CSS included with the campaign content is automatically inlined."

      - name: "preview_text"
        type: "string"
        description: "The preview text for the campaign."

      - name: "reply_to"
        type: "string"
        description: "The reply-to email address for the campaign."

      - name: "subject_line"
        type: "string"
        description: "The subject line for the campaign."

      - name: "template_id"
        type: "string"
        description: "The ID for the template used in the campaign."

      - name: "timewarp"
        type: "boolean"
        description: "Indicates if the campaign is sent using the Timewarp feature."

      - name: "title"
        type: "string"
        description: "The title of the campaign."

      - name: "to_name"
        type: "string"
        description: "The campaign's custom `to` name, typically the first name merge field."

      - name: "use_conversation"
        type: "boolean"
        description: "Indicates whether {{ integration.display_name }}'s Conversations feature is used to manage out-of-office replies."

  - name: "social_card"
    type: "object"
    description: "The preview for the campaign, rendered by social networks like Facebook and Twitter."
    subattributes:
      - name: "description"
        type: "string"
        description: "A short summary of the campaign to display."

      - name: "image_url"
        type: "string"
        description: "The url for the header image for the card."

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

      - name: "text_clicks"
        type: "boolean"
        description: "Indicates whether clicks are tracked in the plain-text version of the campaign."

  - name: "type"
    type: "string"
    description: |
      The type of the campaign. Possible values are:

      - `regular`
      - `plaintext`
      - `absplit`
      - `rss`
      - `variate`

  - name: "web_id"
    type: "integer"
    description: "The ID used in the {{ integration.display_name }} web application. View this campaign in your {{ integration.display_name }} account at `https://{dc}.admin.mailchimp.com/campaigns/show/?id={web_id}`."
---