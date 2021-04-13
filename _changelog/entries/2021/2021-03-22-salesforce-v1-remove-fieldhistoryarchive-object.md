---
title: "Salesforce (v1): Remove FieldHistoryArchive object"
content-type: "changelog-entry"
date: 2021-03-22
entry-type: removed
entry-category: integration
connection-id: "salesforce"
connection-version: 1
pull-request: "https://github.com/singer-io/tap-salesforce/pull/101"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've determined that the `FieldHistoryArchive` object is incompatible with the {{ this-connection.display_name }} integration's current method of querying, and as a result have removed it from the integration.

Refer to the [tap repository](https://github.com/singer-io/tap-salesforce/blob/master/Blacklisting.md){:target="new"} for more info.