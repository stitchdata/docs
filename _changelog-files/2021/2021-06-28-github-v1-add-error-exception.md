---
title: "GitHub (v1) update: New empty response error exception"
content-type: "changelog-entry"
date: 2021-06-28
entry-type: updated-feature
entry-category: "integration"
connection-id: "github"
connection-version: 1
pull-request: "https://github.com/singer-io/tap-github/pull/126"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

To improve the experience of our {{ this-connection.display_name }} integration, we've changed how we handle empty response errors.

Instead of bypassing the error without an explanation, the integration will now raise an error and display it in the Extraction Logs:

```shell
HTTP-error-code: 400, Error: The request is missing or has a bad parameter.
