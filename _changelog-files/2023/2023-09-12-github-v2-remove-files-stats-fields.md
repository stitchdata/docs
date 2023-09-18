---
title: "GitHub (v2) update: `files` and `stats` fields from commit-related schemas"
content-type: "changelog-entry"
date: 2023-09-12
entry-type: updated-feature
entry-category: integration
connection-id: github
connection-version: 2
pull-request: "https://github.com/singer-io/tap-github/pull/198"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to remove the `files` and `stats` fields from the `commits` and `pr-commits` streams, since these are not returned by the {{ this-connection.display_name }} API.