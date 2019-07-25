---
tap: "mailchimp"
version: "1.0"

key: "list"
name: "lists"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-mailchimp/blob/master/tap_mailchimp/schemas/lists.json"
description: |
  The `{{ table.name }}` table contains info about all the lists in your {{ integration.display_name }} account. A list is also known as an audience, and is where all contacts are stored and managed in {{ integration.display_name }}.

replication-method: "Full Table"

api-method:
    name: "Get information about all lists"
    doc-link: "https://developer.mailchimp.com/documentation/mailchimp/reference/lists/#read-get_lists"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The list ID."
    foreign-key-id: "list-id"

  - name: "beamer_address"
    type: "string"
    description: |
      The list’s [Email Beamer address](https://mailchimp.com/help/use-email-beamer-to-create-a-campaign/){:target="new"}.

  - name: "campaign_defaults"
    type: "object"
    description: |
      [Default values for campaigns](https://mailchimp.com/help/edit-your-emails-subject-preview-text-from-name-or-from-email-address){:target="new"} created for this list.
    subattributes:
      - name: "from_email"
        type: "string"
        description: "The default from email for campaigns sent to this list."

      - name: "from_name"
        type: "string"
        description: "The default from name for campaigns sent to this list."

      - name: "language"
        type: "string"
        description: "The default language for this lists’s forms."

      - name: "subject"
        type: "string"
        description: "The default subject line for campaigns sent to this list."

  - name: "contact"
    type: "object"
    description: |
      [Contact information displayed in campaign footers](https://mailchimp.com/help/about-campaign-footers){:target="new"} to comply with international spam laws.
    subattributes:
      - name: "address1"
        type: "string"
        description: "The street address for the list contact."

      - name: "address2"
        type: "string"
        description: "The street address for the list contact."

      - name: "city"
        type: "string"
        description: "The city for the list contact."

      - name: "company"
        type: "string"
        description: "The company name for the list."

      - name: "country"
        type: "string"
        description: "A two-character ISO3166 country code. Defaults to `US` if invalid."

      - name: "phone"
        type: "string"
        description: "The phone number for the list contact."

      - name: "state"
        type: "string"
        description: "The state for the list contact."

      - name: "zip"
        type: "string"
        description: "The postal or zip code for the list contact."

  - name: "date_created"
    type: "date-time"
    description: "The date and time that this list was created in ISO 8601 format."

  - name: "double_optin"
    type: "boolean"
    description: "Whether or not to require the subscriber to confirm subscription via email."

  - name: "email_type_option"
    type: "boolean"
    description: "Whether the list supports multiple formats for emails. When set to `true`, subscribers can choose whether they want to receive HTML or plain-text emails. When set to `false`, subscribers will receive HTML emails, with a plain-text alternative backup."

  - name: "has_welcome"
    type: "boolean"
    description: "Whether or not this list has a welcome automation connected."

  - name: "list_rating"
    type: "integer"
    description: "An auto-generated activity score for the list (`0-5`)."

  - name: "marketing_permissions"
    type: "boolean"
    description: "Whether or not the list has marketing permissions (eg. GDPR) enabled."

  - name: "modules"
    type: "array"
    description: "Any list-specific modules installed for this list."
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "name"
    type: "string"
    description: "The name of the list."

  - name: "notify_on_subscribe"
    type: "string"
    description: "The email address to send subscribe notifications to."

  - name: "notify_on_unsubscribe"
    type: "string"
    description: "The email address to send unsubscribe notifications to."

  - name: "permission_reminder"
    type: "string"
    description: |
      The [permission reminder](https://mailchimp.com/help/edit-the-permission-reminder){:target="new"} for the list.

  - name: "stats"
    type: "object"
    description: |
      Stats for the list. According to {{ integration.display_name }}, `"Many of these are cached for at least five minutes."`
    subattributes:
      - name: "avg_sub_rate"
        type: "number"
        description: "The average number of subscriptions per month for the list. **Note**: This field will only have a value if it has been calculated by {{ integration.display_name }}."

      - name: "avg_unsub_rate"
        type: "number"
        description: "The average number of unsubscriptions per month for the list. **Note**: This field will only have a value if it has been calculated by {{ integration.display_name }}."

      - name: "campaign_count"
        type: "integer"
        description: "The number of campaigns in any status that use this list."

      - name: "campaign_last_sent"
        type: "date-time"
        description: "The date and time the last campaign was sent to this list in ISO 8601 format. This is updated when a campaign is sent to 10 or more recipients."

      - name: "cleaned_count"
        type: "integer"
        description: "The number of members cleaned from the list."

      - name: "cleaned_count_since_send"
        type: "integer"
        description: "The number of members cleaned from the list since the last campaign was sent."

      - name: "click_rate"
        type: "number"
        description: "The average click rate, a percentage represented as a number between 0 and 100, per campaign for the list. **Note**: This field will only have a value if it has been calculated by {{ integration.display_name }}."

      - name: "last_sub_date"
        type: "date-time"
        description: "The date and time of the last time someone subscribed to this list in ISO 8601 format."

      - name: "last_unsub_date"
        type: "date-time"
        description: "The date and time of the last time someone unsubscribed from this list in ISO 8601 format."

      - name: "member_count"
        type: "integer"
        description: "The number of active members in the list."

      - name: "member_count_since_send"
        type: "integer"
        description: "The number of active members in the list since the last campaign was sent."

      - name: "merge_field_count"
        type: "integer"
        description: "The number of merge vars for this list (not EMAIL, which is required)."

      - name: "open_rate"
        type: "number"
        description: "The average open rate, a percentage represented as a number between 0 and 100, per campaign for the list. **Note**: This field will only have a value if it has been calculated by {{ integration.display_name }}."

      - name: "target_sub_rate"
        type: "number"
        description: "The target number of subscriptions per month for the list to keep it growing. **Note**: This field will only have a value if it has been calculated by {{ integration.display_name }}."

      - name: "unsubscribe_count"
        type: "integer"
        description: "The number of members who have unsubscribed from the list."

      - name: "unsubscribe_count_since_send"
        type: "integer"
        description: "The number of members who have unsubscribed since the last campaign was sent."

  - name: "subscribe_url_long"
    type: "string"
    description: "The full version of this list’s subscribe form (host will vary)."

  - name: "subscribe_url_short"
    type: "string"
    description: |
      {{ integration.display_name }}'s [EepURL shortened version](https://mailchimp.com/help/share-your-signup-form/){:target="new"} of this list’s subscribe form.

  - name: "use_archive_bar"
    type: "boolean"
    description: "Whether campaigns for this list use the Archive Bar in archives by default."

  - name: "visibility"
    type: "string"
    description: |
      Indicates if the list is [public or private](https://mailchimp.com/help/about-list-publicity/){:target="new"}. Possible values are:

      - `pub` (Public)
      - `prv` (Private)

  - name: "web_id"
    type: "string"
    description: "The ID used in the {{ integration.display_name }} web application. View this list in your {{ integration.display_name }} account at `https://{dc}.admin.mailchimp.com/lists/members/?id={web_id}`."
---