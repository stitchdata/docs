---
title: "Mambu (v2) improvement: Timezone improvement"
content-type: "changelog-entry"
date: 2022-09-27
entry-type: improvement
entry-category: integration
connection-id: mambu
connection-version: 2
pull-request: "https://github.com/singer-io/tap-mambu/pull/85"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've improved our {{ this-connection.display_name }} `date-time` fields to eliminate several timezone related issues:

- All `date-time` data has been converted to UTC for processing
- Implemented functionality to get the tenant's timezone so that calculations for the local time are done using the tenant's, and not the local computer's
- The following streams now use `date-time` instead of just `date`: `clients`, `communications`, `deposit_transactions`, `loan_accounts`, `loan_transactions`