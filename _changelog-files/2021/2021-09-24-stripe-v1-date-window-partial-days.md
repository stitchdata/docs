---
title: "Stripe (v1) update: Partial days in the date window"
content-type: "changelog-entry"
date: 2021-09-24
entry-type: updated-feature
entry-category: integration
connection-id: stripe
connection-version: 1
pull-request: "https://github.com/singer-io/tap-stripe/pull/100"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

Customers can now write in and request partial days in the date window for the {{ this-connection.display_name }} integration. For example, a `date_window_size` value of `.0.5` will query for half a day at a time.