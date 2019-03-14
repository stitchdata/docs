---
tap: "intercom"
# version:

name: "users"
doc-link: https://developers.intercom.io/docs/users
description: |
  The `users` table contains info about the users in your Intercom account.

  #### Custom Attributes

  If applicable, Stitch will replicate custom fields related to `users` in Intercom.

replication-method: "Key-based Incremental"
api-method:
  name: List Users
  doc-link: https://developers.intercom.com/intercom-api-reference/reference#list-users

attribution-window: true

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The user ID."
    foreign-key-id: "user-id"

  - name: "updated_at"
    replication-key: true
    type: "date-time"
    description: "The time the user was last updated."

  - name: "created_at"
    type: "date-time"
    description: "The time the user was added to Intercom."

  - name: "signed_up_at"
    type: "date-time"
    description: "The time the user signed up."

  - name: "email"
    type: "string"
    description: "The email address associated with the user."

  - name: "name"
    type: "string"
    description: "The full name of the user."

  - name: "phone"
    type: "string"
    description: "The phone number associated with the user."

  - name: "last_request_at"
    type: "date-time"
    description: "The time the user last made a request."

  - name: "session_count"
    type: "integer"
    description: "The number of sessions recorded for the user."

  - name: "avatar"
    type: "object"
    description: "Details about the avatar associated with the user."
    subattributes:
      - name: "image_url"
        type: "string"
        description: "The URL of the avatar image associated with the user."

      - name: "type"
        type: "string"
        description: "The value of this field will be `avatar`."

  - name: "unsubscribed_from_emails"
    type: "boolean"
    description: "Indicates if the user is unsubscribed from emails."

  - name: "location_data"
    type: "object"
    description: "Details about the user's location."
    subattributes:
      - name: "city_name"
        type: "string"
        description: "The name of the city associated with the user's location."

      - name: "continent_code"
        type: "string"
        description: "The continent code associated with the user's location."

      - name: "country_code"
        type: "string"
        description: "The country code associated with the user's location."

      - name: "country_name"
        type: "string"
        description: "The name of the country associated with the user's location."

      - name: "latitude"
        type: "integer"
        description: "The latitude associated with the user's location."

      - name: "longitude"
        type: "integer"
        description: "The longitude associated with the user's location."

      - name: "postal_code"
        type: "string"
        description: "The postal code associated with the user's location."

      - name: "region_name"
        type: "string"
        description: "The name of the region associated with the user's location."

      - name: "timezone"
        type: "string"
        description: "The ISO 8601 timezone associated with the user's location."

      - name: "type"
        type: "string"
        description: "The value of this field will be `location_data`."

  - name: "user_agent_data"
    type: "string"
    description: "Data about the last user agent the user was seen using."

  - name: "last_seen_ip"
    type: "string"
    description: "The IP address the user last visited your application from."

  - name: "pseudonym"
    type: "string"
    description: "If the user was previously a lead, this field will contain the pseudonym used. Ex: `Pink Giraffe`"

  - name: "anonymous"
    type: "boolean"
    description: "Indicates if the user is a lead. This will always be `false`."

  - name: "companies"
    type: "array"
    description: "Details about the companies the user is associated with."
    subattributes:
      - name: "id"
        type: "string"
        description: "The Intercom-defined company ID."
        foreign-key-id: "company-id"

      - name: "company_id"
        type: "string"
        description: "The ID that you assigned to the company."

      - name: "name"
        type: "string"
        description: "The name of the company."

      - name: "type"
        type: "string"
        description: "The value of this field will be `company`."

  - name: "social_profiles"
    type: "array"
    description: "Details about the social profiles the user is associated with."
    subattributes:
      - name: "id"
        type: "string"
        description: "The user's user ID on the social platform."

      - name: "name"
        type: "string"
        description: "The name of the social service. Ex: `facebook`"

      - name: "url"
        type: "string"
        description: "The user's user homepage on the social platform."

      - name: "username"
        type: "string"
        description: "The user's username on the social platform."

      - name: "type"
        type: "string"
        description: "The value of this field will be `social_profile`."

  - name: "segments"
    type: "array"
    description: "Details about the segments the user is associated with."
    subattributes:
      - name: "id"
        type: "string"
        description: "The segment ID."
        foreign-key-id: "segment-id"

      - name: "type"
        type: "string"
        description: "The value of this field will be `segment`."

  - name: "tags"
    type: "array"
    description: "Details about the tags the user is associated with."
    subattributes:
      - name: "id"
        type: "string"
        description: "The tag ID."
        foreign-key-id: "tag-id"

      - name: "name"
        type: "string"
        description: "The name of the tag."

      - name: "type"
        type: "string"
        description: "The value of this field will be `tag`."

  - name: "type"
    type: "string"
    description: "The value of this field will be `user`."
---
