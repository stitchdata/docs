---
tap: "square"
version: "1"
key: "location"

name: "locations"
doc-link: "https://developer.squareup.com/reference/square/locations-api"
singer-schema: "https://github.com/singer-io/tap-square/blob/master/tap_square/schemas/locations.json"
description: |
  The `{{ table.name }}` table contains information about all of your business locations in {{ integration.display_name }}.

replication-method: "Full Table"

api-method:
  name: "List locations (V2)"
  doc-link: "https://developer.squareup.com/reference/square/locations-api/list-locations"

attributes:
  - name: "id"
    type: "string"
    primary-key: true
    description: "The location ID."
    foreign-key-id: "location-id"

  - name: "address"
    type: "object"
    description: ""
    subattributes:
      - name: "address_line_1"
        type: "string"
        description: ""

      - name: "address_line_2"
        type: "string"
        description: ""

      - name: "address_line_3"
        type: "string"
        description: ""

      - name: "administrative_district_level_1"
        type: "string"
        description: ""

      - name: "administrative_district_level_2"
        type: "string"
        description: ""

      - name: "administrative_district_level_3"
        type: "string"
        description: ""

      - name: "country"
        type: "string"
        description: ""

      - name: "first_name"
        type: "string"
        description: ""

      - name: "last_name"
        type: "string"
        description: ""

      - name: "locality"
        type: "string"
        description: ""

      - name: "organization"
        type: "string"
        description: ""

      - name: "postal_code"
        type: "string"
        description: ""

      - name: "sublocality"
        type: "string"
        description: ""

      - name: "sublocality_2"
        type: "string"
        description: ""

      - name: "sublocality_3"
        type: "string"
        description: ""

  - name: "business_email"
    type: "string"
    description: ""

  - name: "business_hours"
    type: "object"
    description: ""
    subattributes:
      - name: "periods"
        type: "array"
        description: ""
        subattributes:
          - name: "day_of_week"
            type: "string"
            description: ""

          - name: "end_local_time"
            type: "string"
            description: ""

          - name: "start_local_time"
            type: "string"
            description: ""

  - name: "business_name"
    type: "string"
    description: ""

  - name: "capabilities"
    type: "array"
    description: ""
    subattributes:
      - name: "value"
        type: "string"
        description: ""

  - name: "coordinates"
    type: "object"
    description: ""
    subattributes:
      - name: "latitude"
        type: "singer-decimal"
        description: ""

      - name: "longitude"
        type: "singer-decimal"
        description: ""

  - name: "country"
    type: "string"
    description: ""

  - name: "created_at"
    type: "date-time"
    description: ""

  - name: "currency"
    type: "string"
    description: ""

  - name: "description"
    type: "string"
    description: ""

  - name: "facebook_url"
    type: "string"
    description: ""

  - name: "instagram_username"
    type: "string"
    description: ""

  - name: "language_code"
    type: "string"
    description: ""

  - name: "mcc"
    type: "string"
    description: ""

  - name: "merchant_id"
    type: "string"
    description: ""
    # foreign-key-id: "merchant-id"

  - name: "name"
    type: "string"
    description: ""

  - name: "phone_number"
    type: "string"
    description: ""

  - name: "status"
    type: "string"
    description: ""

  - name: "timezone"
    type: "string"
    description: ""

  - name: "twitter_username"
    type: "string"
    description: ""

  - name: "type"
    type: "string"
    description: ""

  - name: "website_url"
    type: "string"
    description: ""
---