---
title: "Intaact (v1) update: Match more input filenames"
content-type: "changelog-entry"
date: 2023-08-14
entry-type: improvement
entry-category: integration
connection-id: intaact
connection-version: 1
pull-request: "https://github.com/singer-io/tap-intacct/pull/11"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've updated our {{ this-connection.display_name }} (v{{ this-connection.this-version }}) integration to find any input file whose name starts with `table_name` and ends with `.csv`.