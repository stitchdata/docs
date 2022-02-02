---
title: "Typeform (v1) bug fix: IndexError issue in landings pagination"
content-type: "changelog-entry"
date: 2021-10-29
entry-type: bug-fix
entry-category: integration
connection-id: typeform
connection-version: 1
pull-request: "https://github.com/singer-io/tap-typeform/pull/51"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've fixed an issue with our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration where an `IndexError` was returned when indexing the `items` list in landings pagination. Stitch will now check if `items` is empty.