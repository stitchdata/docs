---
title: "Typeform (v1) update: Update table to incremental"
content-type: "changelog-entry"
date: 2022-05-17
entry-type: updated-feature
entry-category: integration
connection-id: typeform
connection-version: 1
pull-request: "https://github.com/singer-io/tap-typeform/pull/58"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

Our `landings` table's replication method has been changed from full table to key-based incremental.