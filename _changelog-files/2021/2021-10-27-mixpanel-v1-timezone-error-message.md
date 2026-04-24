---
title: "Mixpanel (v1) update: New error message for timezone issues"
content-type: "changelog-entry"
date: 2021-10-27
entry-type: improvement
entry-category: integration
connection-id: "mixpanel"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-mixpanel/pull/35"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved how our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration handles errors. An error message will now be returned when there is an issue related to timezones.