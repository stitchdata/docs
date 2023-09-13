---
title: "Typeform (v2) update: New property in submitted_landings stream"
content-type: "changelog-entry"
date: 2023-05-31
entry-type: updated-feature
entry-category: integration
connection-id: typeform
connection-version: 2
pull-request: "https://github.com/singer-io/tap-typeform/pull/75"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to add the `tags` property in the `submitted_landings` stream.