---
title: "Marketo (v1) feature: Implement request timeout"
content-type: "changelog-entry"
date: 2021-11-10
entry-type: new-feature
entry-category: integration
connection-id: marketo
connection-version: 1
pull-request: "https://github.com/singer-io/tap-marketo/pull/78"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've added a request timeout to the {{ this-connection.display_name }} integration for API requests with a default timeout of 300 seconds.