---
title: "Chargebee (v1) bug fix: Update tax_rate field type"
content-type: "changelog-entry"
date: 2023-10-31
entry-type: bug-fix
entry-category: integration
connection-id: chargebee
connection-version: 1
pull-request: "https://github.com/singer-io/tap-chargebee/pull/102"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've fixed a data type issue in our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to avoid truncating the value of the `tax_rate` field.