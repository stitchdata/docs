---
tap: "mailchimp"
version: "1.0"

key: "list-member"
name: "list_members"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-mailchimp/blob/master/tap_mailchimp/schemas/list_members.json"
description: |
  The `{{ table.name }}` table contains info about the members in a specific {{ integration.display_name }} list.

replication-method: "Key-based Incremental"

replication-key:
  name: "last_modified"

api-method:
    name: "Get information about members in a list"
    doc-link: "https://developer.mailchimp.com/documentation/mailchimp/reference/lists/members/#read-get_lists_list_id_members"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The list member ID. This is the MD5 hash of the lowercase version of the list member’s email address."
    #foreign-key-id: "list-member-id"

  - name: "last_changed"
    type: "date-time"
    replication-key: true
    description: "The date and time the member’s info was last changed in ISO 8601 format."

  - name: "email_address"
    type: "string"
    description: "Email address for a subscriber."

  - name: "email_client"
    type: "string"
    description: "The list member’s email client."

  - name: "email_type"
    type: "string"
    description: |
      The type of email this member asked to get. Possible values are:

      - `html`
      - `text`

  - name: "ip_opt"
    type: "string"
    description: "The IP address the subscriber used to confirm their opt-in status."

  - name: "ip_signup"
    type: "string"
    description: "The IP address the subscriber signed up from."

  - name: "language"
    type: "string"
    description: "If set/detected, the subscriber’s language."
    doc-link: "https://mailchimp.com/help/view-and-edit-contact-languages/?_ga=2.133440206.1967669071.1563545438-786188311.1561484332"

  - name: "list_id"
    type: "string"
    description: "The list ID."
    foreign-key-id: "list-id"

  - name: "location"
    type: "object"
    description: "Subscriber location information."
    subattributes:
      - name: "country_code"
        type: "string"
        description: "The unique code for the location country."

      - name: "dstoff"
        type: "integer"
        description: "The offset for timezones where daylight saving time is observed."

      - name: "gmtoff"
        type: "integer"
        description: "The time difference in hours from GMT."

      - name: "latitude"
        type: "number"
        description: "The location latitude."

      - name: "longitude"
        type: "number"
        description: "  The location longitude."

      - name: "timezone"
        type: "string"
        description: "The timezone for the location."

  - name: "member_rating"
    type: "number"
    description: "Star rating for this member, between `1` and `5`."

  - name: "merge_fields"
    type: "anything"
    description: "An individual merge var and value for a member."

  - name: "source"
    type: "string"
    description: "The source from which the subscriber was added to this list."

  - name: "stats"
    type: "object"
    description: "Open and click rates for this subscriber."
    subattributes:
      - name: "avg_click_rate"
        type: "number"
        description: "The subscriber’s average clickthrough rate."

      - name: "avg_open_rate"
        type: "number"
        description: "The subscriber’s average open rate."

  - name: "status"
    type: "string"
    description: |
      Subscriber’s current status. Possible values are:

      - `subscribed`
      - `unsubscribed`
      - `cleaned`
      - `pending`

  - name: "tags"
    type: "array"
    description: "The tags applied to this member."
    subattributes:
      - name: "id"
        type: "integer"
        description: "The tag ID."

      - name: "name"
        type: "string"
        description: "The name of the tag."

  - name: "tags_count"
    type: "integer"
    description: "The number of tags applied to this member."

  - name: "timestamp_opt"
    type: "date-time"
    description: "The date and time the subscribe confirmed their opt-in status in ISO 8601 format."

  - name: "timestamp_signup"
    type: "date-time"
    description: "The date and time the subscriber signed up for the list in ISO 8601 format."

  - name: "unique_email_id"
    type: "string"
    description: "An identifier for the address across all of {{ integration.display_name }}."

  - name: "unsubscribe_reason"
    type: "string"
    description: "A subscriber’s reason for unsubscribing."

  - name: "vip"
    type: "boolean"
    description: "The VIP status for the subscriber."
    doc-link: "https://mailchimp.com/help/designate-and-send-to-vip-contacts/?_ga=2.138092912.1967669071.1563545438-786188311.1561484332"

  - name: "web_id"
    type: "integer"
    description: "The ID used in the {{ integration.display_name }} web application. View this campaign in your {{ integration.display_name }} account at `https://{dc}.admin.mailchimp.com/campaigns/show/?id={web_id}`."
---