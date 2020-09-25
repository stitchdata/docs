---
tap: "google-search-console"
version: "1"
key: ""

name: "sitemaps"
doc-link: "https://developers.google.com/webmaster-tools/search-console-api-original/v3/sitemaps"
singer-schema: "https://github.com/singer-io/tap-google-search-console/blob/master/tap_google_search_console/schemas/sitemaps.json"
description: |
  The `{{ table.name }}` table contains information about the sitemap entries in your {{ integration.display_name }}.

replication-method: "Full Table"

api-method:
    name: "listSitemaps"
    doc-link: "https://developers.google.com/webmaster-tools/search-console-api-original/v3/sitemaps/list"

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
    type: "string"
    description: |
      The type of content in the sitemap. Acceptable values are:
        - `androidApp`
        - `image`
        - `iosApp`
        - `mobile`
        - `news`
        - `pattern`
        - `video`
        - `web`
  - name: "errors"
    type: "integer"
    description: "The number of errors in the sitemap."
  - name: "is_pending"
    type: "boolean"
    description: "Whether or not the sitemap has been processed. If `true`, the sitemap as not been processed."
  - name: "is_sitemaps_index"
    type: "boolean"
    description: "Whether or not this is a sitemap index file. If `true`, it is a sitemap index file."
  - name: "last_downloaded"
    type: "date-time"
    description: "The time the sitmap was last downloaded."
  - name: "type"
    type: "string"
    description: |
      The type of sitemap. Acceptable values are:
        - `atomFeed`
        - `notSitemap`
        - `patternSitemap`
        - `rssFeed`
        - `sitemap`
        - `urlList`
  - name: "warnings"
    type: "integer"
    description: "The number of warnings for the sitemap."
---
