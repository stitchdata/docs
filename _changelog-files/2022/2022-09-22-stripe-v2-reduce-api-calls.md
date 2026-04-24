---
title: "Stripe (v2) update: Reduce API calls"
content-type: "changelog-entry"
date: 2022-09-22
entry-type: improvement
entry-category: integration
connection-id: stripe
connection-version: 2
pull-request: "https://github.com/singer-io/tap-stripe/pull/150"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to reduce the amount of calls made to the {{ this-connection.display_name }} API. The integration now extracts data from the last 7 days by default. This date range is configurable and can be set to a maximum of 30 days.