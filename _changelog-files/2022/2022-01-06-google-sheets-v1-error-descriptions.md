---
title: "Google Sheets (v1) bug fix: Return error descriptions"
content-type: "changelog-entry"
date: 2022-01-06
entry-type: bug-fix
entry-category: integration
connection-id: google-sheets
connection-version: 1
pull-request: "https://github.com/singer-io/tap-google-sheets/pull/59"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved how our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration handles errors. The integration will now read status codes from API responses and return the error description when it is available.