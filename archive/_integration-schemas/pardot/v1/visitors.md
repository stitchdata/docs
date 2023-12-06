---
tap: "pardot"
version: "1"
key: "visitor"

name: "visitors"
doc-link: "http://developer.pardot.com/kb/object-field-references/#visitor"
singer-schema: "https://github.com/singer-io/tap-pardot/blob/master/tap_pardot/schemas/visitors.json"
description: |
  The `{{ table.name }}` table contains info about visitors.

replication-method: "Key-based Incremental"

api-method:
  name: "Query visitors"
  doc-link: "http://developer.pardot.com/kb/api-version-3/visitors/"

attributes:
  - name: "id"
    type: "integer"
    primary-key: true
    description: "The visitor ID."
    foreign-key-id: "visitor-id"

  - name: "updated_at"
    type: "date-time"
    replication-key: true
    description: "The time the visitor was last updated."

  - name: "campaign_parameter"
    type: "string"
    description: "The campaign parameter (`utm_campaign`) for the visitor from Google Analytics."

  - name: "content_parameter"
    type: "string"
    description: "The content parameter (`utm_content`) for the visitor from Google Analytics."

  - name: "created_at"
    type: "date-time"
    description: "The time the visitor was created."

  - name: "hostname"
    type: "string"
    description: "The visitor's hostname."

  - name: "ip_address"
    type: "string"
    description: "The visitor's IP address."

  - name: "medium_parameter"
    type: "string"
    description: "The medium parameter (`utm_medium`) for the visitor from Google Analytics."

  - name: "page_view_count"
    type: "integer"
    description: "The number of page views by this visitor."

  - name: "source_parameter"
    type: "string"
    description: "The source parameter (`utm_source`) for the visitor from Google Analytics."

  - name: "term_parameter"
    type: "string"
    description: "The term parameter (`utm_term`) for the visitor from Google Analytics."
---