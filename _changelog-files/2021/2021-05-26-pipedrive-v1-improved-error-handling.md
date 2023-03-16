---
title: "Pipedrive (v1) improvement: Error handling and retries"
content-type: "changelog-entry"
date: 2021-05-26
entry-type: improvement
entry-category: integration
connection-id: pipedrive
connection-version: 1
pull-request: "https://github.com/singer-io/tap-pipedrive/pull/99"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved how our {{ this-connection.display_name }} integration handles errors. Previously, the integration wouldn't retry errors when they were received from the {{ this-connection.display_name }} API. The integration will now retry when errors are encountered for any table.