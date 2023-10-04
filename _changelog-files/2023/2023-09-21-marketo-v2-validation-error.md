---
title: "Marketo (v2) bug fix: Max API calls issue"
content-type: "changelog-entry"
date: 2023-09-21
entry-type: bug-fix
entry-category: integration
connection-id: marketo
connection-version: 2
pull-request: "https://github.com/singer-io/tap-marketo/pull/84"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've fixed an issue related to the **Max Daily API Calls** parameter in our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration.