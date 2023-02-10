---
tap: "snapchat-ads"
version: "1"
key: ""

name: "organizations"
doc-link: https://developers.snapchat.com/api/docs/#get-all-organizations
singer-schema: https://github.com/singer-io/tap-snapchat-ads/blob/master/tap_snapchat_ads/schemas/organizations.json
description: "This stream retrieves all organizations."

replication-method: "Key-based Incremental"

table-key-properties: "id"
valid-replication-keys: "updated_at"

attributes:
  - name: "accepted_term_version"
    type: "string"
    description: ""

  - name: "address_line_1"
    type: "string"
    description: "Address Line 1"

  - name: "administrative_district_level_1"
    type: "string"
    description: "District"

  - name: "configuration_settings"
    type: "object"
    description: "Configuration Settings"
    subattributes:
    - name: "notifications_enabled"
      type: "boolean"
      description: ""


  - name: "contact_email"
    type: "string"
    description: "Emial address to be contacted"

  - name: "contact_name"
    type: "string"
    description: "Name of the contact"

  - name: "contact_phone"
    type: "string"
    description: "Phone number of the Contact"

  - name: "contact_phone_optin"
    type: "boolean"
    description: ""

  - name: "country"
    type: "string"
    description: "Country name"

  - name: "created_at"
    type: "date-time"
    description: "Date of creation"

  - name: "id"
    primary-key: true
    type: "string"
    description: "Organization ID"

  - name: "locality"
    type: "string"
    description: "Locality name"

  - name: "my_display_name"
    type: "string"
    description: "Display name"

  - name: "my_invited_email"
    type: "string"
    description: "Invited Email ID"

  - name: "my_member_id"
    type: "string"
    description: "Member ID"

  - name: "name"
    type: "string"
    description: "Organization name"

  - name: "postal_code"
    type: "string"
    description: "Postal Code"

  - name: "roles"
    type: "array"
    description: "List of Roles"
    subattributes:
    - name: "items"
      type: "string"
      description: ""


  - name: "state"
    type: "string"
    description: "State name"

  - name: "type"
    type: "string"
    description: "Organization type"

  - name: "updated_at"
    type: "date-time"
    description: "Date of last updated"


