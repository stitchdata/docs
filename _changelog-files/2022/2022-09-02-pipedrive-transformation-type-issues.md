---
title: "Pipedrive (v1) bug fix: Transformation and type issues"
content-type: "changelog-entry"
date: 2022-09-02
entry-type: bug-fix
entry-category: integration
connection-id: pipedrive
connection-version: 1
pull-request: "https://github.com/singer-io/tap-pipedrive/pull/120"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've fixed issues related to transformations and `NoneType` objects in our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration.