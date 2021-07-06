---
title: "Salesforce (v1) integrations: Improved PK chunking error messages"
content-type: "changelog-entry"
date: 2020-04-01
entry-type: improvement
entry-category: integration
connection-id: "salesforce"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-salesforce/pull/76"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

Error messages resulting from PK (Primary Key) chunking in {{ this-connection.display_name }} integrations have been extended. Previously, only timeout issues were covered by the integration. This improvement adds logic that covers additional situations, such as failure to write query results.