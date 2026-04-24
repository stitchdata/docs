---
title: "Pipedrive (v1) removal: Removed delete_logs table"
content-type: "changelog-entry"
date: 2021-05-26
entry-type: removed
entry-category: integration
connection-id: pipedrive
connection-version: 1
pull-request: "https://github.com/singer-io/tap-pipedrive/pull/99"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've removed the `delete_logs` table from our {{ this-connection.display_name }} integration, as {{ this-connection.display_name }} has removed support for it.