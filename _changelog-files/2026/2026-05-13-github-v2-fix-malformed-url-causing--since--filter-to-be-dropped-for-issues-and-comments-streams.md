---
title: "GitHub (v2): fix malformed URL causing 'since' filter to be dropped for Issues and Comments streams"
content-type: "changelog-entry"
date: 2026-05-13
entry-type: bug-fix
entry-category: integration
connection-id: github
connection-version: 2
pull-request: "https://github.com/singer-io/tap-github/pull/230"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to fix malformed URL causing 'since' filter to be dropped for Issues and Comments streams.