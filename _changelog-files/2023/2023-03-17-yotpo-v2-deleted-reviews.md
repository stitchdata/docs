---
title: "Yotpo (v2): Synchronize deleted reviews"
content-type: "changelog-entry"
date: 2023-03-17
entry-type: bug-fix
entry-category: integration
connection-id: yotpo
connection-version: 2
pull-request: "https://github.com/singer-io/tap-yotpo/pull/55"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've fixed an issue related to the `reviews` stream in our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration. The stream will now synchronize deleted reviews.