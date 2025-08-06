---
title: "Xero (v1) update: Replicating archived contacts"
content-type: "changelog-entry"
date: 2021-04-15
entry-type: improvement
entry-category: "integration, documentation"
connection-id: xero
connection-version: 1
pull-request: "https://github.com/singer-io/tap-xero/pull/84"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

Archived contacts can now be included in replication for {{ this-connection.display_name }} integrations.

To replicate records for both archived and active contacts:

- **In the Stitch app**: Check the **Include archived contacts** setting in the **Integration Settings** page
- **In the Connect API**: Set the `include_archived_contacts` property for `platform.xero` to `true`

If this setting isn't enabled, Stitch will replicate data only for active contacts.