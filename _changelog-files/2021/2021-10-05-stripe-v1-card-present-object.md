---
title: "Stripe (v1) update: New Charges object"
content-type: "changelog-entry"
date: 2021-10-05
entry-type: updated-feature
entry-category: integration
connection-id: stripe
connection-version: 1
pull-request: "https://github.com/singer-io/tap-stripe/pull/101"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've added the `card_present` object to our {{ this-connection.display_name }} integration's `charges` table.

