---
title: "Zuora (v1): Ignore unsupported related objects"
content-type: "changelog-entry"
date: 2023-01-31
entry-type: bug-fix
entry-category: integration
connection-id: zuora
connection-version: 1
pull-request: "https://github.com/singer-io/tap-zuora/pull/73"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've fixed a bug with related objects in our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration. Fields that cause issues when added as related objects will now be ignored.