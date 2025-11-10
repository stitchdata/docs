---
title: "JIRA (v2): Add fallback for JIRA API requests when /search/jql endpoint is unavailable"
content-type: "changelog-entry"
date: 2025-11-06
entry-type: improvement
entry-category: integration
connection-id: jira
connection-version: 2
pull-request: "https://github.com/singer-io/tap-jira/pull/131"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to add fallback for JIRA API requests when /search/jql endpoint is unavailable.