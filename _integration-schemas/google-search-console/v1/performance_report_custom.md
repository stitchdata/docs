---
tap: "google-search-console"
version: "1"
key: ""
name: "performance_report_custom"
doc-link: "https://support.google.com/webmasters/answer/7576553?hl=en"
singer-schema: "https://github.com/singer-io/tap-google-search-console/blob/master/tap_google_search_console/schemas/performance_report_custom.json"
description: |
  The `{{ table.name }}` table contains information about the performance of your sites in Google searches. This particular table is filtered and grouped by your custom dimensions.

replication-method: "Key-based Incremental"

api-method:
    name: "postPerformanceReport"
    doc-link: "https://developers.google.com/webmaster-tools/search-console-api-original/v3/searchanalytics/query"

attributes:
  - name: "search_type"
    type: "string"
    primary-key: true
    description: "The search type to filter for. Acceptable values are: `image`, `video`, and `web`."
    foreign-key-id: "search-type"

  - name: "site_url"
    type: "string"
    primary-key: true
    description: "The site URL."
    foreign-key-id: "site-url"

  - name: "dimensions_hash_key"
    type: "string"
    primary-key: true
    description: "The MD5 hash key of your selected dimension values."  

  - name: "date"
    type: "date-time"
    primary-key: true
    description: "The date and time your site appeared in a Google search."
    replication-key: true 

  - name: "clicks"
    type: "integer"
    description: "The amount of clicks from a Google search that lead that landed a user on your site."
  - name: "country"
    type: "string"
    description: "The country that the search came from."
  - name: "ctr"
    type: "number"
    description: "The click-through rate."
  - name: "device"
    type: "string"
    description: "The type of device the user was using to search."
  - name: "impressions"
    type: "integer"
    description: "The amount of links to your sites that exist in a google search."
  - name: "page"
    type: "string"
    description: "The final URL linked by a Search result after any skip redirects."
  - name: "position"
    type: "number"
    description: "The average position of your site in the search result."
  - name: "query"
    type: "string"
    description: "The query strings that the user searched for on Google. Only searches that returned your site are shown."
  
---
