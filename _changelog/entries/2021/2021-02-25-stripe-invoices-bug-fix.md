---
title: "Stripe (v1) bug fix: Removed fields causing issues"
content-type: "changelog-entry"
date: 2021-02-25
entry-type: bug-fix
entry-category: integration
connection-id: stripe
connection-version: 1
full-connection-version: "1.4.6"
pull-request: "https://github.com/singer-io/tap-stripe/pull/79"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

The `custom_fields` object in the {{ this-connection.display_name }} (v1) integration `invoices` table have been removed, as they were causing issues.