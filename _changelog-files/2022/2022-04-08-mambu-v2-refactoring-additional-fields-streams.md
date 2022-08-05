---
title: "Mambu (v2) update: Continued refactoring and new fields"
content-type: "changelog-entry"
date: 2022-04-08
entry-type: updated-feature
entry-category: integration
connection-id: mambu
connection-version: 2
pull-request: "https://github.com/singer-io/tap-mambu/pull/74"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've made many updates to our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration. See the list below for changes:

- Refactoring of the `credit_arrangements` stream
- Refactoring of the `users` stream
- Refactoring of the `activities` stream
- Refactoring of the `audit_trail` stream
- Added the `interest_accrual_breakdown` stream
- Added new fields to the `tasks` stream
- Added new fields to the `loan_transactions` stream