---
title: "Typeform (v1) update: Pagination for landings"
content-type: "changelog-entry"
date: 2021-10-29
entry-type: improvement
entry-category: integration
connection-id: typeform
connection-version: 1
pull-request: "https://github.com/singer-io/tap-typeform/pull/48"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to add pagination to the `landings` stream.