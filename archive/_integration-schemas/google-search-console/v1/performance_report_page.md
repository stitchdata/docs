---
tap: "google-search-console"
version: "1"
key: ""

name: "performance_report_page"
doc-link: "https://support.google.com/webmasters/answer/7576553?hl=en"
singer-schema: "https://github.com/singer-io/tap-google-search-console/blob/master/tap_google_search_console/schemas/performance_report_page.json"
description: |
  The `{{ table.name }}` table contains information about the performance of your sites in Google searches. This particular table is filtered and grouped by your landing page URLs that show up in Google search results.

replication-method: "Key-based Incremental"

api-method:
    name: "postPerformanceReport"
    doc-link: "https://developers.google.com/webmaster-tools/search-console-api-original/v3/searchanalytics/query"
attributes:
  - name: "search_type"
    type: "string"
    primary-key: true
    description: "The search type to filter for. Acceptable values are: `discover`, `googleNews`, `image`, `news`, `video`, and `web`."
    foreign-key-id: "search-type"

  - name: "site_url"
    type: "string"
    primary-key: true
    description: "The site URL."
    foreign-key-id: "site-url"

  - name: "page"
    type: "string"
    primary-key: true
    description: "The final URL linked by a Search result after any skip redirects." 

  - name: "date"
    type: "date-time"
    primary-key: true
    description: "The date and time your site appeared in a Google search."
    replication-key: true
       
  - name: "clicks"
    type: "integer"
    description: "The amount of clicks from a Google search that lead that landed a user on your site."
  - name: "ctr"
    type: "number"
    description: "The click-through rate."
  - name: "impressions"
    type: "integer"
    description: "The amount of links to your sites that exist in a google search."
  - name: "position"
    type: "number"
    description: "The average position of your site in the search result."
---
