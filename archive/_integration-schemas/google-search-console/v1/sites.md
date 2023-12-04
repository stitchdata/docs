---
tap: "google-search-console"
version: "1"
key: ""

name: "sites"
doc-link: "https://developers.google.com/webmaster-tools/search-console-api-original/v3/sites"
singer-schema: "https://github.com/singer-io/tap-google-search-console/blob/master/tap_google_search_console/schemas/sites.json"
description: |
  The `{{ table.name }}` contains information about your {{ integration.display_name }} sites at a permission level.

replication-method: "Full Table"

api-method:
    name: "getSites"
    doc-link: "https://developers.google.com/webmaster-tools/search-console-api-original/v3/sites/get"

attributes:
  - name: "site_url"
    type: "string"
    primary-key: true
    description: "The site URL."
    foreign-key-id: "site-url"

  - name: "permission_level"
    type: "string"
    description: |
      The user's permission level for the site. Acceptable values are:
        - `siteFullUser`
        - `siteOwner`
        - `siteRestrictedUser`
        - `siteUnverifiedUser`
---
