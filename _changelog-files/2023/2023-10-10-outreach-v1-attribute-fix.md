---
title: "Outreach (v1): Fix issue with attribute"
content-type: "changelog-entry"
date: 2023-10-10
entry-type: bug-fix
entry-category: integration
connection-id: outreach
connection-version: 1
pull-request: "https://github.com/singer-io/tap-outreach/pull/32"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to fix an issue related to an attribute in the `mailings` stream.