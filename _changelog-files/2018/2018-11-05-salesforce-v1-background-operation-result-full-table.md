---
title: "Salesforce (v1) integrations: BackgroundOperationResult is now Full Table"
content-type: "changelog-entry"
date: 2018-11-05
entry-type: updated-feature
entry-category: integration
connection-id: "salesforce"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-salesforce/pull/58"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've determined that the `BackgroundOperationResult` object doesn't support ordering by `CreatedDate`, meaning that Stitch can't reliably replicate this data incrementally. This table now has a forced Replication Method of Full Table.