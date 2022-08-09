---
title: "Pendo (v1) improvement: Integer types received as string value"
content-type: "changelog-entry"
date: 2022-04-28
entry-type: improvement
entry-category: integration
connection-id: pendo
connection-version: 1
pull-request: "https://github.com/singer-io/tap-pendo/pull/97"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

This {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration update receives `integer` attributes from {{ this-connection.display_name }} as `string` values with decimals. This will allow custom metadata types to be more permissive.