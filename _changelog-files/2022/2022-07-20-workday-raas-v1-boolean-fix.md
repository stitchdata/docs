---
title: "Workday RaaS (v1) bug fix: Fixed issue with boolean values"
content-type: "changelog-entry"
date: 2022-07-20
entry-type: bug-fix
entry-category: integration
connection-id: workday-raas
connection-version: 1
pull-request: "https://github.com/singer-io/tap-workday-raas/pull/10"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've fixed a bug in our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration causing false positives when evaluating `0` and `1` as boolean values.