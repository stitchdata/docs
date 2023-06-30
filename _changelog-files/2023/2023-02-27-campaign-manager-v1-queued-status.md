---
title: "Campaign Manager (v1) update: Handle queued status"
content-type: "changelog-entry"
date: 2023-02-27
entry-type: improvement
entry-category: integration
connection-id: campaign-manager
connection-version: 1
pull-request: "https://github.com/singer-io/tap-doubleclick-campaign-manager/pull/27"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to explicitely handle the `QUEUED` file status.