---
title: "Mambu (v2) update: New field in the loan_accounts stream"
content-type: "changelog-entry"
date: 2021-11-29
entry-type: updated-feature
entry-category: integration
connection-id: "mambu"
connection-version: "2"
pull-request: "https://github.com/singer-io/tap-mambu/pull/60"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to add a `original_account_key` field to the `loan_accounts` stream.