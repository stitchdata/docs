---
title: "Salesforce (v1) integrations: Convert integer zero values to prevent schema violations"
content-type: "changelog-entry"
date: 2019-08-27
entry-type: improvement
entry-category: integration
connection-id: "salesforce"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-salesforce/pull/67"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

{{ this-connection.display_name }}'s API occasionally returns `integer` fields with a value of `0.0`, resulting in schema violation errors during Extraction. To prevent this error, the integration now converts `0.0` to `0` if the field can be an `integer`.