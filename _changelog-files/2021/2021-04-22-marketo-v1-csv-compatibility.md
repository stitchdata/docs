---
title: "Marketo (v1) improvement: Improved Stitch compatibility"
content-type: "changelog-entry"
date: 2021-04-22
entry-type: improvement
entry-category: integration
connection-id: marketo
connection-version: 1
pull-request: "https://github.com/singer-io/tap-marketo/pull/73"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved {{ this-connection.display_name }}'s compatibility with Stitch by removing CR and CRLF characters from CSV files. Previously, Extraction would fail due to CR and CRLF characters appearing in unquoted fields.