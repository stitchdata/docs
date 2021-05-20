---
title: "Zuora (v1) update: Enforce use of UTC"
content-type: "changelog-entry"
date: 2021-04-29
entry-type: updated-feature
entry-category: integration
connection-id: "zuora"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-zuora/pull/56"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

Our code is now explicitly forcing the use of UTC for timestamps for our {{ this-connection.display_name }} integration.

Our requests to the {{ this-connection.display_name }} REST API weren't specifying a timezone while querying, and the integration assumed that no timezone retrieved meant UTC.  This update ensures times are consistently recorded in a UTC format.
