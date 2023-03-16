---
title: "Stripe (v1) update: Change events stream date window"
content-type: "changelog-entry"
date: 2022-02-17
entry-type: updated-feature
entry-category: integration
connection-id: stripe
connection-version: 1
pull-request: "https://github.com/singer-io/tap-stripe/pull/120"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

Previously the date window for our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration was one week, which caused some connections with many events' bookmarks to never update.

We've updated this window to one day to allow all events to make it through the date window.