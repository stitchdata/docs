---
title: "Stripe (v3): Add transfer_reversals stream"
content-type: "changelog-entry"
date: 2025-12-22
entry-type: improvement
entry-category: integration
connection-id: stripe
connection-version: 3
pull-request: "https://github.com/singer-io/tap-stripe/pull/216"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to add `transfer_reversals` stream.