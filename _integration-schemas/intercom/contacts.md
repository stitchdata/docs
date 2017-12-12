---
tap: "intercom"
# version:

name: "contacts"
doc-link: https://developers.intercom.com/reference#leads
description: |
  The `contacts` table contains info about the logged-out users, or leads, of your Intercom app.

  **Note**: `contacts` is equivalent to the `leads` object in Intercom's API. See [Intercom's documentation](https://developers.intercom.com/reference#leads) for more info.

  #### Custom Attributes

  If applicable, Stitch will replicate custom fields related to `contacts` (leads) in Intercom.
 
replication-method: "Incremental"
api-method:
  name: listLeads
  doc-link: https://developers.intercom.com/reference#list-leads

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The lead's Intercom-defined ID."

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the lead was last updated."

  - name: "created_at"
    type: "date-time"
    description: "The time the lead was added to Intercom."

  - name: "user_id"
    type: "string"
    description: "An Intercom-generated ID for the lead."

  - name: "email"
    type: "string"
    description: "The email associated with the lead."

  - name: "phone"
    type: "string"
    description: "The phone number associated with the lead."

  - name: "name"
    type: "string"
    description: "The name of the lead."

  - name: "last_request_at"
    type: "date-time"
    description: "The time the lead last made a request."

  - name: "avatar"
    type: "object"
    description: "Details about the avatar associated with the lead."
    object-attributes:
      - name: "image_url"
        type: "string"
        description: "The URL of the avatar image associated with the lead."

      - name: "type"
        type: "string"
        description: "The value of this field will be `avatar`."

  - name: "unsubscribed_from_emails"
    type: "boolean"
    description: "Indicates if the lead is unsubscribed from emails."

  - name: "location_data"
    type: "object"
    description: "Details about the lead's location."
    object-attributes:
      - name: "city_name"
        type: "string"
        description: "The name of the city associated with the lead's location."

      - name: "continent_code"
        type: "string"
        description: "The continent code associated with the lead's location."

      - name: "country_code"
        type: "string"
        description: "The country code associated with the lead's location."

      - name: "country_name"
        type: "string"
        description: "The name of the country associated with the lead's location."

      - name: "latitude"
        type: "integer"
        description: "The latitude associated with the lead's location."

      - name: "longitude"
        type: "integer"
        description: "The longitude associated with the lead's location."

      - name: "postal_code"
        type: "string"
        description: "The postal code associated with the lead's location."

      - name: "region_name"
        type: "string"
        description: "The name of the region associated with the lead's location."

      - name: "timezone"
        type: "string"
        description: "The ISO 8601 timezone associated with the lead's location."

      - name: "type"
        type: "string"
        description: "The value of this field will be `location_data`."

  - name: "user_agent_data"
    type: "string"
    description: "Data about the last user agent the lead was seen using."

  - name: "last_seen_ip"
    type: "string"
    description: "The IP address the lead last visited your application from."

  - name: "companies"
    type: "array"
    description: "Details about the companies the lead is associated with."
    array-attributes:
      - name: "id"
        type: "string"
        description: "The Intercom-defined company ID."
        # foreign-keys:
        #   - table: "companies"
        #     attribute: "id"

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
    description: "Details about the social profiles the lead is associated with."
    array-attributes:
      - name: "id"
        type: "string"
        description: "The lead's user ID on the social platform."

      - name: "name"
        type: "string"
        description: "The name of the social service. Ex: `facebook`"

      - name: "url"
        type: "string"
        description: "The lead's user homepage on the social platform."

      - name: "username"
        type: "string"
        description: "The lead's username on the social platform."

      - name: "type"
        type: "string"
        description: "The value of this field will be `social_profile`."

  - name: "segments"
    type: "array"
    description: "Details about the segments the lead is associated with."
    array-attributes:
      - name: "id"
        type: "string"
        description: "The segment ID."
        # foreign-keys:
        #   - table: "segments"
        #     attribute: "id"

      - name: "type"
        type: "string"
        description: "The value of this field will be `segment`."

  - name: "tags"
    type: "array"
    description: "Details about the tags the lead is associated with."
    array-attributes:
      - name: "id"
        type: "string"
        description: "The tag ID."
        # foreign-keys:
        #   - table: "tags"
        #     attribute: "id"

      - name: "name"
        type: "string"
        description: "The name of the tag."

      - name: "type"
        type: "string"
        description: "The value of this field will be `tag`."
---