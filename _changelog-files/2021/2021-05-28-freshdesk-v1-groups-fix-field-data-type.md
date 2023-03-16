---
title: "Freshdesk (v1) improvement: Correct data type for groups table field"
content-type: "changelog-entry"
date: 2021-05-28
entry-type: improvement
entry-category: integration
connection-id: freshdesk
connection-version: 1
pull-request: "https://github.com/singer-io/tap-freshdesk/pull/42"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've added `integer` as a valid data type for the `groups.auto_ticket_assign` field. Previously, the integration would only accept `boolean` values for this field.

As the {{ this-connection.display_name }} API can return `boolean` or `integer` values, the integration's data typing could cause errors or discrepancies. This improvement ensures data is replicated correctly and without issue.