---
title: "Pipedrive (v1) bug fix: Backoff for errors"
content-type: "changelog-entry"
date: 2023-06-07
entry-type: bug-fix
entry-category: integration
connection-id: pipedrive
connection-version: 1
pull-request: "https://github.com/singer-io/tap-pipedrive/pull/115"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've fixed an issue in our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration by adding a backoff in case `5XX` errors occur.