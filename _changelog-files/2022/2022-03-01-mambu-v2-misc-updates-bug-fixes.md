---
title: "Mambu (v2) update: Misc bug fixes and feature updates"
content-type: "changelog-entry"
date: 2022-03-01
entry-type: improvement
entry-category: integration
connection-id: mambu
connection-version: 2
pull-request: "https://github.com/singer-io/tap-mambu/pull/68"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've made many updates to our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration. See the list below for changes:

- added `currency` field to `loan_accounts`
- added `payment_details` field to `deposit_transactions`
- added `status` field to `tasks` stream
- added sorting to `gl_journal_entries` stream
- fixed `loan_accounts` being skipped if updated while the extraction is running
- refactored `deposit_accounts` and `cards` streams