---
title: "JIRA (v2) update: Retry logic for 503 errors"
content-type: "changelog-entry"
date: 2021-10-04
entry-type: updated-feature
entry-category: "integration"
connection-id: jira
connection-version: 2
pull-request: "https://github.com/singer-io/tap-jira/pull/64"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated the handling of HTTP errors in our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration. Retry logic has been added for error code `503`.
