---
title: "Kustomer (v1): Exclude unauthorized streams from discovery"
content-type: "changelog-entry"
date: 2026-07-09
entry-type: improvement
entry-category: integration
connection-id: kustomer
connection-version: 1
pull-request: "https://github.com/singer-io/tap-kustomer/pull/35"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to exclude unauthorized streams from discovery.