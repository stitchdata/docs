---
title: "Salesforce (v1) integrations: Remove *ChangeEvent tables"
content-type: "changelog-entry"
date: 2019-03-15
entry-type: removed
entry-category: integration
connection-id: "salesforce"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-salesforce/pull/62"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

We've determined that `*ChangeEvent` tables aren't queryable via the {{ this-connection.display_name }} REST or Bulk APIs, and have removed them from the integration. Refer to the [tap repository](https://github.com/singer-io/tap-salesforce/blob/master/Blacklisting.md){:target="new"} for more info.