---
title: "RingCentral (v1): Exclude unauthorized streams from catalog"
content-type: "changelog-entry"
date: 2026-11-17
entry-type: improvement
entry-category: integration
connection-id: ringcentral
connection-version: 1
pull-request: "https://github.com/singer-io/tap-ringcentral/pull/26"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to exclude unauthorized streams from catalog.