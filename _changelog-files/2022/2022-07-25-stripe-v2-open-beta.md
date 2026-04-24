---
title: "Stripe integration: New version (v2) now available!"
content-type: "changelog-entry"
date: 2022-07-25
entry-type: new-feature
entry-category: integration
connection-id: "stripe"
connection-version: "2"
#pull-request: "https://github.com/singer-io/tap-stripe/blob/master/CHANGELOG.md"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

A new version (v{{ this-connection.this-version }}) of our {{ this-connection.display_name }} integration is now available!

We've improved the {{ this-connection.display_name }} integration adding a new table and parameter. Here's a look at what has changed:

- New parameter: `lookback_window`. The number of historical days' worth of data to replicate from the `start_date` value for each replication job for your streams. The maximum lookback window is `600` days.
- New table: `payment_intents`. This table contains information about payments, from creation through checkout, in your {{ this-connection.display_name }} account.