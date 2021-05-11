---
title: "New Xero (v1) feature: Adding archived contacts"
content-type: "changelog-entry"
date: 2021-04-15
entry-type: new-feature
entry-category: integration
connection-id: xero
connection-version: 1
pull-request: "https://github.com/singer-io/tap-xero/pull/84"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

You can now add archived contacts from your {{ this-connection.display_name }} account to the {{ this-connection.display_name }} Stitch integration by changing the `includeArchivedContacts` parameter in the configuration file.

When this parameter is set to `TRUE`, Stitch will replicate `ACTIVE` and `ARCHIVE` contacts to the `contacts` table.