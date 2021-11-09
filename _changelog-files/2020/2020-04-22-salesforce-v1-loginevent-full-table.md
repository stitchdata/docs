---
title: "Salesforce (v1) integrations: LoginEvent is now Full Table"
content-type: "changelog-entry"
date: 2020-04-22
entry-type: updated-feature
entry-category: integration
connection-id: "salesforce"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-salesforce/pull/80"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've determined that the `LoginEvent` object doesn't support ordering by `CreatedDate`, meaning that Stitch can't reliably replicate this data incrementally. This table now has a forced Replication Method of Full Table.