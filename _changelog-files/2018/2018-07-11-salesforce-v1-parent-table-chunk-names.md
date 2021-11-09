---
title: "Salesforce (v1) integrations: Add suffix to parent tables ending in __"
content-type: "changelog-entry"
date: 2018-07-11
entry-type: bug-fix
entry-category: integration
connection-id: "salesforce"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-salesforce/pull/51"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

Previously, {{ this-connection.display_name }} integrations attempted to perform PK (Primary Key) chunking for custom tables using an incorrect parent table name. This fix now appends `c` to parent tables ending in `__`, ensuring chunking is performed correctly.