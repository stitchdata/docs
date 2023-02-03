---
title: "Mambu (v2) update: New field in the loan_accounts stream"
content-type: "changelog-entry"
date: 2022-01-28
entry-type: updated-feature
entry-category: integration
connection-id: mambu
connection-version: 2
pull-request: "https://github.com/singer-io/tap-mambu/pull/62"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to add an `last_account_appraisal_date` field to the `loan_accounts` stream.