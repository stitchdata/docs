---
title: "Mixpanel (v1) bug fix: timezone issue in date-time conversions"
content-type: "changelog-entry"
date: 2021-10-27
entry-type: bug-fix
entry-category: integration
connection-id: "mixpanel"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-mixpanel/pull/40"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've fixed an issue with our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration where timezones were ignored when writing UTC `date-time` values. The integration can now write the correct UTC `date-time` value based on the timezone in your {{ this-connection.display_name }} project.