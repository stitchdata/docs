---
tap: "google-search-console"
version: "1"
key: ""

name: "sitemaps"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-google-search-console/blob/master/tap_google_search_console/schemas/sitemaps.json"
description: ""

replication-method: "Full Table"

api-method:
    name: ""
    doc-link: ""

attributes:
  - name: "site_url"
    type: "string"
    primary-key: true
    description: "The site URL."
    foreign-key-id: "site-url"

  - name: "path"
    type: "string"
    primary-key: true
    description: "The URL of the sitemap."

  - name: "last_submitted"
    type: "date-time"
    primary-key: true
    description: "The time the sitemap was last downloaded."  
      
  - name: "contents"
    type: "null"
    description: ""
  - name: "errors"
    type: "integer"
    description: ""
  - name: "is_pending"
    type: "boolean"
    description: ""
  - name: "is_sitemaps_index"
    type: "boolean"
    description: ""
  - name: "last_downloaded"
    type: "date-time"
    description: ""
  - name: "type"
    type: "string"
    description: ""
  - name: "warnings"
    type: "integer"
    description: ""
---
