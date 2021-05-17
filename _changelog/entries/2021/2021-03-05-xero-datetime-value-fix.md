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

Previously, the integration would truncate `date-time` data with a format of `"\/Date(1419937200000+0000)\/"` to `date` only.

This fix ensures that the time component of `date-time` values are correctly preserved.