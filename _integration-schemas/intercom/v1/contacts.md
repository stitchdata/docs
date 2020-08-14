---
tap: "intercom"
version: "1"
key: "contact"

name: "contacts"
doc-link: "https://developers.intercom.com/intercom-api-reference/v2.0/reference#contacts-model"
singer-schema: "https://github.com/singer-io/tap-intercom/blob/master/tap_intercom/schemas/contacts.json"
description: |
  The `{{ table.name }}` table contains info about users and leads in your {{ integration.display_name }} account.

  #### Custom attributes

  If applicable, Stitch will replicate custom fields related to `{{ table.name }}` in {{ integration.display_name }}.

replication-method: "Key-based Incremental"

api-method:
  name: "List all contacts"
  doc-link: "https://developers.intercom.com/intercom-api-reference/v2.0/reference#list-contacts"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The contact ID."
    foreign-key-id: "contact-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the contact was last updated."

  - name: "android_app_name"
    type: "string"
    description: "The name of the Android app the contact is using, if applicable."

  - name: "android_app_version"
    type: "string"
    description: "The version of the Android app the contact is using, if applicable."

  - name: "android_device"
    type: "string"
    description: "The Android device the contact is using, if applicable."

  - name: "android_last_seen_at"
    type: "date-time"
    description: "The last time the contact used the Android app, if applicable."

  - name: "android_os_version"
    type: "string"
    description: "The version of the Android OS the contact is using, if applicable."

  - name: "android_sdk_version"
    type: "string"
    description: "The version of the Android SDK the contact is using, if applicable."

  - name: "avatar"
    type: "string"
    description: ""

  - name: "browser"
    type: "string"
    description: "The name of the browser the contact is using."

  - name: "browser_language"
    type: "string"
    description: "The language set by the browser the contact is using."

  - name: "browser_version"
    type: "string"
    description: The version of the browser the contact is using."

  - name: "companies"
    type: "object"
    description: "Details about the company the contact is associated with."
    subattributes:
      - name: "data"
        type: "array"
        description: "Details about the company the contact is associated with."
        subattributes:
          - name: "id"
            type: "string"
            description: "The {{ integration.display_name }}-defined company ID."
            foreign-key-id: "company-id"

          - name: "type"
            type: "string"
            description: "This will be `company`."

          - name: "url"
            type: "string"
            description: ""

      - name: "has_more"
        type: "boolean"
        description: ""

      - name: "total_count"
        type: "integer"
        description: ""

      - name: "type"
        type: "string"
        description: "This will be `list`."

      - name: "url"
        type: "string"
        description: ""

  - name: "created_at"
    type: "date-time"
    description: "The time the contact was created."

  - name: "custom_attributes"
    type: "object"
    description: "The custom attributes set for the contact."

  - name: "email"
    type: "string"
    description: "The email associated with the lead."

  - name: "external_id"
    type: "string"
    description: "The unique ID for the contact."

  - name: "has_hard_bounced"
    type: "boolean"
    description: "Indicates whether the contact has had an email sent to them hard bounce."

  - name: "ios_app_name"
    type: "string"
    description: "The name of the iOS app the contact is using, if applicable."

  - name: "ios_app_version"
    type: "string"
    description: "The version of the iOS app the contact is using, if applicable."

  - name: "ios_device"
    type: "string"
    description: "The iOS device the contact is using, if applicable."

  - name: "ios_last_seen_at"
    type: "date-time"
    description: "The last time the contact used the iOS app, if applicable."

  - name: "ios_os_version"
    type: "string"
    description: "The version of the iOS OS the contact is using, if applicable."

  - name: "ios_sdk_version"
    type: "string"
    description: "The version of the iOS SDK the contact is using, if applicable."

  - name: "language_override"
    type: "string"
    description: "The preferred language setting for the contact."

  - name: "last_contacted_at"
    type: "date-time"
    description: "The time when the contact was last messaged."

  - name: "last_email_clicked_at"
    type: "date-time"
    description: "The time when the contact last clicked a link in an email sent to them, as a Unix timestamp."

  - name: "last_email_opened_at"
    type: "date-time"
    description: "The time when the contact last opened an email sent to them, as a Unix timestamp."

  - name: "last_replied_at"
    type: "date-time"
    description: "The time when the contact last sent a message, as a Unix timestamp."

  - name: "last_seen_at"
    type: "date-time"
    description: "The time the contact was last seen, as a Unix timestamp."

  - name: "location"
    type: "object"
    description: "Details about the contact's location."
    subattributes:
      - name: "city"
        type: "string"
        description: "The contact's city."

      - name: "country"
        type: "string"
        description: "The contact's country."

      - name: "region"
        type: "string"
        description: "The contact's region."

      - name: "type"
        type: "string"
        description: "This will be `location`."

  - name: "marked_email_as_spam"
    type: "boolean"
    description: "Indicates if the contact has marked an email sent to them as spam."

  - name: "name"
    type: "string"
    description: "The name of the lead."

  - name: "notes"
    type: "object"
    description: "The notes that have been added to the contact."
    subattributes:
      - name: "data"
        type: "array"
        description: "The notes that have been added to the contact."
        subattributes:
          - name: "id"
            type: "string"
            description: "The note ID."

          - name: "type"
            type: "string"
            description: "This will be `note`."

          - name: "url"
            type: "string"
            description: ""

      - name: "has_more"
        type: "boolean"
        description: ""

      - name: "total_count"
        type: "integer"
        description: ""

      - name: "type"
        type: "string"
        description: "This will be `list`."

      - name: "url"
        type: "string"
        description: ""

  - name: "os"
    type: "string"
    description: "The operating system the contact is using."

  - name: "owner_id"
    type: "integer"
    description: "The ID of the admin that has been assigned account ownership of the contact."
    foreign-key-id: "admin-id"

  - name: "phone"
    type: "string"
    description: "The phone number associated with the lead."

  - name: "role"
    type: "string"
    description: "The role of the contact. This will be either `lead` or `user`."

  - name: "signed_up_at"
    type: "date-time"
    description: "The time when a contact signed up, as a Unix timestamp."

  - name: "social_profiles"
    type: "object"
    description: "Details about the social profiles the lead is associated with."
    subattributes:
      - name: "data"
        type: "array"
        description: ""
        subattributes:
          - name: "name"
            type: "string"
            description: "The name of the social service. Ex: `facebook`"

          - name: "type"
            type: "string"
            description: "This will be `social_profile`."

          - name: "url"
            type: "string"
            description: "The URL of the social profile."

      - name: "type"
        type: "string"
        description: ""

  - name: "tags"
    type: "object"
    description: "Details about the tags applied to the contact."
    subattributes:
      - name: "data"
        type: "array"
        description: "Details about the tags applied to the contact."
        subattributes:
          - name: "id"
            type: "string"
            description: "The ID of the tag."
            foreign-key-id: "tag-id"

          - name: "type"
            type: "string"
            description: "This will be `tag`."

          - name: "url"
            type: "string"
            description: ""

      - name: "has_more"
        type: "boolean"
        description: ""

      - name: "total_count"
        type: "integer"
        description: ""

      - name: "type"
        type: "string"
        description: "This will be `list`."

      - name: "url"
        type: "string"
        description: ""

  - name: "type"
    type: "string"
    description: "This will be `contact`."

  - name: "unsubscribed_from_emails"
    type: "boolean"
    description: "Indicates if the contact has unsubscribed from emails."

  - name: "workspace_id"
    type: "string"
    description: "The ID of the workspace the contact is associated with."
---