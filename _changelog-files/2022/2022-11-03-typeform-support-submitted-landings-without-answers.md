---
title: "Typeform (v2): Support submitted landings without answers"
content-type: "changelog-entry"
date: 2022-11-03
entry-type: bug-fix
entry-category: integration
connection-id: typeform
connection-version: 2
pull-request: "https://github.com/singer-io/tap-typeform/pull/69"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've fixed an issue in our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration causing the data extraction to fail when at least one submitted landing had no answer. The integration will now check if a stream's child key is blank before trying to process its children.