---
title: "Pendo (v1) bug fix: Custom field issues for visitors and accounts tables"
content-type: "changelog-entry"
date: 2021-03-10
entry-type: bug-fix
entry-category: "integration"
connection-id: "pendo"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-pendo/pull/27"
---

{{ site.data.changelog.metadata.single-integration | flatify }}

We've fixed a few issues with the {{ this-connection.display_name }} `visitors` and `accounts` tables:

1. Custom fields without a defined data type will no longer return a `null` value.
2. If a table had multiple custom fields, the last field on the table was being overwritten. We've updated the integration to address this.
