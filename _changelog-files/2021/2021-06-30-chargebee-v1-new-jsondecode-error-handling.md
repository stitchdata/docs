---
title: "Chargebee (v1) improvement: New handling for JSONDecode errors"
content-type: "changelog-entry"
date: 2021-06-30
entry-type: improvement
entry-category: "integration"
connection-id: "chargebee"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-chargebee/pull/51/"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've added new helpful error messages for the `invoices` and `transactions` streams when JSONDecode errors are encountered:

- `Sorry, authentication failed. Invalid api key`
- `Did not get response from the server due to an unknown error`