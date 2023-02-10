---
tap: "snapchat-ads"
version: "1"
key: ""

name: "targeting_postal_codes"
doc-link: https://developers.snapchat.com/api/docs/#zipcode
singer-schema: https://github.com/singer-io/tap-snapchat-ads/tree/master/tap_snapchat_ads/schemas/shared/targeting_geo.json
description: "This stream retrieves the list of zipcode targeting options."

replication-method: "Full Table"

table-key-properties: "id"
valid-replication-keys: ""

attributes:
  - name: "city"
    type: "object"
    description: "City details"
    subattributes:
    - name: "id"
      type: "string"
      description: "City ID"

    - name: "name"
      type: "string"
      description: "City Name"


  - name: "continent"
    type: "object"
    description: "Continent Details"
    subattributes:
    - name: "id"
      type: "string"
      description: "Continent ID"

    - name: "name"
      type: "string"
      description: "Continent Short Name. Example: na"

    - name: "full_name"
      type: "string"
      description: "Continent full Name, Example: North America"


  - name: "country"
    type: "object"
    description: "Country details"
    subattributes:
    - name: "id"
      type: "string"
      description: "Country ID"

    - name: "name"
      type: "string"
      description: "Country Name"

    - name: "code"
      type: "string"
      description: "Country Code"

    - name: "code2"
      type: "string"
      description: ""


  - name: "country_code"
    type: "string"
    description: "ISO ALPHA-2 Country Code (lowercase)"

  - name: "id"
    primary-key: true
    type: "string"
    description: "Postal Code ID"

  - name: "metro"
    type: "object"
    description: "Metro Details"
    subattributes:
    - name: "id"
      type: "string"
      description: "Metro ID"

    - name: "name"
      type: "string"
      description: "Metro Name"

    - name: "regions"
      type: "string"
      description: "Region Name"


  - name: "name"
    type: "string"
    description: "Post Office Name"

  - name: "parent_id"
    type: "string"
    description: ""

  - name: "path"
    type: "string"
    description: ""

  - name: "region"
    type: "object"
    description: "Region details"
    subattributes:
    - name: "id"
      type: "string"
      description: "Region ID"

    - name: "code"
      type: "string"
      description: "Region Code"

    - name: "name"
      type: "string"
      description: "Region Name"


  - name: "source"
    type: "string"
    description: "Data Source"

  - name: "targeting_group"
    type: "string"
    description: "Targeting Group. Only possible value for this stream: `geo`"

  - name: "targeting_type"
    type: "string"
    description: "Targeting Type. Only possible value for this stream: `postal code`"


