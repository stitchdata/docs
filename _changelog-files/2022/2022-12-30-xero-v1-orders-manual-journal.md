---
title: "Remove `order` query param from manual_journals request"
content-type: "changelog-entry"
date: 2022-12-30
entry-type: bug-fix
entry-category: integration
connection-id: xero
connection-version: 1
pull-request: "https://github.com/singer-io/tap-xero/pull/104"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

The Xero API currently has a bug where all `manual_journal` records created or modified since the last bookmark are returned instead of 100 per page causing, in some instances, API quotas to be exceeded.

Xero support noticed this only happens when `order` is added as a query parameter in the request. This temporary fix removes the `order` query parameter when retrieving data for the `manual_journals` stream until Xero fixes the bug. Data will still be retrieved in it's expected for the {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration.