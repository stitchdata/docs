---
title: "Pipedrive (v1) improvement: Retrieve all organization fields"
content-type: "changelog-entry"
date: 2021-05-26
entry-type: improvement
entry-category: integration
connection-id: pipedrive
connection-version: 1
pull-request: "https://github.com/singer-io/tap-pipedrive/pull/99"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

Previously, fields would be missing from the `organizations` table if there were more than 100 fields available. We've added pagination to the requests the integration makes for `organizations` data, ensuring all fields will be discovered and replicated correctly.