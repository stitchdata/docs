---
title: "Salesforce (v1) improvement: Error message formatting"
content-type: "changelog-entry"
date: 2021-03-11
entry-type: improvement
entry-category: "integration"
connection-id: "salesforce"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-salesforce/pull/96"
---

{{ site.data.changelog.metadata.single-integration | flatify }}

There are now actionable error messages when `QUERY_TOO_COMPLICATED` errors are encountered for the {{ this-connection.display_name }} integration.