---
title: "Salesforce (v1): ContentFolderItem is no longer supported"
content-type: "changelog-entry"
date: 2018-03-19
entry-type: removed
entry-category: integration
connection-id: "salesforce"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-salesforce/pull/44"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've determined that the `ContentFolderItem` object is incompatible with Stitch's querying strategy, and as a result is no longer available for replication via the {{ this-connection.display_name }} REST API option.