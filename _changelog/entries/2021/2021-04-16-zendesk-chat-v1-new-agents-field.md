---
title: "Zendesk Chat (v1) update: New field!"
content-type: "changelog-entry"
date: 2021-04-16
entry-type: updated-feature
entry-category: integration
connection-id: zendesk-chat
connection-version: 1
pull-request: "https://github.com/singer-io/tap-zendesk-chat/pull/27"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

A new field has been added to our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration!

The new `enabled_departments` field is now available for replication in the [`agents`]({{ this-connection.url | prepend: site.baseurl | append: "#agents"}}) table.