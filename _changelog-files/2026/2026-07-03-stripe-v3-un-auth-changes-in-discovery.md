---
title: "Stripe (v3): Add implementation to exclude unauthorized streams from discovery"
content-type: "changelog-entry"
date: 2026-07-03
entry-type: improvement
entry-category: integration
connection-id: stripe
connection-version: 3
pull-request: "https://github.com/singer-io/tap-stripe/pull/225"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to add implementation to exclude unauthorized streams from discovery.