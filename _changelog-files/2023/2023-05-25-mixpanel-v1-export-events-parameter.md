---
title: "Mixpanel (v1) update: New Export Events parameter"
content-type: "changelog-entry"
date: 2023-05-25
entry-type: new-feature
entry-category: integration
connection-id: mixpanel
connection-version: 1
pull-request: "https://github.com/singer-io/tap-mixpanel/pull/56"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to add a new `Export Events` parameter that allows you to filter data on specific event names.