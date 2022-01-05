---
title: "Mixpanel (v1) improvement: Support EU endpoints"
content-type: "changelog-entry"
date: 2021-10-18
entry-type: improvement
entry-category: integration
connection-id: mixpanel
connection-version: 1
pull-request: "https://github.com/singer-io/tap-mixpanel/pull/39"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

The {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration now supports EU endpoints, with the exception of the `revenue` and `export` streams.