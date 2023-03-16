---
title: "Salesforce (v1): Improved record type handling"
content-type: "changelog-entry"
date: 2017-11-21
entry-type: updated-feature
entry-category: integration
connection-id: "salesforce"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-salesforce/pull/12"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've added handling for several {{ this-connection.display_name }} record types:

- `byte`
- `calculated`
- `DataCategoryGroupReference`
- `masterRecord`