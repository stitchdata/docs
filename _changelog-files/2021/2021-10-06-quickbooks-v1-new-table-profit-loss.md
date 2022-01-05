---
title: "Quickbooks (v1) update: New ProfitAndLossReport table!"
content-type: "changelog-entry"
date: 2021-10-06
entry-type: updated-feature
entry-category: integration
connection-id: quickbooks
connection-version: 1
pull-request: "https://github.com/singer-io/tap-quickbooks/pull/44"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've added a new table to our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration!

The new `profit_loss_report` table contains info about the account profits and losses accesible to the user who authorized the {{ this-connection.display_name }} integration in Stitch.
