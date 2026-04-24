---
title: "Square (v2) update: New payouts stream"
content-type: "changelog-entry"
date: 2023-08-09
entry-type: new-feature
entry-category: integration
connection-id: square
connection-version: 2
pull-request: "https://github.com/singer-io/tap-square/pull/109"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to replace the deprecated `settlements` stream with the `payouts` stream.