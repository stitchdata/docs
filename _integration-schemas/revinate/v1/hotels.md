---
tap: "revinate"
version: "1.0"

name: "hotels"
doc-link: https://porter.revinate.com/documentation#hotels
singer-schema: https://github.com/singer-io/tap-revinate/blob/master/tap_revinate/schemas.py#L1
description: |
  The  `{{ table.name }}` table contains info about the hotels in your {{ integration.display_name }} account.

  **Note**: Stitch will only replicate data for the hotels that the user whose API key is used to [authenticate the integration](#add-stitch-data-source) has access to. If you're missing records, verify that the authenticating user has access to those hotels in {{ integration.display_name }}.

replication-method: "Full Table"

api-method:
  name: Get hotels
  doc-link: https://porter.revinate.com/documentation#hotels

attributes:
  - name: "hotel_id"
    type: "integer"
    primary-key: true
    description: "The hotel ID."
    foreign-key-id: "hotel-id"

  - name: "hotel_url"
    type: "string"
    description: "The hotel URL."

  - name: "hotel_reviews_snapshot_url"
    type: "string"
    description: "The review snapshot URL associated with the hotel."

  - name: "hotel_json"
    type: "string"
    description: ""

  - name: "name"
    type: "string"
    description: "The name of the hotel."

  - name: "slug"
    type: "string"
    description: ""

  - name: "logo"
    type: "string"
    description: "The logo associated with the hotel."

  - name: "url"
    type: "string"
    description: "The hotel URL."

  - name: "address1"
    type: "string"
    description: "The first line of the hotel's address."

  - name: "address2"
    type: "string"
    description: "The second line of the hotel's address."

  - name: "city"
    type: "string"
    description: "The city the hotel is in."

  - name: "state"
    type: "string"
    description: "The state the hotel is in."

  - name: "postal_code"
    type: "string"
    description: "The postal code for the hotel."

  - name: "country"
    type: "string"
    description: "The country the hotel is in."

  - name: "trip_advisor_id"
    type: "integer"
    description: "The trip advisor ID associated with the hotel."
    #foreign-key-id: "trip-advisor-id"

  - name: "revinate_purchase_uri"
    type: "string"
    description: ""

  - name: "revinate_login_uri"
    type: "string"
    description: ""

  - name: "account_type"
    type: "string"
    description: ""

  - name: "links_json"
    type: "string"
    description: ""
---