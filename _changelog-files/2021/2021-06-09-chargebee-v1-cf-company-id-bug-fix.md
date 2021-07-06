---
title: "Chargebee (v1) bug fix: Correct issue with cf_company_id data type"
content-type: "changelog-entry"
date: 2021-06-09
entry-type: bug-fix
entry-category: "integration"
connection-id: "chargebee"
connection-version: 1
pull-request: "https://github.com/singer-io/tap-chargebee/pull/48"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

Previously, {{ this-connection.display_name }} integrations could encounter issues related to data typing when replicating the `cf_company_id` field in the `customers` and `events` table. We've addressed this by allowing this field to be either an `integer` or a `string`.