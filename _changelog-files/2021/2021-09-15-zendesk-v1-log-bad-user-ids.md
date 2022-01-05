---
title: "Zendesk (v1) improvement: Log bad user IDs"
content-type: "changelog-entry"
date: 2021-09-15
entry-type: improvement
entry-category: integration
connection-id: zendesk
connection-version: 1
pull-request: "https://github.com/singer-io/tap-zendesk/pull/65"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

The Stitch {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration now logs bad user IDs by forcing the exception code to run.