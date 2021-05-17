---
title: "Xero (v1): New wait time for rate limiting"
content-type: "changelog-entry"
date: 2021-04-22
entry-type: updated-feature
entry-category: integration
connection-id: xero
connection-version: 1
pull-request: "https://github.com/singer-io/tap-xero/pull/90"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've added a minute-long wait time to the retry logic for the {{ this-connection.display_name }} integration. This ensures that Stitch doesn't make too many requests to {{ this-connection.display-name }}'s API when retrying on a 429 error.