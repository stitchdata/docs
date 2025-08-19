---
title: "Mixpanel (v1): Update `engage` schema"
content-type: "changelog-entry"
date: 2025-02-20
entry-type: improvement
entry-category: integration
connection-id: mixpanel
connection-version: 1
pull-request: "https://github.com/singer-io/tap-mixpanel/pull/65"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration by removing `required: False` from the `engage` schema.