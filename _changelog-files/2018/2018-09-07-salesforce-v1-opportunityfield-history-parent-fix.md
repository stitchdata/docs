---
title: "Salesforce (v1) integrations: Fix for OpportunityFieldHistory parent"
content-type: "changelog-entry"
date: 2018-09-07
entry-type: bug-fix
entry-category: integration
connection-id: "salesforce"
connection-version: "1"
pull-request: "https://github.com/singer-io/tap-salesforce/pull/52"
---
{{ site.data.changelog.metadata.single-integration | flatify }}

Previously, `OpportunityFieldHistory` exports failed due to a function in the {{ this-connection.display_name }} integration incorrectly returning `OpportunityField` as the parent. This fix adds a check for the `FieldHistory` suffix, ensuring that the parent is correctly returned as `Opportunity`.