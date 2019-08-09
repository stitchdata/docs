---
tap: "revinate"
# version: "1.0"

name: "reviews"
doc-link: https://porter.revinate.com/documentation#reviews
singer-schema: ## link to the JSON schema file in the integration's Singer repo
description: |
  The `table_name` table contains a subset of the latest reviews for the hotels in your {{ integration.display_name }} account.

   **Note**: Stitch will only replicate review data for the hotels that the user whose API key is used to [authenticate the integration](#add-stitch-data-source) has access to. If you're missing records, verify that the authenticating user has access to those hotels in {{ integration.display_name }}.

replication-method: "Key-based Incremental"

api-method:
  name: Get reviews
  doc-link: https://porter.revinate.com/documentation#reviews

attributes:
  - name: "review_id"
    type: "integer"
    primary-key: true
    description: "The review ID."
    # foreign-key-id: "review-id"

  - name: "updated_at"
    type: "integer"
    replication-key: true
    description: "The time the review was last updated."

  - name: "author"
    type: "string"
    description: "The review author."

  - name: "author_location"
    type: "string"
    description: "The review author's location."

  - name: "body"
    type: "string"
    description: "The body of the review."

  - name: "crawled_url"
    type: "string"
    description: ""

  - name: "date_collected"
    type: "integer"
    description: "The date the review was collected."

  - name: "date_review"
    type: "integer"
    description: "The date of the review."

  - name: "guest_stay_json"
    type: "string"
    description: ""

  - name: "hotel_id"
    type: "integer"
    description: "The hotel ID."
    foreign-key-id: "hotel-id"

  - name: "hotel_url"
    type: "string"
    description: ""

  - name: "language_english_name"
    type: "string"
    description: ""

  - name: "language_id"
    type: "integer"
    description: ""

  - name: "language_json"
    type: "string"
    description: ""

  - name: "language_name"
    type: "string"
    description: ""

  - name: "language_slug"
    type: "string"
    description: ""

  - name: "language_url"
    type: "string"
    description: ""

  - name: "links_json"
    type: "string"
    description: ""

  - name: "nps"
    type: "integer"
    description: ""

  - name: "rating"
    type: "number"
    description: "The rating."

  - name: "response_json"
    type: "string"
    description: ""

  - name: "review_json"
    type: "string"
    description: ""

  - name: "review_site_id"
    type: "integer"
    description: ""
    foreign-key-id: "review-site-id"

  - name: "review_site_json"
    type: "string"
    description: ""

  - name: "review_site_main_url"
    type: "string"
    description: ""

  - name: "review_site_name"
    type: "string"
    description: "The name of the review site the review is on."

  - name: "review_site_url"
    type: "string"
    description: ""

  - name: "review_site_slug"
    type: "string"
    description: ""

  - name: "review_url"
    type: "string"
    description: ""

  - name: "subratings_json"
    type: "string"
    description: ""

  - name: "subratings_cleanliness"
    type: "number"
    description: "The cleanliness subrating associated with the review."

  - name: "subratings_hotel_condition"
    type: "number"
    description: "The hotel condition subrating associated with the review."

  - name: "subratings_rooms"
    type: "number"
    description: "The room subrating associated with the review."

  - name: "subratings_service"
    type: "number"
    description: "The service subrating associated with the review."

  - name: "survey_topics_json"
    type: "string"
    description: ""

  - name: "title"
    type: "string"
    description: "The title of the review."

  - name: "trip_type"
    type: "string"
    description: "The trip type included in the review."
---