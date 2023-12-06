---
tap: "pardot"
version: "1"
key: "visit"

name: "visits"
doc-link: "http://developer.pardot.com/kb/object-field-references/#visit"
singer-schema: "https://github.com/singer-io/tap-pardot/blob/master/tap_pardot/schemas/visits.json"
description: |
  The `{{ table.name }}` table contains info about visits.

  **Note**: To replicate this table, you must also set the [`visitors`](#visitors) table to replicate.

replication-method: "Key-based Incremental"

api-method:
  name: "Query visits"
  doc-link: "http://developer.pardot.com/kb/api-version-3/visits/"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    replication-key: true
    description: "The ID of the visit."
    foreign-key-id: "visit-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the visit was last updated."

  - name: "campaign_parameter"
    type: "string"
    description: "The campaign parameter (`utm_campaign`) for the visit from Google Analytics."

  - name: "content_parameter"
    type: "string"
    description: "The content parameter (`utm_content`) for the visit from Google Analytics."

  - name: "created_at"
    type: "date-time"
    description: "The time the visit was created."

  - name: "duration_in_seconds"
    type: "integer"
    description: "The length of the visit, in seconds."

  - name: "first_visitor_page_view_at"
    type: "date-time"
    description: "The time of the first page view for this visit."

  - name: "last_visitor_page_view_at"
    type: "date-time"
    description: "The time of the last page view for this visit."

  - name: "medium_parameter"
    type: "string"
    description: "The medium parameter (`utm_medium`) for the visit from Google Analytics."

  - name: "prospect_id"
    type: "integer"
    description: "The ID of the prospect associated with the visit."
    foreign-key-id: "prospect-id"

  - name: "source_parameter"
    type: "string"
    description: "The source parameter (`utm_source`) for the visit from Google Analytics."

  - name: "term_parameter"
    type: "string"
    description: "The term parameter (`utm_term`) for the visit from Google Analytics."

  - name: "visitor_id"
    type: "integer"
    description: "The ID of the visitor associated with the visit."
    foreign-key-id: "visitor-id"

  - name: "visitor_page_view_count"
    type: "integer"
    description: "The number of page views for this visit."

  - name: "visitor_page_views"
    type: "object"
    description: "Details about page views during the visit."
    subattributes:
      - name: "visitor_page_view"
        type: "array"
        description: "A list of page view events during the visit."
        subattributes:
          - name: "created_at"
            type: "date-time"
            description: "The time the page view was created during the visit."

          - name: "id"
            type: "integer"
            description: "The ID of the page view."

          - name: "title"
            type: "string"
            description: "The title of the page that was viewed."

          - name: "url"
            type: "string"
            description: "The URl of the page that was viewed."
---