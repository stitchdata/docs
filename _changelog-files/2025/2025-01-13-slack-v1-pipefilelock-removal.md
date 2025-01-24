---
title: "Slack (v1) update: `pipefile.lock` removal"
content-type: "changelog-entry"
date: 2025-01-13
entry-type: improvement
entry-category: integration
connection-id: slack
connection-version: 1
pull-request: "https://github.com/singer-io/tap-slack/pull/22"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration by removing `pipefile.lock`.