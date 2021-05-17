---
title: "Xero (v1) update: Increased precision for CurrencyRate values"
content-type: "changelog-entry"
date: 2021-04-13
entry-type: updated-feature
entry-category: integration
connection-id: xero
connection-version: 1
pull-request: "https://github.com/singer-io/tap-xero/pull/87"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've increased the `CurrencyRate` field's precision from six decimals to 10. This affects all tables that contain this field.