---
title: "Outreach (v1) update: New field!"
content-type: "changelog-entry"
date: 2021-06-28
entry-type: updated-feature
entry-category: "integration"
connection-id: "outreach"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-outreach/pull/13"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

A new field has been added to our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration!

The new `name` field is now available for replication in the `events` table.