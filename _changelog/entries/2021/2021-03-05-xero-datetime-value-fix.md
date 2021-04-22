---
title: "Xero (v1) bug fix: Date-time correction"
content-type: "changelog-entry"
date: 2021-03-05
entry-type: bug-fix
entry-category: integration
connection-id: xero
connection-version: 1
pull-request: "https://github.com/singer-io/tap-xero/pull/79"
---

{{ site.data.changelog.metadata.single-integration | flatify }}

The bug was removing the time component of date-time values. The fix ensures that the time component of date-time values are preserved through the replication process.