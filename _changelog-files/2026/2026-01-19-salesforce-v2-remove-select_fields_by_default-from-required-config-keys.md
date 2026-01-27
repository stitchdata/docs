---
title: "Salesforce (v2): Remove select_fields_by_default from required config keys"
content-type: "changelog-entry"
date: 2026-01-19
entry-type: improvement
entry-category: integration
connection-id: salesforce
connection-version: 2
pull-request: "https://github.com/singer-io/tap-salesforce/pull/197"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to remove 'select_fields_by_default' from required config keys.