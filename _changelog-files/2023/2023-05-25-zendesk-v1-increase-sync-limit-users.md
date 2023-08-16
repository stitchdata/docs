---
title: "Zendesk Support (v1) update: Increase sync limit for users stream"
content-type: "changelog-entry"
date: 2023-05-25
entry-type: updated-feature
entry-category: integration
connection-id: zendesk
connection-version: 1
pull-request: "https://github.com/singer-io/tap-zendesk/pull/127"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to used the incremental export API for the `users` stream, which allows Stitch to sync more than 1000 records per query.