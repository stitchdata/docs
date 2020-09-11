---
tap: "google-search-console"
version: "1"
key: ""

name: "sites"
doc-link: ""
singer-schema: "https://github.com/singer-io/tap-google-search-console/blob/master/tap_google_search_console/schemas/sites.json"
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

  - name: "permission_level"
    type: "string"
    description: ""
---
