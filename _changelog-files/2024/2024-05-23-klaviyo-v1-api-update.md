---
title: "Klaviyo (v1) update: API upgrade"
content-type: "changelog-entry"
date: 2024-05-23
entry-type: updated-feature
entry-category: integration
connection-id: tap-klaviyo
connection-version: 1
pull-request: "https://github.com/singer-io/tap-klaviyo/pull/67"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated the {{ this-connection.display_name }} integration's API version.

The base URL has been updated for all streams.

The API key authorization has been moved from the query parameters to the request headers.

The schema for all streams has been updated to include all relevant fields.

New tables have been added: `subscribed_to_email` and `subscribed_to_sms`.