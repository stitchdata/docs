---
title: "Mambu (v1) bug fix: Query Installments correctly"
content-type: "changelog-entry"
date: 2021-09-16
entry-type: bug-fix
entry-category: integration
connection-id: "mambu"
connection-version: 1
pull-request: "https://github.com/singer-io/tap-mambu/pull/54"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We are now querying the `installments` endpoint correctly for the {{ this-connection.display_name }} integration, using the `start_date` instead of the bookmarked value.