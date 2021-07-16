---
title: "Google Search Console (v1) update: New empty response error exception"
content-type: "changelog-entry"
date: 2021-06-29
entry-type: updated-feature
entry-category: "integration"
connection-id: "google-search-console"
connection-version: 1
pull-request: "https://github.com/singer-io/tap-google-search-console/pull/21"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

To improve the experience of our {{ this-connection.display_name }} integration, we've changed how we handle empty response errors.

Instead of bypassing the error without an explanation, the integration will now raise an error and display it in the Extraction Logs:

```shell
HTTP-error-code: 400, Error: The request is missing or has a bad parameter.